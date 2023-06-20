import pygame
from Action import Action

class Human_Agent:
    
    def get_Action (self, event):
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_LEFT: return Action.LEFT
                case pygame.K_RIGHT: return Action.RIGHT
                case pygame.K_UP: return Action.UP
                case pygame.K_DOWN: return Action.DOWN
        else:
            return None