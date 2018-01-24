import player
import maze
import pygame
import os



if __name__ == "__main__" :
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    ## To have a borderles maze, chose an odd width and height
    # maze = maze.Maze(31, 15, 20)
    maze = maze.Maze(250, 125, 5)

    pygame.init()

    maze.draw_maze()
    maze.dfs()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
