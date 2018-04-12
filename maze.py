import numpy
import pygame
import random
import time


# 0 is free cells, 1 is wall cells and 0.5 is visited cells
class Maze:
    # width and height are in cells while cell_size is in pixel.
    def __init__(self, width=100, height=50, cell_size=10,
                 free_cell_color=(255, 255, 255),
                 visited_cell_color=(0, 0, 255),
                 wall_cell_color=(0, 0, 0)):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.free_cell_color = free_cell_color
        self.visited_cell_color = visited_cell_color
        self.wall_cell_color = wall_cell_color
        self.cells = numpy.ones((self.height, self.width))
        self.display = pygame.display.set_mode((self.width * self.cell_size, self.height * self.cell_size))

    def color_cell(self, cell):
        color = None
        if self.cells[cell] == 0:
            color = self.free_cell_color
        if self.cells[cell] == 0.5:
            color = self.visited_cell_color
        if self.cells[cell] == 1:
            color = self.wall_cell_color
        return color

    # x is the matrix column index
    # y is the matrix row index
    # so matrix index are cell = (y, x)
    # pygame draw x from left to right and y from top to bottom
    def draw_cell(self, cell):
        pygame.draw.rect(self.display,
                         self.color_cell(cell),
                         (tuple(self.cell_size * c for c in cell)[::-1], (self.cell_size, self.cell_size)))

    def change_cell(self, cell, value):
        self.cells[cell] = value
        self.draw_cell(cell)

    def draw_maze(self):
        for cell in numpy.ndindex(self.height, self.width):
            self.draw_cell(cell)

    def draw_maze_play(self):
        self.cells[self.cells != 1] = 0
        self.draw_maze()

    #################################################################################################################
    #                                               DFS GENERATION                                                  #
    #################################################################################################################

    def unvisited_cell_neighbors(self, cell):
        neighbors = []
        west = []
        north = []
        east = []
        south = []
        if cell[1] > 1 and self.cells[cell[0], cell[1] - 2] == 1:
            west.extend([(cell[0], cell[1] - 1), (cell[0], cell[1] - 2)])
        if cell[1] < self.width - 2 and self.cells[cell[0], cell[1] + 2] == 1:
            east.extend([(cell[0], cell[1] + 1), (cell[0], cell[1] + 2)])
        if cell[0] > 1 and self.cells[cell[0] - 2, cell[1]] == 1:
            north.extend([(cell[0] - 1, cell[1]), (cell[0] - 2, cell[1])])
        if cell[0] < self.height - 2 and self.cells[cell[0] + 2, cell[1]] == 1:
            south.extend([(cell[0] + 1, cell[1]), (cell[0] + 2, cell[1])])
        neighbors.extend([west, north, east, south])
        neighbors = [x for x in neighbors if x != []]
        return neighbors

    # If wall is a cell, then do step of 2
    # Credit to https://github.com/The-Ofek-Foundation/Maze
    def dfs(self):
        visited = []
        current_cell = (0, 0)
        visited.append(current_cell)
        self.change_cell(current_cell, 0)

        while visited:
            neighbors = self.unvisited_cell_neighbors(current_cell)
            if neighbors:
                next_cell = random.choice(neighbors)
                self.change_cell(next_cell[0], 0)
                self.change_cell(next_cell[1], 0)
                visited.extend([next_cell[0], next_cell[1]])
                current_cell = next_cell[1]
            else:
                if len(visited) > 1:
                    self.change_cell(visited[-1], 0.5)
                    del visited[-1]
                    self.change_cell(visited[-1], 0.5)
                    del visited[-1]
                    current_cell = visited[-1]
                else:
                    self.change_cell(visited[-1], 0.5)
                    current_cell = visited[-1]
                    del visited[-1]
            # Uncomment to see real time progression
            # time.sleep(0.1)
            # pygame.display.update()
