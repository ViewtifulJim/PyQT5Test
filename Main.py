import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project Name")
        # 4 args x and y coordinates, height and weight of the window
        self.setGeometry(1050, 500, 500, 500)
        # this sets the window icon
        self.setWindowIcon(QIcon("testicon.jpg"))

        # basic label construction
        label = QLabel("Hello there...", self)
        label.setFont(QFont("Aptos", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #26d491;"
                            "background-color: #a060b5;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # text alignment
        #label.setAlignment(Qt.AlignTop) # align vertically to the top
        #label.setAlignment(Qt.AlignBottom) # align vertically to the bottom
        #label.setAlignment(Qt.AlignVCenter) # align vertically to the center

        #label.setAlignment(Qt.AlignRight) # align horizontally to the right
        #label.setAlignment(Qt.AlignLeft) # align horizontally to the left
        #label.setAlignment(Qt.AlignHCenter) # align horizontally to center

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # align in the very center which combines both
        #or...
        label.setAlignment(Qt.AlignCenter)

        # images
        label2 = QLabel(self)
        label2.setGeometry(0, 0, 400, 400)

        pixmap = QPixmap("hellothere.png") # load image
        label2.setPixmap(pixmap) # assign image to label 2

        label2.setScaledContents(True) # scale image to fit


        # how to center the image
        #label2.setGeometry((self.width() - label2.width()) // 2,
                           #(self.height() - label2.height()) // 2,
                           #label2.width(),
                           #label2.height())

        label2.setGeometry((self.width() - label2.width()) // 2,
                           100,
                           label2.width(),
                           label2.height())

        #additional line for git commit test

        label2.setGeometry((self.width() - label2.width()) // 2,
                           100,
                           label2.width(),
                           label2.height())






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()





