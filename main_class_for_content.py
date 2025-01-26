import sys
from PyQt5.QtWidgets import  QApplication, QTextEdit, QVBoxLayout, QWidget, QPushButton,QListWidget, QMessageBox

from PyQt5.QtGui import QIcon,QFont
import bird
import pandas as pd
import content_class


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))

        self.selected_text = None
        self.selected_title = None
        self.child_windows = []
        self.selected_content = None

        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre", "Content", "ID"])
        title_label = QPushButton(" Virtual Library")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setStyleSheet("""
            QPushButton {
                background: none;
                border: none;
                color: #0078D7;
                font-size: 32px;
                padding: 20px;
            }
        """)
        self.layout = QVBoxLayout()
        self.layout.addWidget(title_label)
        self.create_list_widget()
        self.create_buttons()
        
        self.setLayout(self.layout)
        
        

    def create_buttons(self):
        # Insert Button
        insert_button = QPushButton("Insert Content")
        insert_button.clicked.connect(self.insert_content)

        # Read Button
        read_button = QPushButton("Read Content")
        read_button.clicked.connect(self.read_content)

        # Add Buttons to Layout
        for button in [insert_button, read_button]:
            button.setStyleSheet("""
                QPushButton {
                background-color: #ffffff;
                color: #0078D7;
                font-size: 18px;
                font-weight: bold;
                border-radius: 20px;
                padding: 15px;
                margin: 10px 50px;
                border: 2px solid #ffffff;
            }
            QPushButton:hover {
                background-color: #00AFFF;
                color: white;
                border: 2px solid white;
            }
        """)
            
            self.layout.addWidget(button)

    def create_list_widget(self):
        self.book_list = QListWidget()
        self.book_list.setStyleSheet("""
            QListWidget {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                padding: 10px;
                font-size: 18px;
                color: black;
            }
            QListWidget::item {
                background: transparent;
                padding: 10px;
                margin: 5px;
            }
            QListWidget::item:nth-child(odd) {
                background: rgba(0, 120, 215, 0.1);
            }
            QListWidget::item:nth-child(even) {
                background: rgba(0, 215, 255, 0.1);
            }
            QListWidget::item:selected {
                background: #0078D7;
                color: white;
                border-radius: 5px;
            }
        """)
        self.book_list.itemClicked.connect(self.extract_selected_book)

        if not self.df.empty:
            for _, book in self.df.iterrows():
                self.book_list.addItem(
                    f'ID: {book["ID"]} - '
                    f'Title: {book["Title"]}, '
                    f'Author: {book["Author"]}, '
                    f'Year: {book["Year"]}, '
                    f'Genre: {book["Genre"]}'
                )

        self.layout.addWidget(self.book_list)

    def extract_selected_book(self, item):
        self.selected_text = item.text()
        start = self.selected_text.find("Title: ") + len("Title: ")
        end = self.selected_text.find(", Author:")
        self.selected_title = self.selected_text[start:end].strip()

        # Extract book details from DataFrame
        selected_book = self.df[self.df["Title"] == self.selected_title]
        if not selected_book.empty:
            self.selected_content = selected_book.iloc[0]["Content"]

    def insert_content(self):
        if self.selected_text:
            insertion_window = content_class.MainWindow(thecontent=self.selected_content)
            self.child_windows.append(insertion_window)
            insertion_window.show()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a book from the list.")

    def read_content(self):
        if self.selected_text:
            if self.selected_content:
                reading_window = bird.MainWindow(thecontent=self.selected_content, thetitle=self.selected_title)
                self.child_windows.append(reading_window)
                reading_window.show()
            else:
                QMessageBox.warning(self, "Content Error", "This book has no associated content.")
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a book from the list.")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
