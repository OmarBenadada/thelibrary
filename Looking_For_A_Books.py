import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QPushButton,QHBoxLayout,QLabel,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import books
import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,800,800)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.book_title=QLabel(self)
        self.book_author=QLabel(self)
        self.book_year=QLabel(self)
        self.book_genre=QLabel(self)
        self.data_info = self.Ui()

    def Ui(self):
        
        self.main_vbox = QVBoxLayout()
        QH=QHBoxLayout()
        QH.setAlignment(Qt.AlignTop)
        
        search=QPushButton("Click Here To Search")
        search.setStyleSheet("""
                QPushButton {
                    background-color:rgba(255, 255, 255, 0.5);
                    color: black;
                    font-size: 25px;
                    border: 2px solid #0078D7;
                    border-radius: 20px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color:rgb(147, 210, 255);
                    color: white;
                }
            """)
        search.clicked.connect(self.on_click)
        
        names=['Title','Author']
        self.data_info={}  
        for name in names:
            field=QLineEdit(self)
            field.setPlaceholderText(f"Enter the {name} ...")
            field.setStyleSheet("font-size:20px; ")
            QH.addWidget(field)
            self.data_info[name]=field
            
        QH.addWidget(search)    
        self.main_vbox.addLayout(QH)
        self.setLayout(self.main_vbox)
        return self.data_info 
    
    
    def on_click(self):
        
        title=self.data_info['Title'].text()
        author=self.data_info['Author'].text()
        
        
        try:
            df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])
            
        names2=[self.book_title,self.book_author,self.book_year,self.book_genre] 
        for i in names2:
            i.setStyleSheet("font-size:20px; ")    
            self.main_vbox.addWidget(i)
            
        self.setLayout(self.main_vbox)    
        
        theone = df[(df["Title"] == title) & (df["Author"] == author)]
        
        if theone.empty: 
            self.book_title.setText("Title: Not found")
            self.book_author.setText("Author: Not found")
            self.book_year.setText("Year: Not found")
            self.book_genre.setText("Genre: Not found")
            
        else:
            thetwo = theone.iloc[0]
            self.book_title.setText(f"The Title of the Book you want is: {{{thetwo['Title']}}}")
            self.book_author.setText(f"The Author of the Book you want is: {{{thetwo['Author']}}}")
            self.book_year.setText(f"The Year of Release of the Book you want is: {{{thetwo['Year']}}}")
            self.book_genre.setText(f"The Genre of the Book you want is: {{{thetwo['Genre']}}}")
   
        
            
        
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
