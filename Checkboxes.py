import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1050, 500, 500, 500)
        self.setWindowTitle("Checkboxes")
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(30, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You don't like food")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())