from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget
from PyQt6.QtGui import QPixmap, QPainter
import sys

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
    tableWidget = TableWidget(1, 2)
    tableWidget.setImage(0, 1, "charms1.jpg")  # Replace with your image path
    tableWidget.setRowHeight(0, 200)  # Set row height
    tableWidget.setColumnWidth(1, 200)  # Set column width
    tableWidget.show()
    sys.exit(app.exec())