import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox)
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        # Create the labels
        self.voice_index_label = QLabel("Voice index:")
        self.voice_rate_label = QLabel("Voice rate:")
        self.apps_label = QLabel("Apps:")
        # Create the line edits
        self.voice_index_line_edit = QLineEdit()
        self.voice_rate_line_edit = QLineEdit()
        self.apps_line_edit = QLineEdit()
        # Create the buttons
        self.add_app_button = QPushButton("+")
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.add_app)
        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.voice_index_label)
        layout.addWidget(self.voice_index_line_edit)
        layout.addWidget(self.voice_rate_label)
        layout.addWidget(self.voice_rate_line_edit)
        layout.addWidget(self.apps_label)
        layout.addWidget(self.apps_line_edit)
        layout.addWidget(self.add_app_button)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)
    def add_app(self):
        # Get the app name from the line edit.
        app_name = self.apps_line_edit.text()
        # Check if the app name is valid.
        if not app_name.isalpha():
            # The app name is not valid. Show an error message.
            QMessageBox.warning(self, "Invalid app name", "The app name can only contain alphabets.")
            return
        # Add the app name to the list of apps.
        self.apps_list.append(app_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())