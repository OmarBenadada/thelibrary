import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.initUI()

    def initUI(self):
        label = QLabel("Menu", self)
        label.setFont(QFont("Arial", 28))  
        label.setAlignment(Qt.AlignHCenter )
        label.setStyleSheet("font-weight: bold; color: #333333;")

        # Button labels and corresponding methods
        button_labels = [
            "Initialiser Tableau",
            "Afficher",
            "Ajouter Étudiant",
            "Rechercher Étudiant",
            "Calculer Moyenne Générale",
            "Supprimer",
        ]

        fonctions = [
            self.Initialiser_Tableau,
            self.afficher,
            self.Ajouter_Etudiant,
            self.Rechercher_Etudiant,
            self.Calculer_Moyenne_Generale,
            self.Supprimer,
        ]

        # Layout for buttons
        layout = QVBoxLayout()
        layout.addWidget(label)

        for label_text, fonction in zip(button_labels, fonctions):
            button = QPushButton(label_text, self)
            button.setFont(QFont("Arial", 16))  
            button.setStyleSheet("""
                QPushButton {
                    background-color:rgba(255, 255, 255, 0.5);
                    color: black;
                    font-size: 25px;
                    border: 2px solid #0078D7;
                    border-radius: 20px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color:rgb(130, 226, 255);
                    color: white;
                }
            """)
            button.setMinimumHeight(70)
            button.setMaximumHeight(180)# Minimum button height
            layout.addWidget(button)

            # Connect button to its function
            button.clicked.connect(fonction)

        # Set layout as the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # Placeholder methods for each button
    def Initialiser_Tableau(self):
        print("Initializing table...")

    def afficher(self):
        print("Displaying data...")

    def Ajouter_Etudiant(self):
        print("Adding student...")

    def Rechercher_Etudiant(self):
        print("Searching for student...")

    def Calculer_Moyenne_Generale(self):
        print("Calculating general average...")

    def Supprimer(self):
        print("Deleting data...")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
