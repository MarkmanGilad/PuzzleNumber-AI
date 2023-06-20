import pygame
from State import State
from constants import *
from Puzzle import Puzzle
from Graphics import Graphics
from Human_Agent import Human_Agent
pygame.init()

def main ():

    FPS = 60
    win = 
    pygame.display.set_caption('Puzzle')
        
    state = State()
    puzzle = Puzzle(state)
    #puzzle.shuffle(iteration=70)
    goal = puzzle.make_goal_state(ROWS,COLS)

    graphics = Graphics(win)
    agent = Human_Agent()
    # agent = DFS_Agent(puzzle, goal)
    run = True
    clock = pygame.time.Clock()
    graphics.draw(puzzle.state)
    pygame.display.update()

    while(run):

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False

            action = agent.get_Action(event)
            puzzle.move(action)
            pygame.time.sleep(0.02)
        
        graphics.draw(puzzle.state)
        pygame.display.update()
        
        if puzzle.state == goal:
            print("Victory")
            run = False
            pygame.time.sleep(3)
    pygame.quit()

if __name__ == '__main__':
    main()