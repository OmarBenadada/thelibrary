import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QListWidget,QMessageBox,QLabel,QHBoxLayout
from PyQt5.QtGui import QIcon
import books
import pandas as pd
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.vbox=QVBoxLayout()
        
        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["ID", "Title", "Author", "Year", "Genre", "Content"])

        
        
        virtual_libarary=QLabel("Virtual Library",self)
        virtual_libarary.setAlignment(Qt.AlignHCenter )
        virtual_libarary.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color:rgb(8, 0, 255);
            background-color:rgb(255, 255, 255);
            padding: 20px;
            border-radius: 15px;
            border: 2px solid rgb(255, 255, 255);
            
        """)
        self.vbox.addWidget(virtual_libarary)
        
        self.book_list = QListWidget()
        self.vbox.addWidget(self.book_list)
        self.book_list.setStyleSheet("""
            font-size: 20px;
            padding: 10px;
            border: 2px solid #0078D7;
            border-radius: 10px;
            background-color:rgb(255, 255, 255);
        """)
        self.popularate()
        
        self.data_info={}
        self.Labels()
        self.Buttons()
        
    def popularate(self):
        i = 0
        listo = []
        while self.df.shape[0] > i:
            listo.append(f'ID: {self.df["ID"][i]} - The Book  {{{self.df["Title"][i]}}}  By  {{{self.df["Author"][i]}}}  Written In  {{{self.df["Year"][i]}}}  And I\'ts  {{{self.df["Genre"][i]}}}')
            i += 1
        self.book_list.addItems(listo)
        
    def Labels(self):
        self.names=['Title','Author','Year','Genre']
        for name in self.names:
            self.field=QLineEdit(self)
            self.field.setPlaceholderText(f"Enter the {name} ...")
            self.field.setStyleSheet("""
                font-size: 18px;
                padding: 10px;
                border: 2px solid #0078D7;
                border-radius: 10px;
                margin-bottom: 10px;
            """)
            self.vbox.addWidget(self.field)
            self.data_info[name]=self.field
        self.setLayout(self.vbox)  
        return self.data_info 
        
    def Buttons(self):
        
        buttons_layout = QHBoxLayout()
        
        self.add=QPushButton("Add")
        buttons_layout.addWidget(self.add)
        self.add.clicked.connect(self.on_click_add)
        
        self.remove=QPushButton("Remove")
        buttons_layout.addWidget(self.remove)
        self.remove.clicked.connect(self.on_click_remove)
        
        self.edit=QPushButton("Edit")
        buttons_layout.addWidget(self.edit)
        self.edit.clicked.connect(self.on_click_edit)
            
        buttons=[self.add,self.remove,self.edit]
        for i in buttons:
            i.setStyleSheet("""
                QPushButton {
                    background-color:rgb(14, 0, 215);
                    color: white;
                    font-size: 18px;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 10px;
                    margin: 5px;
                }
                QPushButton:hover {
                    background-color: #005BB5;
                }
            """)
        self.vbox.addLayout(buttons_layout) 
    
    def on_click_add(self):
        title = self.data_info['Title'].text().strip()
        author = self.data_info['Author'].text().strip()
        year = self.data_info['Year'].text().strip()
        genre = self.data_info['Genre'].text().strip()

        if not year.isdigit():
            QMessageBox.warning(self, "Input Error", f"Year Must Be A number not {year}")
            return

        if title and author and year and genre:
            if not self.df[(self.df["Title"] == title) & (self.df["Author"] == author) & (self.df["Year"] == year) & (self.df["Genre"] == genre)].empty:
                QMessageBox.warning(self, "Input Error", f"this book {author} already Exist in the library")
            else:
                new_id = self.df['ID'].max() + 1 if not self.df.empty else 1

                book = books.Books(title=title, author=author, year=year, genre=genre, content=title.replace(" ", "_") + ".txt")

                frame = pd.DataFrame([{"ID": new_id, "Title": book.title, "Author": book.author, "Year": book.year, "Genre": book.genre, "Content": book.content}])

                self.df = pd.concat([self.df, frame], axis=0, ignore_index=True)
                self.df.to_csv("thelibraryy.csv", index=False)

                self.book_list.addItem(f'ID: {new_id} - the book  {{{title}}}  by  {{{author}}}  written in  {{{year}}}  and its  {{{genre}}}.')

                print("book is added to the library")

                for names, labels in self.data_info.items():
                    labels.setText("")
        else:
            QMessageBox.warning(self, "Input Error", "You Forgot to Fill a Label")
                             
                             
    def on_click_remove(self):
        selected_item = self.book_list.currentItem()
        if selected_item:
            item_text = selected_item.text()

            start_of_id = item_text.find("ID:") + 4
            end_of_id = item_text.find("-")-1
            text_id = int(item_text[start_of_id:end_of_id])

            row_to_drop = self.df[self.df['ID'] == text_id].index

            self.df = self.df.drop(row_to_drop, axis=0)

            self.df.to_csv("thelibraryy.csv", index=False)

            self.book_list.takeItem(self.book_list.row(selected_item))
            for number in self.df["ID"]:
                if number>text_id:
                    self.df.loc[self.df["ID"]>text_id,"ID"]-=1
                    self.df.to_csv("thelibraryy.csv",index=False)
                    break
        else:
            QMessageBox.warning(self, "Selection Error", "You Didn't Select Any Row")
                        
                    
    def on_click_edit(self):
        
        selected_item=self.book_list.currentItem()
        
        if not selected_item:
            QMessageBox.warning(self, "Selection Error", "You Didn't Select Any Row")
            return
        
        self.book_list.takeItem(self.book_list.row(selected_item))
        item_text = selected_item.text()
        
        def exctractor(text,starting_point,end_point,forward=0,backward=0):
            thestrat=text.find(starting_point)+forward
            theend=text.find(end_point)-backward
            return text[thestrat:theend]
            
        self.text_title=exctractor(item_text,"{","}",1)
        text_author=exctractor(item_text,"by","written",5,3) 
        text_year=exctractor(item_text,"written in","and its",13,3)     
        text_genre=exctractor(item_text,"its",".",6)
        text_ID=int(exctractor(item_text,"ID:","-",4,1)) 
        
        row_to_remove=self.df[self.df["ID"]==text_ID].index
        self.df=self.df.drop(row_to_remove,axis=0)
        
        self.df.to_csv("thelibraryy.csv", index=False)
                
        items={'Title':self.text_title,"Author":text_author,"Year":text_year,"Genre":text_genre}
        for names,labels in self.data_info.items():
            labels.setText(items[names])
        for number in self.df["ID"]:
                if number>text_ID:
                    self.df.loc[self.df["ID"]>text_ID,"ID"]-=1
                    self.df.to_csv("thelibraryy.csv",index=False)
                    break
        return self.text_title

   
   
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
