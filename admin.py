from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyQt6.QtWidgets import QApplication , QDialog , QMainWindow , QMessageBox , QPushButton

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__() 
        # Load the .ui file
        uic.loadUi('sales_screen.ui', self) 
        self.reportbutton.clicked.connect(self.show_report_screen)
        self.productsbutton.clicked.connect(self.showproducts)
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

class EditProductsScreen(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(EditProductsScreen, self).__init__()
        # Load the .ui file
        uic.loadUi('projectScreen2.ui', self)



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
