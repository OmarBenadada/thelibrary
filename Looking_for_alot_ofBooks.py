import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QMessageBox,QLabel,QScrollArea,QFrame,QHBoxLayout
from PyQt5.QtGui import QIcon,QFont
import pandas as pd
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.title_label=QLineEdit(self)
        self.title_label.setPlaceholderText("Enter the Title Here...")
        self.search_button=QPushButton("Search")
        self.Ui()
        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre","Content"])

        
    def Ui(self):
        
        self.QV=QVBoxLayout()
        self.QH=QHBoxLayout()
        
        virtual_libarary = QLabel("Virtual Library")
        virtual_libarary.setFont(QFont("Arial", 24, QFont.Bold))
        virtual_libarary.setAlignment(Qt.AlignCenter)
        virtual_libarary.setStyleSheet("color: #2E86C1; margin-bottom: 20px;")
        self.QV.addWidget(virtual_libarary)
    
        virtual_libarary.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color:rgb(8, 0, 255);
            padding: 10px;
            
        """)
        self.title_label.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                padding: 8px;
                border: 2px solid #ccc;
                border-radius: 10px;
            }
            QLineEdit:focus {
                border-color: #0078D7;
            }""")
        
        self.QH.addWidget(self.title_label)
        
        self.search_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                background-color: #0078D7;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #005BB5;
            }
        """)
        self.QH.addWidget(self.search_button)
        self.search_button.clicked.connect(self.search)
        self.QV.addLayout(self.QH)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background: #f7f7f7; border: none;")
        self.result_box=QWidget()
        self.QV_result_box=QVBoxLayout(self.result_box)
        self.scroll_area.setWidget(self.result_box)
        self.QV.addWidget(self.scroll_area)
        
            
        self.setLayout(self.QV)
        
    def search(self):
        title=self.title_label.text().strip().lower()
        theone=self.df[self.df["Title"]==title]
        
        while self.QV_result_box.count():
            item=self.QV_result_box.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        if not title:
            QMessageBox.warning(self,"Input Error",f"You Didnt Enter Anything")
        else:    
            if theone.empty:
                QMessageBox.warning(self,"Input Error",f"No Book Was Found")
            else:
                for number,books in theone.iterrows():
                    book_frame=QFrame()
                    book_frame.setStyleSheet("""
                    QFrame {
                        background: white;
                        border: 1px solid #ddd;
                        border-radius: 10px;
                        padding: 10px;
                        margin-bottom: 10px;
                    }
                """)
                    Vbox=QVBoxLayout(book_frame)
                    
                    Title_label = QLabel(f"Title: <b>{books['Title']}</b>")
                    Author_label = QLabel(f"Author: {books['Author']}")
                    Year_label = QLabel(f"Year: {books['Year']}")
                    Genre_label = QLabel(f"Genre: {books['Genre']}")
                    
                    all_labels=[Title_label,Author_label,Year_label,Genre_label]
                    for labels in all_labels:
                        labels.setStyleSheet("font-size: 20px;")
                        Vbox.addWidget(labels)
                    
                    self.QV_result_box.addWidget(book_frame) 
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
