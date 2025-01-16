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
        self.search=QPushButton("Click Here To Search")
        self.data_info = self.Ui()

    def Ui(self):
        
        self.main_vbox = QVBoxLayout()
        QH=QHBoxLayout()
        QH.setAlignment(Qt.AlignTop)
        
        self.search.setStyleSheet("""
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
        
        self.search.clicked.connect(self.on_click) 
        
        self.field=QLineEdit(self)
        self.field.setPlaceholderText(f"Enter the Title ...")
        self.field.setStyleSheet("font-size:30px; ")
        
        QH.addWidget(self.field)
        
            
        QH.addWidget(self.search)    
        self.main_vbox.addLayout(QH)
        self.setLayout(self.main_vbox)
        self.thetitle=self.field.text()
    
    def on_click(self):
        
        
        
        try:
            df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])
            
        
            
        self.main_vbox.addWidget(self.thetitle)
            
        self.setLayout(self.main_vbox)    
        
        theone = df[(df["Title"] == self.thetitle)]
        self.the_number=theone.shape[0]
        if theone.empty: 
            self.thetitle.setText("""Title: Not found  
                           
                              Author: Not found 
                               
                              Year: Not found 
                              
                              Genre: Not found""")
            
        else:
            for rows_ind,content in theone.iterrows():
                label=QLabel(content,self)
                label.setObjectName(f"label_number_{rows_ind}")
                
   
      
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
