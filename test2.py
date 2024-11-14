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

    def setImage(self, row, col, imagePath):
        image = ImageWidget(imagePath, self)
        self.setCellWidget(row, col, image)

if __name__ == "__main__":
    app = QApplication([])
    tableWidget = TableWidget(10, 2)
    tableWidget.setImage(0, 1, "cruella.png")  # Replace with your image path
    tableWidget.show()
    sys.exit(app.exec())