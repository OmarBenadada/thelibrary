import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QPushButton,QHBoxLayout,QLabel,QVBoxLayout,QFrame,QMessageBox
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,400)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre","Content"])

        self.data_info = self.Ui()
        
        
    def Ui(self):

        self.main_vbox = QVBoxLayout()

        QH = QHBoxLayout()
        
        header_label = QLabel("Virtual Library")
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("color: #0078D7; margin-bottom: 20px;")
        self.main_vbox.addWidget(header_label)
        
        QH.setAlignment(Qt.AlignTop)
     
        names = ['Title', 'Author']
        self.data_info = {}
        for name in names:
            field = QLineEdit(self)
            field.setPlaceholderText(f"Enter the {name} ...")
            field.setStyleSheet("""
                QLineEdit {
                    font-size: 18px;
                    padding: 8px;
                    border: 2px solid #ccc;
                    border-radius: 10px;
                }
                QLineEdit:focus {
                    border-color: #0078D7;
                }
            """)
            QH.addWidget(field)
            self.data_info[name] = field

        search = QPushButton("Search")
        search.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                background-color: #0078D7;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #005BB5;
            }
        """)
        QH.addWidget(search)
        search.clicked.connect(self.on_click)
        
        self.main_vbox.addLayout(QH)
        self.setLayout(self.main_vbox)
        
        return self.data_info

    def on_click(self):
        title = self.data_info['Title'].text().strip().lower()
        author = self.data_info['Author'].text().strip().lower()

        self.setLayout(self.main_vbox)

        theone = self.df[(self.df["Title"] == title) & (self.df["Author"] == author)]

        if theone.empty:
            QMessageBox.warning(self, "Error", "No Book Was Found")
        else:
            for index, info in theone.iterrows():
                frame_book = QFrame()
                
                frame_book.setStyleSheet("""
                    QFrame {
                        background: white;
                        border: 1px solid #ddd;
                        border-radius: 10px;
                        padding: 10px;
                        margin-bottom: 5px; 
                    }
                """)

                result_book = QVBoxLayout(frame_book)

                label_title = QLabel(f"Title: <b>{info['Title']}</b>")
                label_author = QLabel(f"Author: <b>{info['Author']}</b>")
                label_year = QLabel(f"Year: {info['Year']}")
                label_genre = QLabel(f"Genre: {info['Genre']}")

                for i in (label_title, label_author, label_year, label_genre):
                    i.setStyleSheet("font-size: 20px;")
                    result_book.addWidget(i)
                self.main_vbox.addWidget(frame_book)

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
