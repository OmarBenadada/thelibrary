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
        self.book_title=QLabel("Here Is The Title Of The Book :",self)
        self.book_author=QLabel("Here Is The Author Of The Book :",self)
        self.book_year=QLabel("Here Is The Year Of The Book :",self)
        self.book_genre=QLabel("Here Is The Genre Of The Book :",self)
        self.data_info = self.Ui()

    def Ui(self):
        
        main_vbox=QVBoxLayout()
        QH=QHBoxLayout()
        QH.setAlignment(Qt.AlignTop)
        
        save=QPushButton("Click Here To Search")
        save.setStyleSheet("""
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
        ##save.clicked.connect(self.on_click)
        
        names=['Title','Author']
        names2=[self.book_title,self.book_author,self.book_year,self.book_genre]
        self.data_info={}
        for name in names:
            field=QLineEdit(self)
            field.setPlaceholderText(f"Enter the {name} ...")
            field.setStyleSheet("font-size:30px; ")
            QH.addWidget(field)
            self.data_info[name]=field
        QH.addWidget(save)
        main_vbox.addLayout(QH)
            
        for i in names2:
            main_vbox.addWidget(i)
            i.setStyleSheet("font-size:20px;")
        
            
        self.setLayout(main_vbox)      
        return self.data_info 
    
    
    # def on_click(self):
        
    #     title=self.data_info['Title'].text()
    #     author=self.data_info['Author'].text()
    #     year=self.data_info['Year'].text()
    #     genre=self.data_info['Genre'].text()
        
    #     if not year.isdigit():
    #         print("Year must be a valid number.")
    #         return
        
        
    #     try:
    #         df = pd.read_csv("thelibraryy.csv")
    #     except FileNotFoundError:
    #         df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])
        
    #     if not df[(df["Title"]==title) & (df["Author"]==author)].empty:
    #         print(f"this book {author} already Exist in the library ")
            
   
    #     else:
    #         book = books.Books(title=title, author=author, year=year, genre=genre)
    #         frame = pd.DataFrame([{"Title": book.title, "Author": book.author, "Year": book.year, "Genre": book.genre}])
            
    #         df=pd.concat([df,frame],axis=0,ignore_index=True)
            
    #         df.to_csv("thelibraryy.csv", index=False)
            
    #         print("book is added to the library")
        
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
