import sys
from PyQt5.QtWidgets import (
    QApplication, QLineEdit, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QScrollArea
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import pandas as pd

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 800, 600)
        self.setWindowTitle("Virtual Library - Search by Title")
        self.setWindowIcon(QIcon("bookshelf.png"))

        # Set up the main UI
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        # Title input field
        self.title_field = QLineEdit(self)
        self.title_field.setPlaceholderText("Enter the book title...")
        self.title_field.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                padding: 10px;
                border: 2px solid #0078D7;
                border-radius: 10px;
            }
        """)

        # Search button
        self.search_button = QPushButton("Search")
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
        self.search_button.clicked.connect(self.search_books)

        # Add input and button to the layout
        self.main_layout.addWidget(self.title_field)
        self.main_layout.addWidget(self.search_button)

        # Scroll area for displaying results
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background: #f7f7f7; border: none;")
        self.result_widget = QWidget()
        self.result_layout = QVBoxLayout(self.result_widget)
        self.scroll_area.setWidget(self.result_widget)

        # Add scroll area to the main layout
        self.main_layout.addWidget(self.scroll_area)

        self.setLayout(self.main_layout)

    def search_books(self):
        title = self.title_field.text().strip()
        if not title:
            QMessageBox.warning(self, "Input Error", "Please enter a book title.")
            return

        # Read the library data
        try:
            df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Library file not found!")
            return

        # Filter books by title
        matching_books = df[df["Title"].str.contains(title, case=False, na=False)]

        # Clear previous results
        while self.result_layout.count():
            item = self.result_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Display results
        if matching_books.empty:
            QMessageBox.information(self, "Search Result", f"No books found with the title '{title}'.")
        else:
            for _, book in matching_books.iterrows():
                # Directly create labels without using QFrame
                book_layout = QVBoxLayout()

                title_label = QLabel(f"Title: <b>{book['Title']}</b>")
                author_label = QLabel(f"Author: <i>{book['Author']}</i>")
                year_label = QLabel(f"Year: {book['Year']}")
                genre_label = QLabel(f"Genre: {book['Genre']}")

                for label in (title_label, author_label, year_label, genre_label):
                    label.setStyleSheet("font-size: 16px;")

                # Add labels to layout
                for label in (title_label, author_label, year_label, genre_label):
                    book_layout.addWidget(label)

                # Create a widget to hold the layout and add it to the result layout
                book_widget = QWidget()
                book_widget.setLayout(book_layout)
                self.result_layout.addWidget(book_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
