import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMenu, QAction)

class Dodoso(QWidget):
    def __init__(self):
        super().__init__()
        
        # create push button connect it to a slot
        submit_button = QPushButton("Submit", self)
        
        # create the menu object
        button_menu = QMenu(self)
        
        # add the menu to the button
        submit_button.setMenu(button_menu)
        # create actions
        save_action = QAction("&Save", self)
        update_action = QAction("&Update", self)

        # add actions to button
        button_menu.addAction(save_action)
        button_menu.addAction(update_action)

        # create layout and add submit button to it
        vertical_box_layout = QVBoxLayout()
        vertical_box_layout.addWidget(submit_button)
        
        self.setLayout(vertical_box_layout)
        self.setGeometry(500,500,500,300)
        self.setWindowTitle('Dodoso')
        self.show()

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = Dodoso()
    sys.exit(qapp.exec_())