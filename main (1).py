import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from catalogue_ui import Ui_MainWindow  # Import the converted UI file

class CatalogueApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the UI from the imported file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Assuming your product items are inside a Scroll Area in the UI file
        # Check if the Scroll Area is working as expected
        self.ui.scrollArea.setWidgetResizable(True)

        # Add some basic styling (optional)
        self.setWindowTitle("Safatique Catalogue")
        self.setWindowIcon(QtGui.QIcon("path/to/icon.png"))  # Optional: Set an app icon

        # You can perform additional setup or add functionality here if needed
        # For example, loading product images, names, and prices dynamically

# Initialize and display the app
app = QtWidgets.QApplication(sys.argv)
window = CatalogueApp()
window.show()
sys.exit(app.exec())
