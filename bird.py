import sys
from PyQt5.QtWidgets import QApplication,QTextEdit,QVBoxLayout,QWidget,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt




class MainWindow(QWidget):
    def __init__(self,thecontent=None,thetitle=None):
        super().__init__()
        self.setGeometry(200, 200, 700, 700)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        
        thecontent=thecontent
        thetitle=thetitle
        
        with open(thecontent,"r")as file:
            thestory=file.read()
            
        label_for_title=QLabel(thetitle,self)
        label_for_title.setAlignment(Qt.AlignHCenter )
        label_for_title.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color:rgb(255, 255, 255);
            background-color:rgb(0, 72, 255);
            padding: 20px;
            border-radius: 15px;
            border: 2px solid rgb(0, 72, 255);
        """)
        
        spac_for_reading = QTextEdit()
        spac_for_reading.setPlainText(thestory)
        spac_for_reading.setStyleSheet("font-size: 20px;")
        spac_for_reading.setReadOnly(True)

        QV=QVBoxLayout()
        
        QV.addWidget(label_for_title)
        QV.addWidget(spac_for_reading)
        

        self.setLayout(QV)

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
