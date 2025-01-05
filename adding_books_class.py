import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
import books
import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        
        self.data_info = self.Ui()
        
        
        
    def Ui(self):
        
        vbox=QVBoxLayout()
        
        save=QPushButton("Clich Here To Save")
        
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
        save.clicked.connect(self.on_click)
        
        names=['Title','Author','Year','Genre']
        self.data_info={}
        for name in names:
            field=QLineEdit(self)
            field.setPlaceholderText(f"Enter the {name} ...")
            field.setStyleSheet("font-size:30px; ")
            vbox.addWidget(field)
            self.data_info[name]=field
        
        vbox.addWidget(save)    
        self.setLayout(vbox)  
        return self.data_info 
    
    def on_click(self):
        
        title=self.data_info['Title'].text()
        author=self.data_info['Author'].text()
        year=self.data_info['Year'].text()
        genre=self.data_info['Genre'].text()
        
        try:
            df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])
        
        if not df[(df["Title"]==title) & (df["Author"]==author)].empty:
            print(f"this book {author} already Exist in the library ")
            
   
        else:
            book = books.Books(title=title, author=author, year=year, genre=genre)
            frame = pd.DataFrame([{"Title": book.title, "Author": book.author, "Year": book.year, "Genre": book.genre}])
            
            df=pd.concat([df,frame],axis=0,ignore_index=True)
            
            df.to_csv("thelibraryy.csv", index=False)
            
            print("book is added to the library")
        
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
