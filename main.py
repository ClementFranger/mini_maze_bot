import player
import maze
import pygame

if __name__ == "__main__" :

    ## To have a borderles maze, chose an odd width and height
    maze = maze.Maze(101, 51)

    pygame.init()

    maze.draw_maze()
    maze.dfs()
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
