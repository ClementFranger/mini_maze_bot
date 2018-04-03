import player
import maze
import pygame
import os
import time

if __name__ == "__main__" :
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    ## To have a borderless maze, chose an odd width and height
    # maze = maze.Maze(31, 15, 20)
    maze = maze.Maze(199, 99, 5)

    pygame.init()

    maze.draw_maze()

    maze.dfs()

    maze.draw_maze_play()

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
