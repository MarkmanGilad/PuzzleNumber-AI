# Environment
from constants import *
from State import State
from Action import Action
import numpy as np
import random

class Puzzle:

    def __init__(self, state:State = None):
        if state:
            self.state = state
        else:
            self.shuffle()

    def make_goal_state (self, rows=ROWS, cols=COLS):
        board = np.arange(rows*cols)
        board = board.reshape((rows, cols))
        return State(board)

    # השלם את הפונקציה הבודקת אם פעולה שנבחרה היא חוקית למצב שמתקבל 
    # הפונקציה מחזירה אמת אם היא חוקית, אחרת שקר
    def is_legal_action (self, action: Action, state:State = None):
        pass

    # השלם את הפעולה המקבלת מצב (או השמור באובייקט)
    # הפעולה מחזירה רשימה של פעולות חוקיות למצב הנתון
    def get_actions (self, state: State = None):
        pass

    # הפונקציה מקבלת פעולה ואם היא חוקית משנה את המצב של הסביבה.
    def move (self, action: Action):
        pass
        
    # הפונקציה מקבלת מצב ופעולה ומחזירה מצב החדש בהתאם לפעולה
    # שימו לב שיש להעתיק מצב חדש ולא לשנות את המצב שהתקבל
    def next_state (self, action: Action, state: State):
        pass

    def shuffle (self, state: State = None, iteration=70):
        if state is None:
            self.state = self.make_goal_state()
        path = []
        for i in range(iteration):
            actions = self.get_actions()
            action = random.choice(actions)
            self.move(action)
            path.append(action)
        return path