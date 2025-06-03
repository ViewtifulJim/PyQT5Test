import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1050, 500, 500, 500)
        self.setWindowTitle("Buttons")
        # declare variables here then use them elsewhere
        self.button  = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        # styling the variable declared in the constructor
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px")
        # with buttons you need a signal connected to a slot as below
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")

    def on_click(self):
        # print("clicked")
        # self.button.setText("clicked other")
        # # example of disabling the button
        # self.button.setDisabled(True)
        if self.label.text() == "Hello":
            self.label.setText("Goodbye")
        else:
            self.label.setText("Hello")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())