import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget
from PyQt6.QtGui import QPixmap, QPainter

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

        # Create and set up the table widget
        self.tableWidget = TableWidget(1, 2, self)
        self.tableWidget.setGeometry(50, 50, 400, 300)  # Adjust the position and size as needed
        self.tableWidget.setImage(0, 1, "charms1.jpg")  # Replace with your image path
        self.tableWidget.setRowHeight(0, 200)  # Set row height
        self.tableWidget.setColumnWidth(1, 200)  # Set column width
        # self.tableWidget.show()
        
    def show_login_screen(self):
        self.login_screen = LoginScreen()
        self.setFixedSize(self.size())
        self.login_screen.show()


class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi('login screen.ui', self)
        self.setWindowTitle("Login")
        self.setFixedSize(self.size())
        self.pushButton_signup.clicked.connect(self.show_signup_screen)
        self.pushButton_login.clicked.connect(self.show_catalogue_screen)
        
    def show_signup_screen(self):
        self.signup_screen = SignupScreen()
        self.setFixedSize(self.size())
        self.signup_screen.show()
        
    def show_catalogue_screen(self):
        self.catalogue_screen = CatalogueScreen()
        self.setFixedSize(self.size())
        self.catalogue_screen.show()
        
class SignupScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignupScreen, self).__init__()
        uic.loadUi('signupscreen.ui', self)
        self.setWindowTitle("Sign Up")
        self.setFixedSize(self.size())
        
class CatalogueScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(CatalogueScreen, self).__init__()
        uic.loadUi('catalogue2.ui', self)
        self.setWindowTitle("Safatique Catalogue")
        self.setFixedSize(self.size())
        self.label_logo.setPixmap(QPixmap("./images/axolotl.jpg"))
        self.scrollArea_products.setWidgetResizable(True)
        self.pushButton_viewCart.clicked.connect(self.show_cart_screen)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_findProducts.clicked.connect(self.show_productCategory_screen)
        # self.radioButton_charms.clicked.connect(self.show_products_screen)
        
    def show_cart_screen(self):
        self.cart_screen = CartScreen()
        self.setFixedSize(self.size())
        self.cart_screen.show()
        
    def show_productCategory_screen(self):
        self.product_category_screen = ProductCategoryScreen()
        self.setFixedSize(self.size())
        self.product_category_screen.show()
        
class ProductCategoryScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProductCategoryScreen, self).__init__()
        uic.loadUi('productCategory.ui', self)
        self.setWindowTitle("Product Category")
        self.setFixedSize(self.size())
        self.pushButton_viewProduct.clicked.connect(self.show_products_screen)
        
    def show_products_screen(self):
        self.products_screen = ProductsScreen()
        self.setFixedSize(self.size())
        self.products_screen.show()


class ProductsScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProductsScreen, self).__init__()
        uic.loadUi('productpage.ui', self)
        self.setWindowTitle("Safatique Products")
        self.setFixedSize(self.size())
        self.pushButton_addToCart.clicked.connect(self.show_cart_screen)
        
    def show_cart_screen(self):
        # Simulate Add_to_cart placement logic
        Add_to_cart_successful = True  # Replace with actual logic

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

class CartScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(CartScreen, self).__init__()
        uic.loadUi('Cart.ui', self)
        self.setWindowTitle("Cart")
        self.setFixedSize(self.size())
        self.pushButton_Checkout.clicked.connect(self.show_checkout_screen)
        self.pushButton_backToCatalogue.clicked.connect(self.close)
        
    def show_checkout_screen(self):
        self.checkout_screen = CheckoutScreen()
        self.setFixedSize(self.size())
        self.checkout_screen.show()
        
class CheckoutScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(CheckoutScreen, self).__init__()
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

class ImageWidget(QWidget):
    def __init__(self, imagePath, parent):
        super(ImageWidget, self).__init__(parent)
        self.picture = QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.picture)

class TableWidget(QTableWidget):
    def __init__(self, *args):
        super(TableWidget, self).__init__(*args)
        self.setShowGrid(False)  # Disable grid lines

    def setImage(self, row, col, imagePath):
        image = ImageWidget(imagePath, self)
        self.setCellWidget(row, col, image)
        self.resizeRowToContents(row)
        self.resizeColumnToContents(col)

if __name__ == "__main__":
    app = QApplication([])
    window = UI()  # Create an instance of our class
    sys.exit(app.exec())