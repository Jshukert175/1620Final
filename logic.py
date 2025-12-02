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
        vote_id = int(self.input_id.text())
        try:
            if len(vote_id) != 4:
                raise ValueError
        except ValueError:
            self.label_name.setText(text="Invalid ID")
            return
        if self.jane.isChecked():
            vote = "Jane"
        elif self.john.isChecked():
            vote = "John"
        else:
            vote = "Vote for a candidate"

        if self.votes.checkedButton() is not None:
            self.votes.setExclusive(False)
            self.votes.checkedButton().setChecked(False)
            self.votes.setExclusive(True)

        with open('data.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow([vote_id, vote])

        self.vote_id.clear()