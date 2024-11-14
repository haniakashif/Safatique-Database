import sys
from PyQt6 import QtWidgets, QtGui
from catalogue_ui import Ui_MainWindow  # Import the generated UI code

class CatalogWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Sample product data (name and image paths)
        products = [
            {"name": "Product 1", "image": "path/to/image1.jpg"},
            {"name": "Product 2", "image": "path/to/image2.jpg"},
            {"name": "Product 3", "image": "path/to/image3.jpg"},
            # Add more products as needed
        ]

        # Add products to the scrollable area
        for product in products:
            self.add_product(product["name"], product["image"])

    def add_product(self, name, image_path):
        # Create a container widget for each product
        product_widget = QtWidgets.QWidget()
        product_layout = QtWidgets.QVBoxLayout()

        # Add image label
        image_label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(image_path)
        image_label.setPixmap(pixmap.scaled(100, 100, aspectRatioMode=1))  # Resize as needed
        product_layout.addWidget(image_label)

        # Add name label
        name_label = QtWidgets.QLabel(name)
        product_layout.addWidget(name_label)

        # Set layout to the product widget and add it to the main container
        product_widget.setLayout(product_layout)
        self.ui.productContainer.layout().addWidget(product_widget)

app = QtWidgets.QApplication(sys.argv)
window = CatalogWindow()
window.show()
sys.exit(app.exec())
