import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QGridLayout, QScrollArea, QDialog, QTableWidget
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt
import pyodbc


def query_products(filters=None):
    conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
    products = []

    try:
        # Establish connection
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()

        # Base query
        query = "SELECT prod_id, name, price, category, description, photo_path FROM [product]"

        cursor.execute(query)

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

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__()
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
            query = "SELECT username, [password] FROM [User] WHERE username = ? AND [password] = ?" 
            cursor.execute(query, (username, password))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            
            if len(result) > 0:
                self.show_catalogue_screen()  # Open the next screen if login is successful
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

        if not firstName or not lastName or not email or not phone or not address or not username or not password or not repassword:
            self.show_popup("All fields are required.")
        elif password != repassword:
            self.show_popup("Passwords do not match.")
        elif len(username) > 10:
            self.show_popup("Username cannot be more than 10 characters long.")
        else:
            conn_string = "Driver={SQL Server};Server=ANYA\\SQLSERVER;Database=safatique;Trusted_Connection=True;"
            try:
                conn = pyodbc.connect(conn_string)
                cursor = conn.cursor()

                # Check if username already exists
                query = "SELECT username FROM [User] WHERE username = ?"
                cursor.execute(query, (username,))
                result = cursor.fetchall()
                if len(result) > 0:
                    self.show_popup("Username already exists. Please choose another username.")
                else:
                    # Start a transaction
                    try:
                        # Insert into User table
                        query1 = "INSERT INTO [User] (username, [password], [role]) VALUES (?, ?, ?)"
                        cursor.execute(query1, (username, password, 'customer'))
                        print("User inserted successfully")

                        # Insert into Customer table
                        query2 = "INSERT INTO Customer (firstname, lastname, email, phone) VALUES (?, ?, ?, ?);"
                        cursor.execute(query2, (firstName, lastName, email, phone))
                        print("Customer inserted successfully")

                        # Commit the transaction
                        conn.commit()
                        self.show_popup("Sign up successful. Please log in to continue.")
                        self.close()
                    except pyodbc.Error as e:
                        # Rollback transaction in case of error
                        conn.rollback()
                        self.show_popup("Error: " + str(e))
                        print(f"Transaction error: {e}")
            except pyodbc.Error as e:
                self.show_popup("Database connection error: " + str(e))
                print(f"Database connection error: {e}")
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
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
            self.logoLabel.setScaledContents(True)

            # Configure scroll area for products
            self.scrollArea.setWidgetResizable(True)
            self.scrollAreaWidgetContents = QWidget()
            self.productGridLayout = QGridLayout(self.scrollAreaWidgetContents)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            # Set the window to be non-resizable and adjust to content
            self.setFixedSize(1200, 720)

            # Connect UI elements
            self.applyFiltersButton.clicked.connect(self.apply_filters)
            self.pushButton_viewCart.clicked.connect(self.show_cart_screen)

            # Populate products initially
            self.populate_products()
        except Exception as e:
            print(f"Error during initialization: {e}")

    def populate_products(self, filters=None):
        # Clear existing products
        for i in reversed(range(self.productGridLayout.count())):
            widget = self.productGridLayout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Query products (you can add filters here if needed)
        products = query_products(filters)

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
            title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            title_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
            title_label.mousePressEvent = lambda _, p=product: self.open_product_view(p)
            title_label.mousePressEvent = lambda event, p=product: self.open_product_view(p)
            product_layout.addWidget(title_label)
            # Price
            price_label = QLabel(str(product["price"]))
            price_label.setStyleSheet("color: green; text-align: center;")
            price_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        category = self.categoryComboBox.currentText()
        keyword = self.searchLineEdit.text()
        filters = {"category": category, "keyword": keyword}
        print(f"Applying filters: {filters}")
        self.populate_products(filters)

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
            self.label_price.setText(str(self.product["price"]))
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
    window = UI()  # Create an instance of our class
    sys.exit(app.exec())