import pygame
from State import State
from constants import *
from Puzzle import Puzzle
from Graphics import Graphics
from Human_Agent import Human_Agent
from AI_Agent import AI_Agent

pygame.init()

def main ():
        
    puzzle = Puzzle()
    goal = puzzle.make_goal_state(ROWS,COLS)
    
    graphics = Graphics()
    # agent = Human_Agent()
    agent = AI_Agent(puzzle)
    # agent.Init_Value_Table()
    # agent.Value_Iteration()
    agent.load_v()

    run = True
    clock = pygame.time.Clock()
    graphics.draw(puzzle.state)
    pygame.display.update()
    count = 0
    while(run):

        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False

        action = agent.get_Action(events)
        count += 1
        puzzle.move(action)
        graphics.draw(puzzle.state)
        pygame.display.update()
        print(count, end = '\r')
        if puzzle.state == goal:
            print(f"Victory in {count}")
            # run = False
            puzzle.shuffle()
            count = 0
            pygame.time.wait(2000)
    pygame.quit()

if __name__ == '__main__':
    main()