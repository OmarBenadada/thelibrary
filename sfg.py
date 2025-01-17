import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, 
    QListWidget, QLineEdit, QLabel, QHBoxLayout, QMessageBox
)

class VirtualLibrary(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Library")
        self.setGeometry(100, 100, 400, 400)

        self.layout = QVBoxLayout()

        # List to display books
        self.book_list = QListWidget()
        self.layout.addWidget(self.book_list)

        # Input fields for book title and author
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter book title")
        self.layout.addWidget(self.title_input)

        self.author_input = QLineEdit(self)
        self.author_input.setPlaceholderText("Enter book author")
        self.layout.addWidget(self.author_input)

        # Buttons for adding, editing, and deleting books
        self.add_button = QPushButton("Add Book")
        self.add_button.clicked.connect(self.add_book)
        self.layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Edit Selected Book")
        self.edit_button.clicked.connect(self.edit_book)
        self.layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Delete Book")
        self.delete_button.clicked.connect(self.delete_book)
        self.layout.addWidget(self.delete_button)

        # Search functionality
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search by title or author")
        self.search_input.textChanged.connect(self.search_books)
        self.layout.addWidget(self.search_input)

        self.setLayout(self.layout)

        # Load books from JSON file
        self.load_books()

    def load_books(self):
        try:
            with open('books.json', 'r') as f:
                books = json.load(f)
                for book in books:
                    self.book_list.addItem(f"{book['title']} by {book['author']}")
        except FileNotFoundError:
            pass  # No books file found, start fresh

    def save_books(self):
        books = []
        for i in range(self.book_list.count()):
            item = self.book_list.item(i).text()
            title, author = item.split(" by ")
            books.append({'title': title, 'author': author})
        with open('books.json', 'w') as f:
            json.dump(books, f)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        if title and author:
            self.book_list.addItem(f"{title} by {author}")
            self.title_input.clear()
            self.author_input.clear()
            self.save_books()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter both title and author.")

    def edit_book(self):
        selected_item = self.book_list.currentItem()
        if selected_item:
            title, author = selected_item.text().split(" by ")
            self.title_input.setText(title)
            self.author_input.setText(author)
            self.book_list.takeItem(self.book_list.row(selected_item))
            self.save_books()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a book to edit.")

    def delete_book(self):
        selected_item = self.book_list.currentItem()
        if selected_item:
            self.book_list.takeItem(self.book_list.row(selected_item))
            self.save_books()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a book to delete.")

    def search_books(self):
        search_text = self.search_input.text().lower()
        self.book_list.clear()
        try:
            with open('books.json', 'r') as f:
                books = json.load(f)
                for book in books:
                    if search_text in book['title'].lower() or search_text in book['author'].lower():
                        self.book_list.addItem(f"{book['title']} by {book['author']}")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    library = VirtualLibrary()
    library.show()
    sys.exit(app.exec_())
