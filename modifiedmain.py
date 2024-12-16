import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QGridLayout, QScrollArea, QDialog, QTableWidget
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt
import pyodbc


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
        self.pushButton_login.clicked.connect(self.show_catalogue_screen) #change this to validate_login
        # self.pushButton_close.clicked.connect(self.close)
        
    def show_signup_screen(self):
        self.signup_screen = SignupScreen(self)
        self.hide()
        self.signup_screen.show()
        
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
            cursor.close()
            conn.close()
            
            if len(result) > 0 and result[0].role == 'customer':
                self.show_catalogue_screen()  # Open the next screen if login is successful
            elif len(result) > 0 and result[0].role == 'admin':
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
        self.hide()
        self.catalogue_screen.show()
        
    # def show_admin_screen(self):
    #     self.admin_screen = UI(self)
    #     self.hide()
    #     self.admin_screen.show()

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
            conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
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
                    print("User inserted successfully")

                    # Insert into Customer table
                    query2 = "INSERT INTO Customer (firstname, lastname, email, phone) VALUES (?, ?, ?, ?);"
                    cursor.execute(query2, (firstName, lastName, email, phone))
                    print("Customer inserted successfully")
                    
                    # Insert into UserCustomer table
                    query3 = "SELECT customer_id FROM Customer WHERE firstname = ? and lastname = ? and email = ? and phone = ?;"
                    cursor.execute(query3, (firstName, lastName, email, phone))
                    customer_id = cursor.fetchall()
                    # print("customer_id: ", customer_id)
                    query4 = "INSERT INTO UserCustomer (username, customer_id) VALUES (?, ?);"
                    cursor.execute(query4, (username, int(customer_id[0][0])))
                    print("UserCustomer inserted successfully")
                    
                    # insert into Address table
                    query5 = "INSERT INTO [Address] (address, city) VALUES (?, ?);"
                    cursor.execute(query5, (address, city))
                    print("Address inserted successfully")
                    
                    # insert into CustomerAddress table
                    query6 = "SELECT address_id FROM [Address] WHERE address = ? and city = ?;"
                    cursor.execute(query6, (address, city))
                    address_id = cursor.fetchall()
                    print("address_id: ", address_id)
                    query7 = "INSERT INTO CustomerAddress (customer_id, address_id) VALUES (?, ?);"
                    cursor.execute(query7, (int(customer_id[0][0]), int(address_id[0][0])))
                    print("CustomerAddress inserted successfully")

                    # Commit the transaction
                    conn.commit()
                    self.show_popup("Sign up successful. Please log in to continue.")
                    self.close()
                    print("signup screen closed")
            except pyodbc.Error as e:
                print(f"Database error: {e}")
                if conn:
                    conn.rollback()  # Rollback transaction in case of any error
                self.show_popup("Database error: " + str(e))
                # print(f"Database error: {e}")
            except Exception as e:
                print(f"Error: {e}")
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
            # Ensure the logo scales appropriately
            self.logoLabel.setScaledContents(False)

            # Configure scroll area for products
            self.scrollArea.setWidgetResizable(True)
            self.scrollAreaWidgetContents = QWidget()
            self.productGridLayout = QGridLayout(self.scrollAreaWidgetContents)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            # Set the window to be non-resizable and adjust to content
            self.setFixedSize(1290, 720)

            # Connect UI elements
            self.pushButton_applyFilters.clicked.connect(self.apply_filters)
            self.pushButton_viewCart.clicked.connect(self.show_cart_screen)

            self.populate_products() # Populate products initially
            self.load_categories()  # Load categories from the database
        except Exception as e:
            print(f"Error during initialization: {e}")

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

            print("Final query:", query)  # Debug: print the query
            print("Parameters:", params)  # Debug: print the parameters

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
        # Get selected category and search keyword
        category = self.categoryComboBox.currentText()
        keyword = self.searchLineEdit.text().strip()  # Remove extra spaces

        # Prepare filters dictionary
        filters = {}
        if category and category != "All Categories":
            filters["category"] = category
        if keyword:
            filters["keyword"] = keyword

        print(f"Applying filters: {filters}")  # Debugging

        # Refresh the product grid with filters
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
            self.show_cart_screen()  # Navigate to the cart screen
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
        self.pushButton_backToCatalogue.clicked.connect(self.close)
        
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

if __name__ == "__main__":
    app = QApplication([])
    window = Homepage()  # Create an instance of our class
    sys.exit(app.exec())