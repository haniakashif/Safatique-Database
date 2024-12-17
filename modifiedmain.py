import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QGridLayout, QScrollArea, QDialog, QTableWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt, QDate
import pyodbc
import datetime


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
        print("login screen called and homepage closed")
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
        # self.pushButton_Quick.clicked.connect(self.quickLogin)
        # self.pushButton_close.clicked.connect(self.close)
        
    # def quickLogin(self):
    #     self.lineEdit_username.setText("Ahad001234")
    #     self.lineEdit_password.setText("Pass1234")
    #     self.validate_login()
        
    def show_signup_screen(self):
        self.signup_screen = SignupScreen(self)
        # self.hide()
        self.signup_screen.show()
        
    def closeEvent(self, event):
        print("Closing login screen ignored")
        # print("Closing login screen")
        # if self.parent:
        #     self.parent.show()
        event.ignore()
        
    def show_catalogue_screen(self):
        self.catalogue_screen = CatalogueScreen(self)
        # self.hide()
        self.catalogue_screen.show()
    
    def validate_login(self):
        # Get the username and password entered by the user
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()
            query = "SELECT * FROM [User] WHERE username = ? AND [password] = ?" 
            cursor.execute(query, (username, password))
            result = cursor.fetchall()            
            
            if len(result) > 0 and result[0][2] == 'customer':
                self.show_catalogue_screen()  # Open the next screen if login is successful
                global usernameCustomer
                usernameCustomer = username
                query = "SELECT customer_id FROM [UserCustomer] WHERE username = ?"
                cursor.execute(query, (usernameCustomer))
                result = cursor.fetchall()
                global customerID
                customerID = result[0][0]
                query = "SELECT address_id FROM [CustomerAddress] WHERE customer_id = ?"
                cursor.execute(query, (customerID))
                result = cursor.fetchall()
                global addressID
                #addressID = result[0][0]
                # print("customerID: ", customerID)
                # print("addressID: ", addressID)
                # print("usernameCustomer: ", usernameCustomer)
                self.lineEdit_username.clear()
                self.lineEdit_password.clear()
            elif len(result) > 0 and result[0][2] == 'admin':
                pass
                # self.show_admin_screen()
            else:
                self.msg = QtWidgets.QMessageBox()
                self.msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                self.msg.setText("Invalid username or password. Please try again.")
                self.msg.setWindowTitle("Login Failed")
                self.msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                self.msg.exec()
                self.lineEdit_username.clear()
                self.lineEdit_password.clear()
                
            cursor.close()
            conn.close()
        except pyodbc.Error as e:
            print(f"Database error: {e}")
            return False

class SignupScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SignupScreen, self).__init__(parent)
        self.parent = parent
        uic.loadUi('signupscreen.ui', self)
        self.setWindowTitle("Sign Up")
        self.setFixedSize(self.size())
        self.pushButton_signup.clicked.connect(self.validate_signup)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_repassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
    def show_popup(self, message):
        popup = QtWidgets.QMessageBox(self)
        popup.setIcon(QtWidgets.QMessageBox.Icon.Information)
        popup.setText(message)
        popup.setWindowTitle("Sign Up")
        popup.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        popup.exec()
        
    def closeEvent(self, event):
        print("Closing signup screen")
        if self.parent:
            self.parent.show()
        event.accept()
    
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
            conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
            conn = None
            cursor = None
            try:
                conn = pyodbc.connect(conn_string, autocommit=False)  # Disable autocommit for transaction handling
                cursor = conn.cursor()

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
                    print("closing signup screen")
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
        
class CatalogueScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        # try:
        uic.loadUi('testCatalogue.ui', self)  # Load UI file
        self.setWindowTitle("Safatique Catalogue")  # Set window title
        self.setFixedSize(1290, 720)
        self.logoLabel.setScaledContents(False) # Ensure the logo scales appropriately
        self.scrollArea.setWidgetResizable(True)  # Configure scroll area for products
        self.scrollAreaWidgetContents = QWidget()
        self.productGridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_viewCart.clicked.connect(self.show_cart_screen)
        self.searchLineEdit.textChanged.connect(self.apply_filters)
        self.categoryComboBox.currentIndexChanged.connect(self.apply_filters)
        self.pushButton_logOut.clicked.connect(self.log_out)

        self.populate_products() # Populate products initially
        self.load_categories()  
        
        # except Exception as e:
        #     print(f"Error during initialization: {e}")

    def open_product_view(self, product):
        # print("customerID: ", customerID)
        # print("addressID: ", addressID)
        # print("usernameCustomer: ", usernameCustomer)
        self.products_screen = ProductsScreen(self, product)
        self.hide()
        self.products_screen.show()
        
    def show_cart_screen(self):
        self.cart_screen = CartScreen(self)
        self.hide()
        self.cart_screen.show()
        
    def log_out(self):
        print("log out called and catalogue closed")
        print("usernameCustomer: ", usernameCustomer)
        # self.parent.show()
        self.close()
    
    def query_products(self, filters=None):
        conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
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
            price_label = QLabel(str(product["price"]) + " Rs")
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
        conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
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

class ProductsScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None, product=None):
        super(ProductsScreen, self).__init__(parent)
        self.parent = parent
        self.product = product
        uic.loadUi('productpage.ui', self)
        self.setWindowTitle("Safatique Products")
        self.setFixedSize(self.size())
        self.pushButton_addToCart.clicked.connect(self.add_to_cart_and_show_cart)
        self.spinBox_quantity.setValue(1)

        # Display the product image in the label_logo container
        if self.product:
            pixmap = QPixmap(self.product["photo_path"])
            self.label_logo.setPixmap(pixmap.scaled(self.label_logo.size(), Qt.AspectRatioMode.KeepAspectRatio))
            self.label_productName.setText(self.product["name"])
            self.label_category.setText(self.product.get("category", "N/A"))
            self.label_price.setText(str(self.product["price"]) + " Rs")
            self.textBrowser_description.setText(self.product["description"])
            
        # print("customerID: ", customerID)
        # print("addressID: ", addressID)
        # print("usernameCustomer: ", usernameCustomer)

    def show_popup(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Add to Cart")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def show_catalogue_screen(self):
        self.catalogue_screen = CatalogueScreen(self)
        self.hide()
        self.catalogue_screen.show()
    
    def add_to_cart_and_show_cart(self):
        # Get quantity from spinBox
        # print("customerID: ", customerID)
        # print("addressID: ", addressID)
        # print("usernameCustomer: ", usernameCustomer)
        quantity = self.spinBox_quantity.value()
        if quantity < 1:
            self.show_popup("Please select a valid quantity.")
            return

        # Extract product details
        product_id = self.product["prod_id"]
        product_name = self.product["name"]
        unit_price = float(self.product["price"])
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        # Database connection
        conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()

            # Step 1: Check if a cart exists for this CustomerID
            cursor.execute("Set identity_insert [Cart] on")
            cursor.execute("SELECT * FROM Cart WHERE customer_id = ?", (customerID))
            cart_result = cursor.fetchone()
            # print("cart_result: ", cart_result)

            if not cart_result:
                # Step 2: If no cart exists, create a new cart
                cursor.execute("INSERT INTO Cart (customer_id, date_created) VALUES (?, ?)", (customerID, current_date))
            else:
                # Step 3: Check if the product already exists in CartItems
                cursor.execute("""SELECT quantity FROM CartItems WHERE customer_id = ? AND prod_id = ?""", (customerID, product_id)) 
                item_result = cursor.fetchone()
                # print("item_result: ", item_result)

                if item_result:
                    # If the product already exists, update the quantity
                    existing_quantity = item_result[0]
                    print("existing_quantity: ", existing_quantity)
                    new_quantity = existing_quantity + quantity
                    cursor.execute("""UPDATE CartItems SET quantity = ?, unit_price = ? WHERE customer_id = ? AND prod_id = ?""", (new_quantity, unit_price, customerID, product_id))
                else:
                    # If the product does not exist, insert a new row into CartItems
                    cursor.execute("""INSERT INTO CartItems (customer_id, prod_id, quantity, unit_price) VALUES (?, ?, ?, ?)""", (customerID, product_id, quantity, unit_price))

            # Commit the transaction
            conn.commit()
            self.show_popup("Product added to cart successfully!")
            print("closing product screen")
            self.close()

        except pyodbc.Error as e:
            conn.rollback()
            self.show_popup(f"Error: {str(e)}")
            print(f"Database Error: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
                
        self.show_catalogue_screen()

class CartScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CartScreen, self).__init__(parent)
        self.parent = parent
        uic.loadUi('Cart.ui', self)
        self.setWindowTitle("Cart")
        self.setFixedSize(self.size())
        self.pushButton_Checkout.clicked.connect(self.show_checkout_screen)
        self.label_TotalAmount.setText("0.0 Rs.")
        self.pushButton_deleteItem.clicked.connect(self.delete_item)
        self.update_cart()  # Update cart on screen load
        self.ProductsTableWidget.setColumnWidth(0, int(self.ProductsTableWidget.width() * 0.35))
        self.ProductsTableWidget.setColumnWidth(1, int(self.ProductsTableWidget.width() * 0.15))
        self.ProductsTableWidget.setColumnWidth(2, int(self.ProductsTableWidget.width() * 0.15))
        self.ProductsTableWidget.setColumnWidth(3, int(self.ProductsTableWidget.width() * 0.15))
        self.ProductsTableWidget.setColumnWidth(4, int(self.ProductsTableWidget.width() * 0.2))
        
    def show_checkout_screen(self):
        self.checkout_screen = CheckoutScreen(self)
        self.hide()
        self.checkout_screen.show()

    def show_popup(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Cart")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def update_cart(self):
        self.ProductsTableWidget.setRowCount(0)
        cart_items = self.get_cart_items()
        for item in cart_items:
            row_position = self.ProductsTableWidget.rowCount()
            self.ProductsTableWidget.insertRow(row_position)

            self.ProductsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(item["name"]))
            self.ProductsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(item["unit_price"])))
            self.ProductsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(item["quantity"])))
            self.ProductsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(item["category"]))
            self.ProductsTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(item["unit_price"] * item["quantity"])))

        total_amount = 0
        for item in cart_items:
            total_amount += item["unit_price"] * item["quantity"]
        self.label_TotalAmount.setText(str(total_amount) + " Rs.")

    def get_cart_items(self):
        cart_items = []
        conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"

        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()
            # SQL Query to fetch cart items and product details
            query = """
                SELECT P.name, P.category, CI.quantity, CI.unit_price
                FROM CartItems CI
                INNER JOIN Product P ON CI.prod_id = P.prod_id
                WHERE CI.customer_id = ?
            """
            cursor.execute(query, (customerID,))
            rows = cursor.fetchall()

            # Convert rows to list of dictionaries
            for row in rows:
                cart_items.append({
                    "name": row[0],
                    "category": row[1],
                    "quantity": row[2],
                    "unit_price": row[3]
                })

        except pyodbc.Error as e:
            print(f"Database Error: {e}")
            self.show_popup(f"Error fetching cart: {str(e)}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

        return cart_items
    
    def delete_item(self):
        # print("customerID: ", customerID)
        # print("addressID: ", addressID)
        print("usernameCustomer: ", usernameCustomer)
        print("delete_item called")
        selected_row = self.ProductsTableWidget.currentRow()
        if selected_row == -1:
            self.show_popup("Please select a product to delete.")
            return

        # Fetch product details from the selected row
        product_name = self.ProductsTableWidget.item(selected_row, 0).text()
        quantity = int(self.ProductsTableWidget.item(selected_row, 1).text())

        # Confirm if the user wants to decrease the quantity or remove the item
        confirmation = QtWidgets.QMessageBox.question(
            self,
            "Delete Item",
            "Do you want to decrease the quantity by 1?\n"
            "Click 'No' to delete the product entirely.\n",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No | QtWidgets.QMessageBox.StandardButton.Cancel
        )
        # print("customerID: ", customerID)
        # print("addressID: ", addressID)
        print("usernameCustomer: ", usernameCustomer)
        print("confirmation box opened")
        
        if confirmation == QtWidgets.QMessageBox.StandardButton.Cancel:
            # print("customerID: ", customerID)
            # print("addressID: ", addressID)
            print("usernameCustomer: ", usernameCustomer)
            print("confirmation box closed with cancel")
            return

        try:
            conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()

            if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                # print("customerID: ", customerID)
                # print("addressID: ", addressID)
                print("usernameCustomer: ", usernameCustomer)
                print("yes confirm")
                # Decrease the quantity by 1
                if quantity > 1:
                    query = """
                        UPDATE CartItems
                        SET quantity = quantity - 1
                        WHERE customer_id = ? AND prod_id = (
                            SELECT prod_id FROM Product WHERE name = ?
                        )
                    """
                    cursor.execute(query, (customerID, product_name))
                else:
                    # If quantity is 1, delete the item
                    # print("customerID: ", customerID)
                    # print("addressID: ", addressID)
                    print("usernameCustomer: ", usernameCustomer)
                    print("quantity is 1, so delete product")
                    self.remove_product(cursor, product_name)
            else:
                # Full delete
                # print("customerID: ", customerID)
                # print("addressID: ", addressID)
                print("usernameCustomer: ", usernameCustomer)
                print("full delete")
                self.remove_product(cursor, product_name)

            # Commit changes and refresh the cart
            conn.commit()
            self.update_cart()
            self.show_popup("Cart updated successfully!")

        except pyodbc.Error as e:
            conn.rollback()  # Rollback the transaction on error
            print(f"Database Error: {e}")
            self.show_popup(f"Error updating cart: {str(e)}")
        finally:
            # global cartCloseFlag 
            # cartCloseFlag = 0
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
        

    def remove_product(self, cursor, product_name):
        # print("customerID: ", customerID)
        # print("addressID: ", addressID)
        print("usernameCustomer: ", usernameCustomer)
        print("remove_product called")
        query = """
            DELETE FROM CartItems
            WHERE customer_id = ? AND prod_id = (
                SELECT prod_id FROM Product WHERE name = ?
            )
        """
        cursor.execute(query, (customerID, product_name))
        # cartCloseFlag = 0
        
    def closeEvent(self, event):
        print("closeEvent called and closing cart screen")
        # if cartCloseFlag == 0:
        #     event.ignore()
        if self.parent:
            self.parent.show()
        event.accept()
        self.update_cart()
        
class CheckoutScreen(QtWidgets.QMainWindow):
    total = 0
    def __init__(self, parent=None):
        super(CheckoutScreen, self).__init__(parent)
        self.parent = parent
        uic.loadUi('checkout.ui', self)
        self.setWindowTitle("Checkout")
        self.setFixedSize(self.size())
        self.pushButton_placeOrder.clicked.connect(self.show_place_order_screen)
        self.comboBox_cities.setPlaceholderText("Select your city")
        self.update_details()
        conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
        conn = None
        cursor = None
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        query = "SELECT firstname, lastname, email, phone FROM [Customer] WHERE customer_id = ?"
        cursor.execute(query, (customerID))
        result = cursor.fetchall()
        self.label_CustomerFirstName.setText(result[0][0])
        self.label_CustomerLastName.setText(result[0][1])
        self.label_CustomerEmail.setText(result[0][2])
        self.label_CustomerContact.setText(result[0][3])
        query = """
            select [address] from Customer c join CustomerAddress ca on c.customer_id = ca.customer_id
            join [Address] a on ca.address_id = a.address_id
            where c.customer_id = ?
            """
        cursor.execute(query, (customerID))
        result = cursor.fetchall()
        self.label_CustomerAddress.setText(result[0][0])
        query = "select distinct city from DeliveryCharges"
        cursor.execute(query)
        result = cursor.fetchall()
        self.comboBox_cities.clear()
        self.comboBox_cities.addItems([row[0] for row in result])
        cursor.close() 
        conn.close()
        
        self.checkBox_COD.stateChanged.connect(self.COD)
        self.checkBox_savedAddress.stateChanged.connect(self.UseSavedAddress)
        self.checkBox_savedCard.stateChanged.connect(self.UseSavedCard)
        self.comboBox_cities.currentIndexChanged.connect(self.updateDC)
        # print(self.comboBox_cities.currentIndex())
        
    def updateDC(self):
        conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
        conn = None
        cursor = None
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        query = """
            select cost from DeliveryCharges
            where city = ?
            """
        cursor.execute(query,(str(self.comboBox_cities.currentText())))
        result = cursor.fetchall()
        self.lineEdit_DC.setText(str(result[0][0]))
        self.lineEdit_Total.setText(str(self.total + result[0][0]))
        cursor.close() 
        conn.close()
        
    def COD(self):
        if self.checkBox_COD.isChecked():
            self.lineEdit_newCard.setReadOnly(True)
            self.lineEdit_newCVC.setReadOnly(True)
            self.dateEdit_expiry.setReadOnly(True)
        else:
            self.lineEdit_newCard.setReadOnly(False)
            self.lineEdit_newCVC.setReadOnly(False)
            self.dateEdit_expiry.setReadOnly(False)
            
    def UseSavedCard(self):
        if self.checkBox_savedCard.isChecked:
            conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
            conn = None
            cursor = None
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()
            query = """
                select cardnumber, card_cvc, card_expiry from Customer c join CustomerPaymentInfo cpi on c.customer_id = cpi.customer_id
                join PaymentInfo [pi] on [pi].payment_id = cpi.payment_id
                where c.customer_id = ?;
                """
            cursor.execute(query,(customerID))
            result = cursor.fetchall()
            try:
                self.lineEdit_newCard.setText(str(result[0][0]))
                self.lineEdit_newCVC.setText(str(result[0][1]))
                qdate = QDate.fromString(result[0][2], "yyyy-MM-dd")
                self.dateEdit_expiry.setDate(qdate)
                self.lineEdit_newCard.setReadOnly(True)
                self.lineEdit_newCVC.setReadOnly(True)
                self.dateEdit_expiry.setReadOnly(True)
                cursor.close() 
                conn.close()
            except IndexError:
                cursor.close() 
                conn.close()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)  # Set icon to critical (error)
                msg.setWindowTitle("Error")            # Set the window title
                msg.setText("No card saved")           # Set the main message
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Add OK button
                msg.exec()
                self.checkBox_savedCard.setChecked(False)
        else:
            self.lineEdit_newCard.setReadOnly(False)
            self.lineEdit_newCVC.setReadOnly(False)
            self.dateEdit_expiry.setReadOnly(False)
            self.lineEdit_newCard.clear()
            self.lineEdit_newCVC.clear()
            self.dateEdit_expiry.clear()
    def UseSavedAddress(self):
        if self.checkBox_savedAddress.isChecked():
            conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
            conn = None
            cursor = None
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()
            query = """
                select [address], city from Customer c join CustomerAddress ca on c.customer_id = ca.customer_id
                join [Address] a on ca.address_id = a.address_id
                where c.customer_id = ?
                """
            cursor.execute(query, (customerID))
            result = cursor.fetchall()
            try:
                self.lineEdit_newAddress.setText(result[0][0])
                self.lineEdit_newAddress.setReadOnly(True)
                self.comboBox_cities.setEnabled(False)
                query = """
                    select cost from DeliveryCharges dc join [Address]a on dc.city = a.city
                    join CustomerAddress ca on a.address_id = ca.address_id
                    join Customer c on c.customer_id = ca.customer_id
                    where c.customer_id = ?
                    """
                cursor.execute(query,(customerID))
                result = cursor.fetchall()
                self.lineEdit_DC.setText(str(result[0][0]))
                self.lineEdit_Total.setText(str(self.total + result[0][0]))
                cursor.close() 
                conn.close()
            except IndexError:
                cursor.close()
                conn.close()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)  # Set icon to critical (error)
                msg.setWindowTitle("Error")            # Set the window title
                msg.setText("No address saved")           # Set the main message
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Add OK button
                msg.exec()
                self.checkBox_savedAddress.setChecked(False)
        else:
            self.comboBox_cities.setEnabled(True)
            self.lineEdit_newCard.setReadOnly(False)
            self.lineEdit_newCard.clear()
            self.lineEdit_newCVC.setReadOnly(False)
            self.lineEdit_newCVC.clear()
            self.dateEdit_expiry.setReadOnly(False)
            self.dateEdit_expiry.clear()
            
    def get_cart_items(self):
        """
        Fetch cart items from the database for the current customer.
        Returns a list of dictionaries containing cart item details.
        """
        cart_items = []
        conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"

        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()
            # SQL Query to fetch cart items and product details
            query = """
                SELECT P.name, P.prod_id, CI.quantity, CI.unit_price
                FROM CartItems CI
                INNER JOIN Product P ON CI.prod_id = P.prod_id
                WHERE CI.customer_id = ?
            """
            cursor.execute(query, (customerID,))
            rows = cursor.fetchall()

            # Convert rows to list of dictionaries
            for row in rows:
                cart_items.append({
                    "name": row[0],
                    "prod_id": row[1],
                    "quantity": row[2],
                    "unit_price": row[3],
                    "Total Price": row[2] * row[3]
                })
        except pyodbc.Error as e:
            print(f"Database Error: {e}")
            self.show_popup(f"Error fetching cart: {str(e)}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
        return cart_items
    
    def update_details(self):
        # Clear existing rows
        self.ProductsTableWidget.setRowCount(0)
        # Fetch cart items from database
        cart_items = self.get_cart_items()
        # Populate the table with cart items
        for item in cart_items:
            row_position = self.ProductsTableWidget.rowCount()
            self.ProductsTableWidget.insertRow(row_position)

            self.ProductsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(item["name"]))
            self.ProductsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(item["unit_price"])))
            self.ProductsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(item["quantity"])))
            self.ProductsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(item["unit_price"] * item["quantity"])))
            self.total += item["unit_price"] * item["quantity"]
            
        self.lineEdit_DC.setText("Select City")
        self.lineEdit_Total.setText(str(self.total))


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

if __name__ == "__main__":
    app = QApplication([])
    window = Homepage()  # Create an instance of our class
    sys.exit(app.exec())