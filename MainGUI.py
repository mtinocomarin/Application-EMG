
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox , QStackedWidget
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal

from MainPage import MainPage

# QApplication main application handler 
# Qlabel to display text and images
# QWidget is the base class for all UI objects in PyQt
# QVBoxLayout to arrange widgets vertically
# QPushButton to create clickable button



# Start of the main GUI application
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title
        self.setWindowTitle('EMG GUI Application')

        # Helper function to setup window size
        self._setup_size() 
        self.stack = QStackedWidget(self)

        # Create instances of different pages
        self.entry_page = EntryPage()
        self.main_page = MainPage()

        # Add pages to the stacked widget
        self.stack.addWidget(self.entry_page)
        self.stack.addWidget(self.main_page)

        # wire up signals and slots for navigation between pages
        self.entry_page.nextRequested.connect(lambda: self.stack.setCurrentIndex(1))
        self.main_page.back_to_entry.connect(lambda: self.stack.setCurrentIndex(0))

        # Layout to hold the stacked widget
        root_layout = QVBoxLayout()
        root_layout.addWidget(self.stack)
        self.setLayout(root_layout)


    # Setup Window size dynamically based on screen size
    # Minimum size is set to 700x450 if screen size is smaller
    # otherwise if unable to get screen size, default to 900x600
    def _setup_size(self):
        screen = QGuiApplication.primaryScreen()
        if screen:
            size = screen.availableGeometry().size()
            self.resize(max(700, size.width()//2), max(450, size.height()//2))
        else:
            self.resize(900, 600)


class EntryPage(QWidget):
    nextRequested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout()

        # Set title of the entry page
        self.title = QLabel('Welcome to the EMGs GUI Application', self)
        self.title.setFont(QFont("Playfair Display", 24))
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        # Button to navigate to the main page
        self.next_button = QPushButton('Enter Application', self)
        self.next_button.clicked.connect(self.nextRequested.emit)
        layout.addWidget(self.next_button)
        self.setLayout(layout)

    # Setup Window size dynamically based on screen size
    # Minimum size is set to 700x450 if screen size is smaller
    # otherwise if unable to get screen size, default to 900x600
    def _setup_size(self):
        screen = QGuiApplication.primaryScreen()
        if screen:
            size = screen.availableGeometry().size()
            self.resize(max(700, size.width()//2), max(450, size.height()//2))
        else:
            self.resize(900, 600)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())