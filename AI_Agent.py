from Action import Action
from itertools import permutations
import numpy as np
import torch
from State import State
from Puzzle import Puzzle
import pygame

PATH = 'Data/V_2.pth'
gamma = 0.95

class AI_Agent:
    def __init__(self, env: Puzzle) -> None:
        self.V = dict()
        self.env : Puzzle = env

    def get_Action (self, events):
        state =  self.env.state
        best_value = -1
        best_action = None
        for action in self.env.get_actions(state):
            next_state, reward = self.env(state, action)
            next_value = reward + self.get_V(next_state)
            if next_value > best_value:
                best_value = next_value
                best_action = action
        pygame.time.wait(300)
        return best_action
    
    def Init_Value_Table (self):
        # get all states as tuple
        states = permutations([0,1,2,3,4,5,6,7,8])
        for s in states:
            self.V[s] = 0
        self.save_v()

    def Value_Iteration(self):
        accuracy = 0.001
        acc = 1
        epochs = 0
        while acc > accuracy:
            epochs += 1
            acc = 0
            for key , old_value in self.V.items():
                best_value = -1000
                state = self.key_to_state(key)
                if state == self.env.goal:
                    continue
                for action in self.env.get_actions(state):
                    new_state, reward = self.env(state,action)
                    new_value = reward + gamma*self.get_V(new_state)
                    best_value = max(best_value, new_value)
                    if best_value == 1:
                        i=1
                self.set_V(state, best_value)
                acc = max(acc, abs(old_value - best_value))
                if best_value > 0 :
                    print (f'{key} \t {old_value:.3f} \t {best_value:.3f} \t acc {acc} \t ephocs {epochs}')
                

        self.save_v()

    def save_v (self):
        torch.save(self.V, PATH)

    def load_v (self):
        self.V = torch.load(PATH)
    
    def get_V(self, state: State):
        key = tuple(state.board.flatten())
        return self.V[key]
    
    def set_V(self,state: State, value):
        arr = state.board.flatten()
        key = tuple(arr)
        self.V[key] = value

    def key_to_state(self, key):
        board = np.asarray(key).reshape([3,3])
        return State(board)

