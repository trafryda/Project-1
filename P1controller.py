from PyQt5.QtWidgets import *
from P1gui import Ui_MainWindow
import random as selector
from PyQt5 import QtCore, QtGui, QtWidgets


def computer_selection():
    computer_num = selector.randint(1, 3)
    if computer_num == 1:
        comp_character = 'Rock'
    elif computer_num == 2:
        comp_character = 'Paper'
    else:
        comp_character = 'Scissors'

    return comp_character

def logic(user,computer):
    if user == computer:
        return 'Tie'
    elif computer == 'Rock' and user == 'Scissors':
        return 'Computer Rock, User Scissors'
    elif computer == 'Scissors' and user == 'Paper':
        return 'Computer Scissors, User Paper'
    elif computer == 'Paper' and user == 'Rock':
        return 'Computer Paper, User Rock'
    elif computer == 'Scissors' and user == 'Rock':
        return 'Computer Scissors, User Rock'
    elif computer == 'Paper' and user == 'Scissors':
        return 'Computer paper, User Scissors'
    elif computer == 'Rock' and user == 'Paper':
        return 'Computer Rock, User paper'



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.games_played = 0
        self.comp_wins = 0
        self.user_wins = 0
        self.playButton.clicked.connect(lambda: self.play())


    def play(self):


        self.computer_character = computer_selection()
        if self.computer_character == 'Rock':
            self.picture2.setPixmap(QtGui.QPixmap("../Downloads/Rock_pic.png"))
            self.picture2.setScaledContents(True)
        elif self.computer_character == 'Paper':
            self.picture2.setPixmap(QtGui.QPixmap("../Downloads/Paper.png"))
            self.picture2.setScaledContents(True)
        else:
            self.picture2.setPixmap(QtGui.QPixmap("../Downloads/Scissors1.png"))
            self.picture2.setScaledContents(True)
        self.games_played += 1



        if self.rockButton.isChecked():
            self.user_character = 'Rock'
            self.picture1.setPixmap(QtGui.QPixmap("../Downloads/Rock2.png"))
            self.picture1.setScaledContents(True)
        if self.paper_button.isChecked():
            self.user_character = 'Paper'
            self.picture1.setPixmap(QtGui.QPixmap("../Downloads/Paper.png"))
            self.picture1.setScaledContents(True)
        if self.scissorButton.isChecked():
            self.user_character = 'Scissors'
            self.picture1.setPixmap(QtGui.QPixmap("../Downloads/Scissor2.png"))
            self.picture1.setScaledContents(True)

        self.group.setExclusive(False)
        self.rockButton.setChecked(False)
        self.scissorButton.setChecked(False)
        self.paper_button.setChecked(False)
        self.group.setExclusive(True)

        self.game = logic(self.user_character, self.computer_character)

        if self.game == 'Tie':
            self.welcomeLabel.setText("Computer is {}. You are {}. You tie.".format(self.computer_character, self.user_character))
            self.label.setText('Computer Wins: {}              User Wins: {}'.format(self.comp_wins, self.user_wins))


        elif self.game == 'Computer Rock, User Scissors':
            self.welcomeLabel.setText("Computer is {}. You are {}. You lose.".format(self.computer_character, self.user_character))
            self.comp_wins += 1
            self.label.setText('Computer Wins: {}              User Wins: {}'.format(self.comp_wins, self.user_wins))


        elif self.game == 'Computer Scissors, User Paper':
            self.welcomeLabel.setText("Computer is {}. You are {}. You lose.".format(self.computer_character, self.user_character))
            self.comp_wins += 1
            self.label.setText('Computer Wins: {}              User Wins: {}'.format(self.comp_wins, self.user_wins))


        elif self.game == 'Computer Paper, User Rock':
            self.welcomeLabel.setText("Computer is {}. You are {}. You lose.".format(self.computer_character, self.user_character))
            self.comp_wins += 1
            self.label.setText('Computer Wins: {}              User Wins: {}'.format(self.comp_wins, self.user_wins))



        elif self.game == 'Computer Scissors, User Rock':
            self.welcomeLabel.setText("Computer is {}. You are {}. You win.".format(self.computer_character, self.user_character))
            self.comp_wins += 1
            self.label.setText('Computer Wins: {}              User Wins: {}'.format(self.comp_wins, self.user_wins))


        elif self.game == 'Computer paper, User Scissors':
            self.welcomeLabel.setText("Computer is {}. You are {}. You win.".format(self.computer_character, self.user_character))
            self.user_wins += 1
            self.label.setText('Computer Wins: {}              User Wins: {}'.format(self.comp_wins, self.user_wins))


        elif self.game == 'Computer Rock, User paper':
            self.welcomeLabel.setText("Computer is {}. You are {}. You win.".format(self.computer_character, self.user_character))
            self.user_wins += 1
            self.label.setText('Computer Wins: {}              User Wins: {}'.format(self.comp_wins, self.user_wins))


        if self.games_played == 2:
            if self.comp_wins == 2:
                self.welcomeLabel.setText('Game Over! The computer has won the Series :(')
                self.playButton.hide()
                self.scissorButton.hide()
                self.rockButton.hide()
                self.paper_button.hide()
                self.InstructionsButton.setText('')
                self.picture1.hide()
                self.picture2.setPixmap(QtGui.QPixmap("../Downloads/thankyou.jpeg"))
            elif self.user_wins == 2:
                self.welcomeLabel.setText('Game Over! You have won the Series :)')
                self.playButton.hide()
                self.scissorButton.hide()
                self.rockButton.hide()
                self.paper_button.hide()
                self.InstructionsButton.setText('')
                self.picture1.hide()
                self.picture2.setPixmap(QtGui.QPixmap("../Downloads/thankyou.jpeg"))


        if self.games_played == 3:
            if self.comp_wins > self.user_wins:
                self.welcomeLabel.setText('Game Over! The computer has won the Series :(')
                self.playButton.hide()
                self.scissorButton.hide()
                self.rockButton.hide()
                self.paper_button.hide()
                self.InstructionsButton.setText('')
                self.picture1.hide()
                self.picture2.setPixmap(QtGui.QPixmap("../Downloads/thankyou.jpeg"))

            elif self.comp_wins < self.user_wins:
                self.welcomeLabel.setText('Game Over! You have won the Series :)')
                self.playButton.hide()
                self.scissorButton.hide()
                self.rockButton.hide()
                self.paper_button.hide()
                self.InstructionsButton.setText('')
                self.picture1.hide()
                self.picture2.setPixmap(QtGui.QPixmap("../Downloads/thankyou.jpeg"))


            else:
                self.welcomeLabel.setText('Game Over! The series ends in a draw :)')
                self.playButton.hide()
                self.scissorButton.hide()
                self.rockButton.hide()
                self.paper_button.hide()
                self.InstructionsButton.setText('')
                self.picture1.hide()
                self.picture2.setPixmap(QtGui.QPixmap("../Downloads/thankyou.jpeg"))





