import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QPushButton,QHBoxLayout,QLabel,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,350)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.inputbox=QLineEdit(self)
        self.inputbox.setPlaceholderText("Enter the Year...")
        self.search=QPushButton("Click Here To Search")
        self.the_one=None
        self.the_input=None
        
        self.Ui()
        
    def Ui(self):
        
        QH=QHBoxLayout()
        QH.setAlignment(Qt.AlignTop)
        
        self.search.setStyleSheet("""
                                    QPushButton {
                                        background-color:rgba(255, 255, 255, 0.5);
                                        color: black;
                                        font-size: 20px;
                                        border: 2px solid #0078D7;
                                        border-radius: 20px;
                                        padding: 10px;
                                    }
                                    QPushButton:hover {
                                        background-color:rgb(147, 210, 255);
                                        color: white;
                                    }
                                """)
        self.inputbox.setStyleSheet("font-size:30px;")
        QH.addWidget(self.inputbox)
        QH.addWidget(self.search)
        
        self.setLayout(QH)    

    def on_click(self):
        
        try:
            df=pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])
            
        self.the_input=self.inputbox.text()
        self.the_one=df[(df["Year"]==self.the_input)]
        
        if self.the_one:
            for rows_ind,content in self.the_one.iterrows():
                label=QLabel(self)
                label.setText(f"""Title       {content["Title"]}
Author      {content["Author"]}
Year        {content["Year"]}
Genre     {content["Genre"]}""")
                
        































def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
