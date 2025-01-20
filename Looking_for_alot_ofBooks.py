import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QMessageBox,QLabel,QScrollArea,QFrame
from PyQt5.QtGui import QIcon
import pandas as pd

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
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])

        
    def Ui(self):
        
        self.QV=QVBoxLayout()
    
        self.title_label.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                padding: 10px;
                border: 2px solid #0078D7;
                border-radius: 10px;
            }
        """)
        self.QV.addWidget(self.title_label)
        
        self.search_button.setStyleSheet("""
                    QPushButton {
                        background-color: #0078D7;
                        color: White;
                        font-size: 15px;
                        border-radius: 20px;
                        font-weight: bold;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color:rgb(147, 210, 255);
                        color: white;}""")
        self.QV.addWidget(self.search_button)
        self.search_button.clicked.connect(self.search)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background: #f7f7f7; border: none;")
        self.result_box=QWidget()
        self.QV_result_box=QVBoxLayout(self.result_box)
        self.scroll_area.setWidget(self.result_box)
        self.QV.addWidget(self.scroll_area)
        
            
        self.setLayout(self.QV)
        
    def search(self):
        title=self.title_label.text()
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
