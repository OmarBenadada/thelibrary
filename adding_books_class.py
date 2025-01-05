import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QMainWindow
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.data_info = self.Labels()
        
        
        
    def Labels(self):
        
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
        
        names=['Title','Author','Year','Genre']
        data_info={}
        for name in names:
            field=QLineEdit(self)
            field.setPlaceholderText(f"Enter the {name} ...")
            field.setStyleSheet("font-size:30px; ")
            vbox.addWidget(field)
            data_info[name]=field
        
        vbox.addWidget(save)    
        self.setLayout(vbox)  
        return data_info 
    
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
