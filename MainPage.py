from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont

class MainPage(QWidget):
    back_to_entry = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Set window title , font and layout
        self.setWindowTitle('Main Page')
        self.title = QLabel('This is the Main Page', self)
        self.title.setFont(QFont("Playfair Display", 24))
        self.title.setAlignment(Qt.AlignCenter)

        # Button to go back to entry page
        self.back_button = QPushButton('Back to Entry Page', self)
        self.back_button.clicked.connect(self.back_to_entry.emit)

        # Add widgets to layout
        layout.addWidget(self.title)
        layout.addWidget(self.back_button)
        self.setLayout(layout)