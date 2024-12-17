from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyQt6.QtWidgets import QDialog , QMessageBox , QPushButton
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget,QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QInputDialog
import pyodbc
from datetime import datetime
from collections import defaultdict
from PyQt6 import QtGui, QtCore
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QListWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QPushButton, QCheckBox
import os


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__() 
        # Load the .ui file
        uic.loadUi('sales_screen.ui', self) 
        self.conn_string = "Driver={SQL Server};Server=SF\MYSQLSERVER1;Database=safatique;Trusted_Connection=True;"

        # Load data on screen load
        self.load_sales_data()
        # Connect filters to apply_filters  
        self.filterpstatus_2.currentTextChanged.connect(self.apply_filters)
        self.filterpmstatus_2.currentTextChanged.connect(self.apply_filters)
        self.filterfstatus_2.currentTextChanged.connect(self.apply_filters)
        self.date_2.stateChanged.connect(self.apply_filters)
        self.fromdate_2.dateChanged.connect(self.apply_filters)
        self.todate_2.dateChanged.connect(self.apply_filters)
        self.filterproduct_2.textChanged.connect(self.apply_filters)
        self.search.textChanged.connect(self.apply_filters)

        self.allorders_2.stateChanged.connect(self.apply_filters)
        self.paid_2.stateChanged.connect(self.apply_filters)
        self.notpaid_2.stateChanged.connect(self.apply_filters)
        self.fulfillment_2.stateChanged.connect(self.apply_filters)

        self.reportbutton.clicked.connect(self.show_report_screen)
        self.productsbutton.clicked.connect(self.showproducts)
        self.rawmaterial.clicked.connect(self.showEditRawMats)

    def show_sales_screen(self):
        """
        Show the Sales Screen and hide the Products Screen.
        """
        self.products_screen.hide()  # Hide Products Screen
        self.sales_screen.show()  # Show Sales Screen


    def load_sales_data(self):
        """
        Fetch data from the database and populate the UI.
        """
        query = """
        SELECT 
            Orders.order_id,
            Orders.order_date,
            Orders.payment_status,
            Orders.processing_status,
            Customer.firstname,
            Customer.lastname,
            Customer.email,
            Customer.phone,
            Address.address,
            Address.city
        FROM 
            Orders
        JOIN 
            OrderDetails ON Orders.order_id = OrderDetails.order_id
        JOIN 
            Customer ON Orders.customer_id = Customer.customer_id
        JOIN 
            CustomerAddress ON Customer.customer_id = CustomerAddress.customer_id
        JOIN 
            Address ON CustomerAddress.address_id = Address.address_id
        """

        try:
            conn = pyodbc.connect(self.conn_string)
            cursor = conn.cursor()
            cursor.execute(query)
            orders = cursor.fetchall()

            # Populate orders in the scroll area
            self.populate_orders(orders)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to load data: {str(e)}")

    def apply_filters(self):
        """
        Apply filters to update the displayed orders.
        """
        query = """
        SELECT distinct Orders.order_id, order_date, payment_status,
        processing_status, firstname, lastname, email, phone, address, city
        FROM Orders
        JOIN OrderDetails ON Orders.order_id = OrderDetails.order_id
        JOIN Customer ON Orders.customer_id = Customer.customer_id
        JOIN CustomerAddress ON Customer.customer_id = CustomerAddress.customer_id
        JOIN Address ON CustomerAddress.address_id = Address.address_id
        LEFT JOIN CustomerPaymentInfo ON Customer.customer_id = CustomerPaymentInfo.customer_id
        LEFT JOIN PaymentInfo ON CustomerPaymentInfo.payment_id = PaymentInfo.payment_id
        WHERE 1=1
        """
        params = []
    
        if self.paid_2.isChecked():
            query += """
            AND payment_status LIKE 'Paid' AND processing_status LIKE 'Processing'
            """
        elif self.notpaid_2.isChecked():
            query += """
            AND payment_status LIKE 'Awaiting Payment' AND processing_status LIKE 'Processing'
            """

        # Fulfillment status filter (only if fulfillment_2 is checked)
        if self.fulfillment_2.isChecked():
            query += " AND processing_status LIKE 'Processing'"

        # All Orders (when allorders_2 is checked, show everything)
        if self.allorders_2.isChecked():
            pass  # No additional filter for all orders, it shows everything

        payment_mode = self.filterpmstatus_2.currentText()
        # Add the condition for payment_status if it's not "Any"
        if payment_mode != "Any":
            query += """
            AND (CASE
                    WHEN PaymentInfo.payment_id IS NULL THEN 'Bank Transfer'
                    ELSE 'COD'
                END) = ?
            """
            # Append the selected payment status to params
            params.append(payment_mode)

        if self.filterpstatus_2.currentText() != "Any":
            query += " AND payment_status = ?"
            params.append(self.filterpstatus_2.currentText())
        
        # Processing Status Filter
        if self.filterfstatus_2.currentText() != "Any":
            query += " AND processing_status = ?"
            params.append(self.filterfstatus_2.currentText())

        # Date Range Filter
        if self.date_2.isChecked():
            from_date = self.fromdate_2.date().toString("yyyy-MM-dd")
            to_date = self.todate_2.date().toString("yyyy-MM-dd")
            query += " AND order_date BETWEEN ? AND ?"
            params.extend([from_date, to_date])

        # Product or Order ID Filter
        if self.filterproduct_2.text().strip():
            query += " AND (Orders.order_id LIKE ? OR OrderDetails.prod_id LIKE ?)"
            product_filter = f"%{self.filterproduct_2.text().strip()}%"
            params.extend([product_filter, product_filter])

        # Search (Customer details, etc.)
        if self.search.text().strip():
            search_filter = f"%{self.search.text().strip()}%"
            query += """
            AND (firstname LIKE ? OR lastname LIKE ? OR email LIKE ? OR phone LIKE ? OR address LIKE ?)
            """
            params.extend([search_filter] * 5)

        # print("Executing query:", query)
        # print("With parameters:", params)



        try:
            conn = pyodbc.connect(self.conn_string)
            cursor = conn.cursor()
            cursor.execute(query, params)
            filtered_orders = cursor.fetchall()
        
            # Populate filtered orders
            self.populate_orders(filtered_orders)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to apply filters: {str(e)}")

    def populate_orders(self, orders):
        """
        Populate the QListWidget with dynamically created widgets for each order,
        including product details and total costs.
        """
        # Clear existing items in the list widget
        self.orderListWidget.clear()

        for order in orders:
            # Order details
            order_id, order_date, payment_status, processing_status, firstname, lastname, email, phone, address, city = order

            # Query to fetch product details for this specific order_id
            product_query = """
            SELECT 
                Product.name, 
                Product.price, 
                OrderDetails.quantity, 
                (Product.price * OrderDetails.quantity) AS total_product_cost
            FROM 
                OrderDetails
            JOIN 
                Product ON OrderDetails.prod_id = Product.prod_id
            WHERE 
                OrderDetails.order_id = ?
            """
            
            try:
                conn = pyodbc.connect(self.conn_string)
                cursor = conn.cursor()
                cursor.execute(product_query, order_id)
                products = cursor.fetchall()
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to load product details for Order #{order_id}: {str(e)}")
                return

            # Concatenate product details into a string
            product_details_text = "<b>Products:</b><br>"
            total_order_cost = 0
            for product in products:
                product_name, product_price, quantity, total_product_cost = product
                total_order_cost += total_product_cost
                product_details_text += f"- {product_name} | Price: {product_price} | Qty: {quantity} | Total: {total_product_cost}<br>"

            # Add delivery cost if applicable
            delivery_cost = 0
            try:
                delivery_query = """
                SELECT DeliveryCharges.cost
                FROM DeliveryCharges
                JOIN Address ON Address.city = DeliveryCharges.city
                JOIN CustomerAddress ON CustomerAddress.address_id = Address.address_id
                WHERE CustomerAddress.customer_id = (
                    SELECT customer_id FROM Orders WHERE order_id = ?
                )
                """
                cursor.execute(delivery_query, order_id)
                delivery_cost = cursor.fetchone()[0]
            except Exception as e:
                pass  # If delivery cost is not applicable, skip silently

            total_order_cost += delivery_cost

            # Main container widget
            container = QWidget()
            container_layout = QVBoxLayout()
            container.setLayout(container_layout)

            # Header (Order ID and Date)
            header = QLabel(f"<b>Order #{order_id}</b> - {order_date}")
            container_layout.addWidget(header)

            # Customer and Product Details
            details = QLabel(
                f"<b>Customer:</b> {firstname} {lastname}<br>"
                f"<b>Email:</b> {email}<br>"
                f"<b>Phone:</b> {phone}<br>"
                f"<b>Address:</b> {address}, {city}<br><br>"
                f"{product_details_text}<br>"
                f"<b>Delivery Cost:</b> {delivery_cost}<br>"
                f"<b>Total Cost:</b> {total_order_cost}"
            )
            details.setWordWrap(True)
            container_layout.addWidget(details)

            # Controls section
            controls_layout = QHBoxLayout()

            # Checkbox
            checkbox = QCheckBox("Select")
            controls_layout.addWidget(checkbox)

            # Payment status combo box
            payment_combo = QComboBox()
            payment_combo.addItems(["Awaiting Payment", "paid", "Cancelled", "Refunded"])
            payment_combo.setCurrentText(payment_status)
            controls_layout.addWidget(payment_combo)

            # Processing status combo box
            processing_combo = QComboBox()
            processing_combo.addItems(["Awaiting Processing", "Processing", "Shipped", "delivered"])
            processing_combo.setCurrentText(processing_status)
            controls_layout.addWidget(processing_combo)

            # Print button
            print_button = QPushButton("Print")
            controls_layout.addWidget(print_button)

            # Update button
            update_button = QPushButton("Update")
            controls_layout.addWidget(update_button)

            # Add the controls layout to the container
            container_layout.addLayout(controls_layout)

            # Style the container for differentiation
            container.setStyleSheet("border: 1px solid gray; padding: 10px; margin-bottom: 10px;")

            # Add the container to the QListWidget
            item = QListWidgetItem(self.orderListWidget)
            item.setSizeHint(container.sizeHint())  # Adjust size of the list item to fit the widget
            self.orderListWidget.addItem(item)
            self.orderListWidget.setItemWidget(item, container)

            # Connect signals for the buttons
            print_button.clicked.connect(lambda checked, oid=order_id: self.print_order(oid))
            update_button.clicked.connect(lambda checked, oid=order_id, pc=payment_combo, prc=processing_combo: self.update_order(oid, pc, prc))

    def print_order(self, order_id):
        """
        Handle the print button click event.
        """
        print(f"Print button clicked for Order #{order_id}")

    def update_order(self, order_id, payment_combo, processing_combo):
        """
        Handle the update button click event.
        """
        payment_status = payment_combo.currentText()
        processing_status = processing_combo.currentText()
        print(f"Update button clicked for Order #{order_id}")
        print(f"Updated Payment Status: {payment_status}")
        print(f"Updated Processing Status: {processing_status}")
        try:
            # Connect to the database
            conn = pyodbc.connect(self.conn_string)  # Replace with your actual connection string
            cursor = conn.cursor()

            # Prepare the update query
            update_query = """
            UPDATE Orders
            SET payment_status = ?, processing_status = ?
            WHERE order_id = ?
            """

            # Execute the query with the new values
            cursor.execute(update_query, payment_status, processing_status, order_id)
            conn.commit()

            # Provide feedback to the user
            QtWidgets.QMessageBox.information(self, "Success", f"Order #{order_id} updated successfully.")


        except Exception as e:
            # Handle errors and display a message to the user
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to update order: {str(e)}")

        finally:
            # Ensure the database connection is closed
            if 'conn' in locals():
                conn.close()
    def show_report_screen(self):
        # Create an instance of the report screen and show it
        self.report_screen = ReportScreen()
        self.report_screen.show()
    
    def showproducts(self):
        """
        Show the Products Screen and populate the existing listWidget.
        """
        self.products_screen = ProductsScreen()
        self.products_screen.show()

        # Clear the listWidget to avoid duplication
        self.products_screen.listWidget.clear()

        # Fetch grouped product data
        products = self.fetch_and_group_products()

        # Populate the listWidget with product details
        for prefix, product in products.items():
            self.add_product_to_list(product)

        self.products_screen.searchprod.textChanged.connect(self.filter_products)

    def filter_products(self):
        """
        Run a query to filter products based on the search query.
        """
        # Get search input
        search_query = self.products_screen.searchprod.text().strip()

        # Prepare the SQL query with LIKE for name, category, ID, and description
        query = """
        SELECT prod_id, name, price, category, description, photo_path
        FROM Product
        WHERE name LIKE ?
        OR category LIKE ?
        OR prod_id LIKE ?
        OR description LIKE ?
        """
        params = [f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"]

        # Execute the query
        try:
            conn = pyodbc.connect(self.conn_string)
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to filter products: {str(e)}")
            return

        # Clear the existing listWidget
        self.products_screen.listWidget.clear()

        # Populate the listWidget with the query results
        for row in rows:
            product = {
                "prod_id": row[0],
                "name": row[1],
                "price": row[2],
                "category": row[3],
                "description": row[4],
                "photopath": row[5]
            }
            self.add_product_to_list(product)



    def fetch_and_group_products(self):
        """
        Fetch product data and group by product ID prefix.
        """
        query = """
        SELECT prod_id, name, price, category, description, photo_path
        FROM Product
        """
        try:
            conn = pyodbc.connect(self.conn_string)
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to fetch products: {str(e)}")
            return {}

        # Group products by prefix and calculate options
        grouped_products = defaultdict(list)
        for row in rows:
            prod_id, name, price, category, description, photopath = row
            prefix = prod_id.split('_')[0]  # Extract prefix (e.g., P1, P10)
            color = prod_id.split('_')[1]   # Extract color part
            grouped_products[prefix].append({
                "prod_id": prod_id,
                "name": name,
                "price": price,
                "category": category,
                "description": description,
                "photopath": photopath,
                "color": color
            })

        # Choose one product per prefix and calculate options
        processed_products = {}
        for prefix, items in grouped_products.items():
            first_item = items[0]  # Choose the first item as the main product
            options_count = len(items)  # Count the number of variations
            first_item['options'] = f"{options_count} Options"
            processed_products[prefix] = first_item

        return processed_products

    def add_product_to_list(self, product):
        """
        Add a single product to the existing listWidget.
        :param product: Dictionary containing product details.
        """
        # Unpack product details
        prod_id = product.get("prod_id")
        name = product.get("name")
        price = product.get("price")
        category = product.get("category")
        description = product.get("description")
        options = product.get("options")
        photopath = product.get("photopath")

        # Create a container widget for product details
        product_widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()

        # Product Image
        image_label = QtWidgets.QLabel()
        image_label.setFixedSize(100, 100)
        if photopath and os.path.exists(photopath):
            image_label.setPixmap(QtGui.QPixmap(photopath).scaled(100, 100, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        else:
            image_label.setText("No Image")
            image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Product Details
        details_layout = QtWidgets.QVBoxLayout()
        name_label = QtWidgets.QLabel(f"<b>{name}</b>")
        price_label = QtWidgets.QLabel(f"Price: {price} Rs")
        category_label = QtWidgets.QLabel(f"Category: {category}")
        options_label = QtWidgets.QLabel(f"Options: {options}")
        description_label = QtWidgets.QLabel(f"{description}")

        details_layout.addWidget(name_label)
        details_layout.addWidget(price_label)
        details_layout.addWidget(category_label)
        details_layout.addWidget(options_label)
        details_layout.addWidget(description_label)

        # Edit Button
        edit_button = QtWidgets.QPushButton("Edit Product")
        edit_button.clicked.connect(lambda: self.showeditproducts(prod_id))

        # Add everything to the layout
        layout.addWidget(image_label)
        layout.addLayout(details_layout)
        layout.addWidget(edit_button)

        product_widget.setLayout(layout)

        # Add the widget to the existing listWidget
        list_item = QtWidgets.QListWidgetItem(self.products_screen.listWidget)
        list_item.setSizeHint(product_widget.sizeHint())  # Set the item's size
        self.products_screen.listWidget.addItem(list_item)
        self.products_screen.listWidget.setItemWidget(list_item, product_widget)


    def showeditproducts(self, prod_id):
        # Create an instance of the edit products screen and show it
        if prod_id:
            print(f"Editing product with ID: {prod_id}")  # Debugging statement
        self.editproducts_screen = EditProductsScreen(prod_id)
        self.conn_string = "Driver={SQL Server};Server=SF\MYSQLSERVER1;Database=safatique;Trusted_Connection=True;"
        self.editproducts_screen.show()
    
    def showEditRawMats(self):
        self.editRawMats_screen = EditRawMatsScreen()
        self.editRawMats_screen.show()

class EditProductsScreen(QtWidgets.QMainWindow):
    def __init__(self, prod_id):
        # Call the inherited classes __init__ method
        super(EditProductsScreen, self).__init__()
        # Load the .ui file
        uic.loadUi('projectScreen2.ui', self)
        self.conn_string = "Driver={SQL Server};Server=SF\MYSQLSERVER1;Database=safatique;Trusted_Connection=True;"
        self.product_id = prod_id
        self.base_price = 0
        self.variants = []

        # Load product details
        self.load_product_details()

        # Connect buttons
        self.addvariant.clicked.connect(self.add_variant)
        self.save.clicked.connect(self.save_changes)
        self.cancel.clicked.connect(self.close)
        self.addphotopushButton.clicked.connect(self.add_photo)

    def load_product_details(self):
        """
        Load product details and variants from the database.
        """
        try:
            uic.loadUi('projectScreen2.ui', self)
            conn = pyodbc.connect(self.conn_string)
            cursor = conn.cursor()

            # Fetch product details
            query = """
            SELECT name, prod_id, price, category, description, photo_path 
            FROM Product WHERE prod_id LIKE ?
            """
            cursor.execute(query, [self.product_id + '%'])
            rows = cursor.fetchall()
            

            # Set base product details (minimum price)
            main_product = min(rows, key=lambda x: x[2])  # Find the product with the minimum price
            print(main_product)
            self.base_price = main_product[2]
            self.newname.setText(main_product[0])
            self.prod_id.setText(main_product[1].split('_')[0])
            self.baseprice.setText(str(self.base_price))
            self.prodtypecomboBox.setCurrentText(main_product[3])
            self.description.setPlainText(main_product[4])
            self.currentname.setText(f"{main_product[0]}")  # Display current name

            # Load variants
            self.variants = rows
            self.display_variants()

            conn.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load product: {str(e)}")

    def display_variants(self):
        """
        Display all variants in the QListWidget.
        """
        self.variantsdisplay.clear()
        for variant in self.variants:
            prod_code = variant[1]
            color = prod_code.split('_')[1] if '_' in prod_code else 'N/A'
            price_diff = int(variant[2]) - self.base_price
            item_text = f"Color: {color}, Extra Cost: +{price_diff}"
            list_item = QtWidgets.QListWidgetItem(item_text)

            # Add a Remove button
            remove_button = QtWidgets.QPushButton("Remove")
            remove_button.clicked.connect(lambda _, code=prod_code: self.remove_variant(code))

            # Set widget in QListWidget
            widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout()
            layout.addWidget(QtWidgets.QLabel(item_text))
            layout.addWidget(remove_button)
            widget.setLayout(layout)

            self.variantsdisplay.addItem(list_item)
            self.variantsdisplay.setItemWidget(list_item, widget)

    def add_variant(self):
        """
        Add a new variant to the QListWidget and variants list.
        """
        color = self.variantname.text().strip()
        cost_modifier = self.variantcost.text().strip()

        if not color or not cost_modifier.isdigit():
            QtWidgets.QMessageBox.warning(self, "Input Error", "Enter valid color and cost modifier.")
            return

        # Add variant entry
        new_prod_code = f"{self.prod_id.text()}_{color}"
        new_price = self.base_price + int(cost_modifier)
        self.variants.append((self.newname.text(), new_prod_code, new_price, "", ""))

        self.display_variants()
        self.variantname.clear()
        self.variantcost.clear()

    def remove_variant(self, prod_code):
        """
        Remove a variant from the variants list.
        """
        self.variants = [v for v in self.variants if v[1] != prod_code]
        self.display_variants()

    def add_photo(self):
        """
        Select and update photo path.
        """
        photo_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Photo", "", "Images (*.png *.jpg *.jpeg)")
        if photo_path:
            print(f"Selected photo: {photo_path}")
            self.photopath = photo_path
            self.currentname.setText("Photo updated successfully!")

    def save_changes(self):
        """
        Save changes to the database.
        """
        try:
            conn = pyodbc.connect(self.conn_string)
            cursor = conn.cursor()

            # Update main product details
            cursor.execute("""
                UPDATE Product SET name=?, price=?, category=?, description=?, photo_path=?
                WHERE prod_id LIKE ?
            """, [
                self.newname.text(), self.baseprice.text(),
                self.prodtypecomboBox.currentText(), self.description.toPlainText(), 
                self.photopath, self.prod_id.text() + '%'
            ])

            # Delete existing variants and add new ones
            cursor.execute("DELETE FROM Products WHERE prod_id LIKE ?", [self.prod_id.text() + '%'])
            for variant in self.variants:
                cursor.execute("""
                    INSERT INTO Product (name, prod_id, price, category, description, photo_path)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, variant)

            conn.commit()
            conn.close()
            QtWidgets.QMessageBox.information(self, "Success", "Product saved successfully!")
            self.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to save changes: {str(e)}")

class EditRawMatsScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(EditRawMatsScreen, self).__init__()
        # Load the .ui file for the screen
        uic.loadUi('editRawMats1.ui', self)
        
        # Populate the table when screen loads
        self.populate_table()

        # Connect the edit button to the function
        self.editbutton.clicked.connect(self.show_edit_dialog)
        self.addbutton.clicked.connect(self.addrawmat)

        # Close button functionality
        self.closebutton.clicked.connect(self.close)
    def populate_table(self):
        conn_string = "Driver={SQL Server};Server=SF\MYSQLSERVER1;Database=safatique;Trusted_Connection=True;"
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM RawMaterial")
            rows = cursor.fetchall()

            # Set the row and column count based on query results
            self.RawMatsTable.setRowCount(len(rows))
            self.RawMatsTable.setColumnCount(len(cursor.description))

            # Set column headers
            for col_idx, column in enumerate(cursor.description):
                self.RawMatsTable.setHorizontalHeaderItem(col_idx, QTableWidgetItem(column[0]))

            # Populate the table with data
            for row_idx, row in enumerate(rows):
                for col_idx, data in enumerate(row):
                    self.RawMatsTable.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

            self.RawMatsTable.resizeColumnsToContents()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to load data: {str(e)}")


    def show_edit_dialog(self):
        # Get the selected row from the table
        selected_row = self.RawMatsTable.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a row to edit.")
            return

        # Get the column to edit (e.g., name)
        column_index = self.RawMatsTable.currentColumn()
        old_value = self.RawMatsTable.item(selected_row, column_index).text()

        # Check if the column is not 'mat_id' (since 'mat_id' is assumed to be non-editable)
        if column_index == 0:
            QMessageBox.warning(self, "Invalid Edit", "You cannot edit the mat_id column.")
            return

        # Ask for the new value using QInputDialog
        new_value, ok = QInputDialog.getText(self, "Edit Value", f"Enter new value for {self.RawMatsTable.horizontalHeaderItem(column_index).text()}:",
                                            text=old_value)

        if ok and new_value.strip() != "":
            # Update the table locally
            self.RawMatsTable.setItem(selected_row, column_index, QTableWidgetItem(new_value))

            # Update the database
            self.update_database(selected_row, column_index, new_value)

    def addrawmat(self):
        """
        Prompt the user for raw material details and add them to the database and table.
        """
        # Ask for raw material name
        name, ok_name = QInputDialog.getText(self, "Add Raw Material", "Enter raw material name:")
        if not ok_name or not name.strip():
            QMessageBox.warning(self, "Invalid Input", "Name cannot be empty.")
            return

        # Ask for raw material type
        mat_type, ok_type = QInputDialog.getText(self, "Add Raw Material", "Enter raw material type:")
        if not ok_type or not mat_type.strip():
            QMessageBox.warning(self, "Invalid Input", "Type cannot be empty.")
            return

        # Ask for raw material quantity
        quantity, ok_quantity = QInputDialog.getInt(self, "Add Raw Material", "Enter quantity:")
        if not ok_quantity or quantity <= 0:
            QMessageBox.warning(self, "Invalid Input", "Quantity must be a positive number.")
            return

        # Ask for raw material cost
        cost, ok_cost = QInputDialog.getDouble(self, "Add Raw Material", "Enter cost:", decimals=2)
        if not ok_cost or cost <= 0:
            QMessageBox.warning(self, "Invalid Input", "Cost must be a positive number.")
            return

        # Connect to the database and insert the new raw material
        conn_string = "Driver={SQL Server};Server=SF\MYSQLSERVER1;Database=safatique;Trusted_Connection=True;"
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()

            # Insert into database
            insert_query = """
                INSERT INTO RawMaterial (name, type, quantity, cost)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(insert_query, name, mat_type, quantity, cost)
            conn.commit()

            # Update the table widget
            self.populate_table()

            QMessageBox.information(self, "Success", "Raw material added successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to add raw material: {str(e)}")

            

    def update_database(self, row, col, new_value):
        """
        Update the selected row's value in the database.
        """
        # Get the primary key for the selected row (assume mat_id is in column 0)
        mat_id = self.RawMatsTable.item(row, 0).text()

        # Get the column name from the table header
        column_name = self.RawMatsTable.horizontalHeaderItem(col).text()

        # Connect to the database
        conn_string = "Driver={SQL Server};Server=SF\MYSQLSERVER1;Database=safatique;Trusted_Connection=True;"
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()

            # Update the database with the new value
            update_query = f"""
                UPDATE RawMaterial
                SET {column_name} = ?
                WHERE mat_id = ?
            """
            cursor.execute(update_query, new_value, mat_id)
            conn.commit()

            QMessageBox.information(self, "Success", f"{column_name} updated successfully.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to update database: {str(e)}")
        


class ProductsScreen(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(ProductsScreen, self).__init__()
        # Load the .ui file
        uic.loadUi('projectScreen1.ui', self)

class ReportScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(ReportScreen, self).__init__()
        # Load the report .ui file
        uic.loadUi('Database_project_report_screen.ui', self)
        self.generatepdf.clicked.connect(self.generate_pdf)

    def extract_data(self):
        """
        Extract data from the QTextBrowser widgets dynamically.
        """
        data = {
            "Visitors": self.findChild(QtWidgets.QTextBrowser, "visitors").toPlainText(),
            "Product Views": self.findChild(QtWidgets.QTextBrowser, "productviews").toPlainText(),
            "Orders Received": self.findChild(QtWidgets.QTextBrowser, "ordersreceived").toPlainText(),
            "Revenue": self.findChild(QtWidgets.QTextBrowser, "revenue").toPlainText(),
            "Visitors with Product Views": self.findChild(QtWidgets.QTextBrowser, "visitorsprodviews").toPlainText(),
            "Added to Cart": self.findChild(QtWidgets.QTextBrowser, "addedtocart").toPlainText()
        }
        return data

    def generate_pdf(self):
        """
        Generate a PDF containing all the data displayed in the report screen.
        """
        # Extract the data
        data = self.extract_data()
        
        # Create a PDF file
        pdf_filename = "Report.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=A4)
        width, height = A4  # A4 page dimensions

        # Add Title
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width / 2.0, height - 50, "Report Summary")

        # Add Report Data
        c.setFont("Helvetica", 12)
        y = height - 100  # Starting y position

        for key, value in data.items():
            c.drawString(50, y, f"{key}: {value}")
            y -= 20  # Move to the next line
        
        # Save the PDF
        c.save()
        QtWidgets.QMessageBox.information(self, "PDF Generated", f"Report has been saved as {pdf_filename}")


# Initialize and display the app
app = QtWidgets.QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
