import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout)

class Dodoso(QWidget):
    def __init__(self):
        super().__init__()
        
        # QPushButton
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.respond_to_button_click)

        vertical_box_layout = QVBoxLayout()
        vertical_box_layout.addWidget(submit_button)
        
        self.setLayout(vertical_box_layout)
        self.setGeometry(500,500,500,300)
        self.setWindowTitle('Dodoso')
        self.show()

    def respond_to_button_click(self):
        print("Button clicked")

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = Dodoso()
    sys.exit(qapp.exec_())