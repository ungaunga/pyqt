import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                QVBoxLayout, QMenu, QAction, QLineEdit, QLabel, QScrollArea)

class Dodoso(QWidget):
    def __init__(self):
        super().__init__()
        # create layout and add submit button to it
        self.vertical_box_layout = QVBoxLayout()
        
        # create the text field and its label here
        name_label = QLabel("Name", self)
        # we will make the name_field a class property, so we can be able to access
        # it anywhere outside the constructor. (be warned: this may not the best way to do it :) )
        self.name_field = QLineEdit(self)

        # add these to the layout
        self.vertical_box_layout.addWidget(name_label)
        self.vertical_box_layout.addWidget(self.name_field)

        # add them to the 
        # create push button connect it to a slot
        submit_button = QPushButton("Submit", self)
        
        # create the menu object
        button_menu = QMenu(self)
        
        # add the menu to the button
        submit_button.setMenu(button_menu)
        # create actions
        save_action = QAction("&Save", self)
        update_action = QAction("&Update", self)

        # connect actions to slots
        save_action.triggered.connect(self.save)
        update_action.triggered.connect(self.update)

        # add actions to button
        button_menu.addAction(save_action)
        button_menu.addAction(update_action)

        self.vertical_box_layout.addWidget(submit_button)

        self.setLayout(self.vertical_box_layout)
        self.setGeometry(500,500, 300, 100)
        self.setWindowTitle('Dodoso')
        self.show()

    # these two functions will serve as slots for the two actions we have just created.
    def save(self):
        self.vertical_box_layout.addWidget(QLabel(f"Saving ... {self.name_field.text()}"))

    def update(self):
        self.vertical_box_layout.addWidget(QLabel(f"Updating ... {self.name_field.text()}"))

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = Dodoso()
    sys.exit(qapp.exec_())