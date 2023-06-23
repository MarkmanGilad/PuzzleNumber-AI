# Environment
from typing import Any
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
        self.goal = self.make_goal_state()

    def make_goal_state (self, rows=ROWS, cols=COLS):
        board = np.arange(rows*cols)
        board = board.reshape((rows, cols))
        return State(board)

    # השלם את הפונקציה הבודקת אם פעולה שנבחרה היא חוקית למצב שמתקבל 
    # הפונקציה מחזירה אמת אם היא חוקית, אחרת שקר
    def is_legal_action (self, action: Action, state:State):
        if action is None:
            return False
        blank_row, blank_col = state.get_blank_pos()
        match action:
            case Action.UP: return blank_row > 0
            case Action.DOWN: return blank_row < state.rows-1
            case Action.RIGHT: return blank_col < state.cols-1
            case Action.LEFT : return blank_col > 0        

    # השלם את הפעולה המקבלת מצב (או השמור באובייקט)
    # הפעולה מחזירה רשימה של פעולות חוקיות למצב הנתון
    def get_actions (self, state: State):
        actions = []
        if self.is_legal_action(Action.DOWN, state): 
            actions.append(Action.DOWN)
        if self.is_legal_action(Action.RIGHT, state): 
            actions.append(Action.RIGHT)
        if self.is_legal_action(Action.UP, state): 
            actions.append(Action.UP)
        if self.is_legal_action(Action.LEFT, state): 
            actions.append(Action.LEFT)
        return actions        

    # הפונקציה מקבלת פעולה ואם היא חוקית משנה את המצב של הסביבה.
    def move (self, action: Action):
        if not self.is_legal_action(action, self.state):
            return
        state = self.state
        blank_row, blank_col = state.get_blank_pos()
        target_row, target_col = blank_row, blank_col
        match action:
            case Action.UP: target_row -=1
            case Action.DOWN: target_row +=1
            case Action.RIGHT: target_col +=1
            case Action.LEFT : target_col -=1
        state.board[blank_row, blank_col], state.board[target_row, target_col] = state.board[target_row, target_col], state.board[blank_row, blank_col]
        state.blank_pos = target_row, target_col
        
    # הפונקציה מקבלת מצב ופעולה ומחזירה מצב החדש בהתאם לפעולה
    # שימו לב שיש להעתיק מצב חדש ולא לשנות את המצב שהתקבל
    def next_state (self, action: Action, state: State):
        legal = self.is_legal_action(action, state) 
        if not self.is_legal_action(action, state):
            return
        state = state.copy()
        blank_row, blank_col = state.get_blank_pos()
        target_row, target_col = blank_row, blank_col
        match action:
            case Action.UP: target_row -=1
            case Action.DOWN: target_row +=1
            case Action.RIGHT: target_col +=1
            case Action.LEFT : target_col -=1
        state.board[blank_row, blank_col], state.board[target_row, target_col] = state.board[target_row, target_col], state.board[blank_row, blank_col]
        state.blank_pos = target_row, target_col
        return state

    def shuffle (self, state: State = None, iteration=100):
        if state is None:
            state = self.make_goal_state()
            self.state = state
        path = []
        for i in range(iteration):
            actions = self.get_actions(state)
            action = random.choice(actions)
            self.move(action)
            path.append(action)
        return path
    
    # gets state, action; return tuple of new_state, reward

    def __call__(self, state: State, action:Action):
        next_state = self.next_state(action, state)
        reward = int(next_state == self.goal) 
        return next_state, reward