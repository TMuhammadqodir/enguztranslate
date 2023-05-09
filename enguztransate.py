import sys

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QListWidget


class MainWin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(700,500)
        self.h_box = QHBoxLayout()
        self.v_box1 = QVBoxLayout()
        self.setStyleSheet("background: #3EC5CA")

        self.btn1 = QPushButton()
        self.v_box1.addWidget(self.btn1)
        self.btn2 = QPushButton()
        self.v_box1.addWidget(self.btn2)
        self.btn3 = QPushButton('Exit')
        self.v_box1.addWidget(self.btn3)

        self.steelbutton(self.btn1,self.btn2,self.btn3)

        self.h_box.addLayout(self.v_box1)
        self.setLayout(self.h_box)

        self.btn2.setFixedWidth

        self.btn3.clicked.connect(self.exit)

    def setNameBtn(self, btn1, btn2):
        self.btn1.setText(btn1)
        self.btn2.setText(btn2)

    def exit(self):
        self.close()
        self.file.close()
        
    def steelbutton(self, *temp):
        for i in temp:
            i.setStyleSheet('background: red')
            i.setFixedHeight(80)
            i.setFixedWidth(200)
    
    def steelLineEdit(self, *temp):
        for i in temp:
            i.setStyleSheet('background: orange')
            i.setFixedHeight(80)
            i.setFixedWidth(450)
    
        

class SearchPage(MainWin):

    def __init__(self) -> None:
        super().__init__()
        self.v_box2 = QVBoxLayout()

        self.setNameBtn('Add new word', 'List of words')

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText('Enter word...')
        self.steelLineEdit(self.search_edit)
        self.v_box2.addWidget(self.search_edit)

        self.search_ledit = QLineEdit()
        self.v_box2.addWidget(self.search_ledit)

        self.search_btn = QPushButton('Search')
        self.search_btn.setStyleSheet("background: green")
        self.v_box2.addWidget(self.search_btn)

        self.steelLineEdit(self.search_ledit, self.search_btn)
        self.search_ledit.setStyleSheet('background: #33DDF1')
        self.h_box.addLayout(self.v_box2)        

        self.btn1.clicked.connect(self.showAddNewWord)
        self.btn2.clicked.connect(self.showListOfWords)
        self.search_btn.clicked.connect(self.SearchWord)

    def showAddNewWord(self):

        self.close()
        self.win = AddNewWordPage()
        self.win.show()

    def showListOfWords(self):

        self.close()
        self.win = ListOfWordsPage()
        self.win.show()

        
    def SearchWord(self):
        with open("enguzdictionary.txt", 'r') as file:
            temp=file.read().split('\n')[:-1]
            k=0
            for i in temp:
                i=i.split(',')
                if i[0].lower()==self.search_edit.text().lower():
                    self.search_ledit.setText(i[1])
                    k=1
                    break
                elif i[1].lower()==self.search_edit.text().lower():
                    self.search_ledit.setText(i[0])
                    k=1
                    break
            if k==0:
                self.search_ledit.setText('Topilmadi!')
        

class AddNewWordPage(MainWin):

    def __init__(self) -> None:
        
        super().__init__()
        self.v_box2 = QVBoxLayout()

        self.setNameBtn('Search a word', 'List of words')

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText('Enter an english word...')
        self.v_box2.addWidget(self.eng_edit)

        self.uzb_edit = QLineEdit()
        self.uzb_edit.setPlaceholderText('Enter an uzbek word...')
        self.v_box2.addWidget(self.uzb_edit)        

        self.steelLineEdit(self.eng_edit, self.uzb_edit)

        self.add_btn = QPushButton('Add word')
        self.add_btn.setStyleSheet("background: green")
        self.add_btn.setFixedHeight(80)
        self.add_btn.setFixedWidth(450)
        self.v_box2.addWidget(self.add_btn)

        self.h_box.addLayout(self.v_box2)
        
        self.btn1.clicked.connect(self.ShowSearchPage)
        self.btn2.clicked.connect(self.ShowListOfWordsPage)
        self.add_btn.clicked.connect(self.AddNewWord)
        
    def ShowSearchPage(self):
        self.close()
        self.win=SearchPage()
        self.win.show()   
        
    def ShowListOfWordsPage(self):
        self.close()
        self.win=ListOfWordsPage()
        self.win.show()
        
        
    def AddNewWord(self):
        with open("enguzdictionary.txt", 'a') as file:
            if len(self.eng_edit.text())>0 and len(self.uzb_edit.text())>0:
                file.write(f"{self.eng_edit.text()},{self.uzb_edit.text()}\n")
                self.eng_edit.clear()
                self.uzb_edit.clear()
        


class ListOfWordsPage(MainWin):

    def __init__(self) -> None:

        super().__init__()
        self.v_box2 = QVBoxLayout()
        self.v_box3 = QVBoxLayout()

        self.setNameBtn('Search a word', 'Add a word')

        self.eng_label = QLabel('English')
        self.eng_label.setStyleSheet("color: #035A0C")
        self.eng_qlw = QListWidget()
        self.eng_qlw.setStyleSheet("background: orange")

        self.v_box2.addWidget(self.eng_label)
        self.v_box2.addWidget(self.eng_qlw)

        self.uzb_label = QLabel('Uzbek')
        self.uzb_label.setStyleSheet("color: #035A0C")
        self.uzb_qlw = QListWidget()
        self.openfile()
        self.uzb_qlw.setStyleSheet("background: orange")

        self.v_box3.addWidget(self.uzb_label)
        self.v_box3.addWidget(self.uzb_qlw)

        self.h_box.addLayout(self.v_box2)
        self.h_box.addLayout(self.v_box3)        
    
        self.btn1.clicked.connect(self.ShowSearchPage)
        self.btn2.clicked.connect(self.AddNewWordPage)
            
    def ShowSearchPage(self):
        self.close()
        self.win=SearchPage()
        self.win.show()   
        
    def AddNewWordPage(self):
        self.close()
        self.win=AddNewWordPage()
        self.win.show()    
        
    def openfile(self):
        try:    
            with open("enguzdictionary.txt", 'r') as file:
                temp=file.read().split('\n')[:-1]
                for i in temp:
                    i=i.split(',')
                    self.eng_qlw.addItem(i[0])
                    self.uzb_qlw.addItem(i[1])
        except Exception as err: print(err)



app = QApplication([])
win = SearchPage()
win.show()
sys.exit(app.exec_())