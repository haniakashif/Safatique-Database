from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyQt6.QtWidgets import QDialog , QMessageBox , QPushButton
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget,QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QInputDialog
import pyodbc

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__() 
        # Load the .ui file
        uic.loadUi('sales_screen.ui', self) 
        self.reportbutton.clicked.connect(self.show_report_screen)
        self.productsbutton.clicked.connect(self.showproducts)
        self.rawmaterial.clicked.connect(self.showEditRawMats)
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


# Initialize and display the app
app = QtWidgets.QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
