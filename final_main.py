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
from PyQt6.QtWidgets import QListWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QPushButton, QCheckBox
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QGridLayout, QScrollArea, QDialog, QTableWidget
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt
import pyodbc

customerID = ''
addressID = ''
usernameCustomer = ''


class Homepage(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Homepage, self).__init__()
        # Load the .ui file
        uic.loadUi('homepage.ui', self)
        # Show the GUI
        self.show()
        self.setWindowTitle("Safatique")
        # Set fixed size for the window
        self.setFixedSize(self.size())
        self.pushButton_shopNow.clicked.connect(self.show_login_screen)
        
    def show_login_screen(self):
        self.login_screen = LoginScreen(self)
        self.close()
        self.login_screen.show()

class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.parent = parent
        uic.loadUi('login screen.ui', self)
        self.setWindowTitle("Login")
        self.setFixedSize(self.size())
        self.pushButton_signup.clicked.connect(self.show_signup_screen)
        self.pushButton_login.clicked.connect(self.validate_login) #change this to validate_login
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        # self.pushButton_close.clicked.connect(self.close)
        
    def show_signup_screen(self):
        self.signup_screen = SignupScreen(self)
        # self.hide()
        self.signup_screen.show()
        
    def validate_login(self):
        # Get the username and password entered by the user
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        conn_string = "Driver={SQL Server};Server=SHAAFPC\DBSQLSERVER;Database=safatique;Trusted_Connection=True;"
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()
            query = "SELECT * FROM [User] WHERE username = ? AND [password] = ?" 
            cursor.execute(query, (username, password))
            result = cursor.fetchall()
            # print(result)
            cursor.close()
            conn.close()
            
            if len(result) > 0 and result[0][2] == 'customer':
                self.show_catalogue_screen()  # Open the next screen if login is successful
                self.lineEdit_username.clear()
                self.lineEdit_password.clear()
            elif len(result) > 0 and result[0][2] == 'admin':
                pass
                self.show_admin_screen()
            else:
                self.msg = QtWidgets.QMessageBox()
                self.msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                self.msg.setText("Invalid username or password. Please try again.")
                self.msg.setWindowTitle("Login Failed")
                self.msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                self.msg.exec()
                self.lineEdit_username.clear()
                self.lineEdit_password.clear()
                
        except pyodbc.Error as e:
            print(f"Database error: {e}")
            return False
    # this event box will ignore close command to stop the login screen from closing as well, so there is no option but to login
    def closeEvent(self, event):
        # print("Closing login screen")
        # if self.parent:
        #     self.parent.show()
        event.ignore()
        
    def show_catalogue_screen(self):
        self.catalogue_screen = CatalogueScreen(self)
        # self.hide()
        self.catalogue_screen.show()
        
    def show_admin_screen(self):
        self.admin_screen = UI()
        self.hide()
        self.admin_screen.show()

# class PersistentMessageBox(QtWidgets.QMessageBox):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def done(self, result):
#         # Prevent the message box from closing
#         if result == QtWidgets.QMessageBox.StandardButton.Ok:
#             return  # Ignore the "OK" button
#         super().done(result)  # Allow other buttons to work normally
        
#     def close_message_box(self):
#         if self.msg:
#             self.msg.close()

class SignupScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SignupScreen, self).__init__(parent)
        self.parent = parent
        uic.loadUi('signupscreen.ui', self)
        self.setWindowTitle("Sign Up")
        self.setFixedSize(self.size())
        self.pushButton_signup.clicked.connect(self.validate_signup)
        
    def validate_signup(self):
        firstName = self.lineEdit_firstName.text()
        lastName = self.lineEdit_lastName.text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        repassword = self.lineEdit_repassword.text()
        email = self.lineEdit_email.text()
        phone = self.lineEdit_phone.text()
        address = self.lineEdit_address.text()
        city = self.lineEdit_city.text()

        if not firstName or not lastName or not email or not phone or not username or not password or not repassword or not address or not city:
            self.show_popup("All fields are required.")
        elif len(username) > 10:
            self.show_popup("Username cannot be more than 10 characters long.")
        elif len(password) > 16:
            self.show_popup("Password cannot be more than 16 characters long.")
        elif len(phone) != 10 or not phone.isdigit():
            self.show_popup("Phone number must be 10 digits long and numeric.")
        elif password != repassword:
            self.show_popup("Passwords do not match.")
        else:
            conn_string = "Driver={SQL Server};Server=SHAAFPC\DBSQLSERVER;Database=safatique;Trusted_Connection=True;"
            conn = None
            cursor = None
            try:
                conn = pyodbc.connect(conn_string, autocommit=False)  # Disable autocommit for transaction handling
                cursor = conn.cursor()

                # Check if username already exists
                # cursor.execute("BEGIN TRANSACTION") # DO NOT PUT THIS SINCE THE LOGIC ALREADY HANDLES ROLLBACK
                query = "SELECT username FROM [User] WHERE username = ?"
                cursor.execute(query, (username))
                result = cursor.fetchall()
                if len(result) > 0:
                    self.show_popup("Username already exists. Please choose another username.")
                else:
                    # Insert into User table
                    query1 = "INSERT INTO [User] (username, [password], [role]) VALUES (?, ?, ?)"
                    cursor.execute(query1, (username, password, 'customer'))
                    # print("User inserted successfully")

                    # Insert into Customer table
                    query2 = "INSERT INTO Customer (firstname, lastname, email, phone) VALUES (?, ?, ?, ?);"
                    cursor.execute(query2, (firstName, lastName, email, phone))
                    # print("Customer inserted successfully")
                    
                    # Insert into UserCustomer table
                    query3 = "SELECT customer_id FROM Customer WHERE firstname = ? and lastname = ? and email = ? and phone = ?;"
                    cursor.execute(query3, (firstName, lastName, email, phone))
                    customer_id = cursor.fetchall()
                    # print("customer_id: ", customer_id)
                    query4 = "INSERT INTO UserCustomer (username, customer_id) VALUES (?, ?);"
                    cursor.execute(query4, (username, int(customer_id[0][0])))
                    # print("UserCustomer inserted successfully")
                    
                    # insert into Address table
                    query5 = "INSERT INTO [Address] (address, city) VALUES (?, ?);"
                    cursor.execute(query5, (address, city))
                    # print("Address inserted successfully")
                    
                    # insert into CustomerAddress table
                    query6 = "SELECT address_id FROM [Address] WHERE address = ? and city = ?;"
                    cursor.execute(query6, (address, city))
                    address_id = cursor.fetchall()
                    # print("address_id: ", address_id)
                    query7 = "INSERT INTO CustomerAddress (customer_id, address_id) VALUES (?, ?);"
                    cursor.execute(query7, (int(customer_id[0][0]), int(address_id[0][0])))
                    # print("CustomerAddress inserted successfully")

                    # Commit the transaction
                    conn.commit()
                    self.show_popup("Sign up successful. Please log in to continue.")
                    self.close()
                    # print("signup screen closed")
            except pyodbc.Error as e:
                if conn:
                    conn.rollback()  # Rollback transaction in case of any error
                self.show_popup("Database error: " + str(e))
                # print(f"Database error: {e}")
            except Exception as e:
                if conn:
                    conn.rollback()  # Rollback transaction in case of unexpected errors
                self.show_popup("An unexpected error occurred: " + str(e))
                print(f"Unexpected error: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()

    def show_popup(self, message):
        popup = QtWidgets.QMessageBox(self)
        popup.setIcon(QtWidgets.QMessageBox.Icon.Information)
        popup.setText(message)
        popup.setWindowTitle("Sign Up")
        popup.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        popup.exec()
        
    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()
        
class CatalogueScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        try:
            uic.loadUi('testCatalogue.ui', self)  # Load UI file
            self.logoLabel.setScaledContents(False) # Ensure the logo scales appropriately

            self.scrollArea.setWidgetResizable(True)  # Configure scroll area for products
            self.scrollAreaWidgetContents = QWidget()
            self.productGridLayout = QGridLayout(self.scrollAreaWidgetContents)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            # Set the window to be non-resizable and adjust to content
            self.setFixedSize(1290, 720)

            # Connect UI elements
            # self.pushButton_applyFilters.clicked.connect(self.apply_filters)
            self.pushButton_viewCart.clicked.connect(self.show_cart_screen)
            self.searchLineEdit.textChanged.connect(self.apply_filters)
            self.categoryComboBox.currentIndexChanged.connect(self.apply_filters)
            self.pushButton_logOut.clicked.connect(self.close)

            self.populate_products() # Populate products initially
            self.load_categories()  # Load categories from the database
            
        except Exception as e:
            print(f"Error during initialization: {e}")

    def query_products(self, filters=None):
        conn_string = "Driver={SQL Server};Server=SHAAFPC\DBSQLSERVER;Database=safatique;Trusted_Connection=True;"
        products = []

        try:
            # Establish connection
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()

            # Base query
            query = "SELECT prod_id, name, price, category, description, photo_path FROM [product]"
            conditions = []  # List to hold WHERE conditions
            params = []  # List to hold parameter values for placeholders

            # Apply category filter (excluding "All Categories")
            if filters and filters.get("category") and filters["category"] != "All Categories":
                conditions.append("category = ?")
                params.append(filters["category"])

            # Apply keyword filter for product name or description
            if filters and filters.get("keyword"):
                conditions.append("(name LIKE ? OR description LIKE ?)")
                keyword = f"%{filters['keyword']}%"
                params.extend([keyword, keyword])

            # Add WHERE clause if there are conditions
            if conditions:
                query += " WHERE " + " AND ".join(conditions)

            # print("Final query:", query)  # Debug: print the query
            # print("Parameters:", params)  # Debug: print the parameters

            # Execute query with parameters
            cursor.execute(query, params)

            # Fetch and parse results
            rows = cursor.fetchall()
            for row in rows:
                products.append({
                    "prod_id": row.prod_id,
                    "name": row.name,
                    "price": row.price,
                    "category": row.category,
                    "description": row.description,
                    "photo_path": row.photo_path
                })

            # Close cursor and connection
            cursor.close()
            conn.close()
        except pyodbc.Error as e:
            print(f"Database error: {e}")

        return products


    def populate_products(self, filters=None):
        # Clear existing products
        for i in reversed(range(self.productGridLayout.count())):
            widget = self.productGridLayout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Query products (you can add filters here if needed)
        products = self.query_products(filters)

        # Add products to grid
        row, col = 0, 0
        for product in products:
            # Product container
            product_widget = QWidget()
            product_layout = QVBoxLayout()

            # Image
            image_label = QLabel()
            image_label.setFixedSize(150, 150)  # Ensure uniform image size
            pixmap = QPixmap(product["photo_path"])
            # print(product["photo_path"])
            image_label.setPixmap(pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_label.mousePressEvent = lambda _, p=product: self.open_product_view(p)
            product_layout.addWidget(image_label)
            # print("error check")
            # Title (clickable)
            title_label = QLabel(product["name"])
            title_label.setStyleSheet("font-weight: bold; text-align: center;")
            title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            title_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
            title_label.mousePressEvent = lambda _, p=product: self.open_product_view(p)
            title_label.mousePressEvent = lambda event, p=product: self.open_product_view(p)
            product_layout.addWidget(title_label)
            # Price
            price_label = QLabel(str(product["price"]))
            price_label.setStyleSheet("color: green; text-align: center;")
            price_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            product_layout.addWidget(price_label)

            # Set layout and styling
            product_widget.setLayout(product_layout)
            product_widget.setCursor(Qt.CursorShape.PointingHandCursor)

            # Add to grid
            self.productGridLayout.addWidget(product_widget, row, col)

            # print("error check")
            col += 1
            if col == 3:  # Move to next row after 3 columns
                col = 0
                row += 1

        # Fill empty cells if there are fewer than 7 products
        total_columns = 3
        while row * total_columns + col < 7:
            spacer_widget = QWidget()  # Empty widget to fill space
            self.productGridLayout.addWidget(spacer_widget, row, col)
            col += 1
            if col == 3:
                col = 0
                row += 1

    def apply_filters(self):
        # Get selected category and current search keyword
        category = self.categoryComboBox.currentText()
        keyword = self.searchLineEdit.text().strip()  # Get text from the search field

        # Prepare filters dictionary
        filters = {}
        if category and category != "All Categories":
            filters["category"] = category
        if keyword:
            filters["keyword"] = keyword

        # print(f"Applying filters: {filters}")  # Debugging

        # Refresh the product grid with the applied filters
        self.populate_products(filters)

    def load_categories(self):
        conn_string = "Driver={SQL Server};Server=SHAAFPC\DBSQLSERVER;Database=safatique;Trusted_Connection=True;"
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()

            # Query to fetch unique categories
            query = "SELECT DISTINCT category FROM [product]"
            cursor.execute(query)

            # Add categories to the ComboBox
            self.categoryComboBox.addItem("All Categories")  # Default option
            for row in cursor.fetchall():
                self.categoryComboBox.addItem(row.category)

            cursor.close()
            conn.close()
        except pyodbc.Error as e:
            print(f"Database error: {e}")


    def open_product_view(self, product):
        self.products_screen = ProductsScreen(self, product)
        self.hide()
        self.products_screen.show()
        
    def show_cart_screen(self):
        self.cart_screen = CartScreen(self)
        self.hide()
        self.cart_screen.show()
        
    def show_productCategory_screen(self):
        self.product_category_screen = ProductCategoryScreen(self)
        self.hide()
        self.product_category_screen.show()
        
class ProductCategoryScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ProductCategoryScreen, self).__init__(parent)
        self.parent = parent
        uic.loadUi('productCategory.ui', self)
        self.setWindowTitle("Product Category")
        self.setFixedSize(self.size())
        self.pushButton_viewProduct.clicked.connect(self.show_products_screen)
        
    def show_products_screen(self):
        self.products_screen = ProductsScreen(self)
        self.hide()
        self.products_screen.show()
        
    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()


class ProductsScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None, product=None):
        super(ProductsScreen, self).__init__(parent)
        self.parent = parent
        self.product = product
        uic.loadUi('productpage.ui', self)
        self.setWindowTitle("Safatique Products")
        self.setFixedSize(self.size())
        self.pushButton_addToCart.clicked.connect(self.add_to_cart_and_show_cart)

        # Display the product image in the label_logo container
        if self.product:
            pixmap = QPixmap(self.product["photo_path"])
            self.label_logo.setPixmap(pixmap.scaled(self.label_logo.size(), Qt.AspectRatioMode.KeepAspectRatio))
            self.label_productName.setText(self.product["name"])
            self.label_category.setText(self.product.get("category", "N/A"))
            self.label_price.setText(str(self.product["price"])+" Rs")
            self.textBrowser_description.setText(self.product["description"])
        
    def add_to_cart_and_show_cart(self):
        # Simulate Add_to_cart placement logic
        Add_to_cart_successful = True  # Replace with actual logic for adding product to the cart

        if Add_to_cart_successful:
            self.show_popup("Added to cart successfully!")
            self.close()
        else:
            self.show_popup("Error adding to cart. Please try again.")

    def show_popup(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Add to cart")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def show_cart_screen(self):
        self.cart_screen = CartScreen(self)
        self.hide()
        self.cart_screen.show()

    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()


class CartScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CartScreen, self).__init__(parent)
        self.parent = parent
        uic.loadUi('Cart.ui', self)
        self.setWindowTitle("Cart")
        self.setFixedSize(self.size())
        self.pushButton_Checkout.clicked.connect(self.show_checkout_screen)
        
    def show_checkout_screen(self):
        self.checkout_screen = CheckoutScreen(self)
        self.hide()
        self.checkout_screen.show()
        
    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()
        self.update_cart()

    def update_cart(self):
        # Clear existing rows
        self.ProductsTableWidget.setRowCount(0)

        # Simulate fetching cart items (replace with actual logic)
        cart_items = self.get_cart_items()

        # Populate the table with cart items
        for item in cart_items:
            row_position = self.ProductsTableWidget.rowCount()
            self.ProductsTableWidget.insertRow(row_position)

            self.ProductsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(item["name"]))
            self.ProductsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(item["price"])))
            self.ProductsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(item["category"]))
            self.ProductsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(item["description"]))

    def get_cart_items(self):
        # Simulate fetching cart items from a database or other source
        # Replace this with actual logic to fetch cart items
        return [
            {"name": "Diamond Ring", "price": 1200, "category": "Jewelry", "description": "A beautiful diamond ring"},
            {"name": "Gold Necklace", "price": 900, "category": "Jewelry", "description": "A stunning gold necklace"}
        ]
        
class CheckoutScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CheckoutScreen, self).__init__(parent)
        self.parent = parent
        uic.loadUi('checkout.ui', self)
        self.setWindowTitle("Checkout")
        self.setFixedSize(self.size())
        self.pushButton_placeOrder.clicked.connect(self.show_place_order_screen)
        
    def show_place_order_screen(self):
        # Simulate order placement logic
        order_successful = True  # Replace with actual logic

        if order_successful:
            self.show_popup("Order placed successfully!")
            self.close()
        else:
            self.show_popup("Error placing order. Please try again.")

    def show_popup(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Order Status")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()
        
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__() 
        # Load the .ui file
        uic.loadUi('sales_screen.ui', self) 
        self.conn_string = "Driver={SQL Server};Server=SHAAFPC\DBSQLSERVER;Database=safatique;Trusted_Connection=True;"

        # Load data on screen load
        self.load_sales_data()
        # Connect filters to apply_filters  
        self.filterpmstatus_2.currentTextChanged.connect(self.apply_filters)
        self.filterfstatus_2.currentTextChanged.connect(self.apply_filters)
        self.date_2.stateChanged.connect(self.apply_filters)
        self.fromdate_2.dateChanged.connect(self.apply_filters)
        self.todate_2.dateChanged.connect(self.apply_filters)
        self.filterproduct_2.textChanged.connect(self.apply_filters)
        self.search.textChanged.connect(self.apply_filters)

        self.reportbutton.clicked.connect(self.show_report_screen)
        self.productsbutton.clicked.connect(self.showproducts)
        self.rawmaterial.clicked.connect(self.showEditRawMats)

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
            print("POPULATED.")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to load data: {str(e)}")

    def apply_filters(self):
        """
        Apply filters to update the displayed orders.
        """
        query = """
        SELECT distinct Orders.order_id, order_date, 
        CASE
            WHEN PaymentInfo.payment_id IS NULL THEN 'Bank Transfer'
            ELSE 'COD'
        END AS payment_status,
        processing_status, firstname, lastname, email, phone, address, city
        FROM Orders
        JOIN OrderDetails ON Orders.order_id = OrderDetails.order_id
        JOIN Customer ON Orders.customer_id = Customer.customer_id
        JOIN CustomerAddress ON Customer.customer_id = CustomerAddress.customer_id
        JOIN Address ON CustomerAddress.address_id = Address.address_id
        LEFT JOIN CustomerPaymentInfo ON Customer.customer_id = CustomerPaymentInfo.customer_id
        LEFT JOIN PaymentInfo ON CustomerPaymentInfo.payment_id = PaymentInfo.payment_id
        """
        params = []
    


        payment_status = self.filterpmstatus_2.currentText()
        # Add the condition for payment_status if it's not "Any"
        if payment_status != "Any":
            query += """
            WHERE (CASE
                    WHEN PaymentInfo.payment_id IS NULL THEN 'Bank Transfer'
                    ELSE 'COD'
                END) = ?
            """
            # Append the selected payment status to params
            params.append(payment_status)
        
        # Processing Status Filter
        if self.filterfstatus_2.currentText() != "Any":
            query += " AND processing_status = ?"
            params.append(self.filterfstatus_2.currentText())

        # Date Range Filter
        if self.date_2.isChecked():
            from_date = self.fromdate.date().toString("yyyy-MM-dd")
            to_date = self.todate.date().toString("yyyy-MM-dd")
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
        # Create an instance of the products screen and show it
        self.products_screen = ProductsScreen()
        self.products_screen.show()

        self.products_screen.edit1.clicked.connect(self.showeditproducts)

    def showeditproducts(self):
        # Create an instance of the edit products screen and show it
        self.editproducts_screen = EditProductsScreen()
        self.editproducts_screen.show()
    
    def showEditRawMats(self):
        self.editRawMats_screen = EditRawMatsScreen()
        self.editRawMats_screen.show()

class EditProductsScreen(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(EditProductsScreen, self).__init__()
        # Load the .ui file
        uic.loadUi('projectScreen2.ui', self)

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
        conn_string = "Driver={SQL Server};Server=SHAAFPC\DBSQLSERVER;Database=safatique;Trusted_Connection=True;"
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
        conn_string = "Driver={SQL Server};Server=SHAAFPC\DBSQLSERVER;Database=safatique;Trusted_Connection=True;"
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
        conn_string = "Driver={SQL Server};Server=SHAAFPC\DBSQLSERVER;Database=safatique;Trusted_Connection=True;"
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

if __name__ == "__main__":
    app = QApplication([])
    window = Homepage()  # Create an instance of our class
    sys.exit(app.exec())