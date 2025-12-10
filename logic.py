from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Method to initialize the main window
        """
        super().__init__()
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda : self.submit())

    def submit(self):
        """
        Method to submit vote
        :return: vote and vote_id
        """
        vote_id = self.input_id.text()
        try:
            if len(vote_id) != 4:
                raise ValueError
            if vote_id.isdigit() == False:
                raise TypeError
        except ValueError:
            self.label_name.setText("Invalid ID")
            self.label_name.setStyleSheet("color: red")
            return
        except TypeError:
            self.label_name.setText("Insert a number")
            self.label_name.setStyleSheet("color: red")
            return

        vote = None
        if self.jane.isChecked():
            vote = "Jane"
        elif self.john.isChecked():
            vote = "John"
        else:
            self.label_name.setText("Vote for a candidate")
            self.label_name.setStyleSheet("color: red")
            return

        radio = self.votes.checkedButton()
        if radio:
            self.votes.setExclusive(False)
            radio.setChecked(False)
            self.votes.setExclusive(True)


        with open('data.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow([vote_id, vote])

        with open('data.csv', 'r', newline='') as csvread:
            reader = csv.reader(csvread)
            voters = []
            for row in reader:
                voters.append(row[0])
            for v in voters:
                if voters.count(v) > 1:
                    self.label_name.setText("Already Voted")
                    self.label_name.setStyleSheet("color: red")
                else:
                    self.input_id.clear()
                    self.label_name.setText("Submitted")
                    self.label_name.setStyleSheet("color: green")
                    self.input_id.setFocus()
