import pygame
import numpy as np
import time

BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (20, 20, 20)
GOING_TO_DIE_COLOR = (255, 240, 170)
ALIVE_COLOR = (255, 255, 255)


def update_state(screen, cells, size, playing=False):
    grid = np.empty((cells.shape[0], cells.shape[1]))

    for row, column in np.ndindex(cells.shape):
        nb_alive_neighbors = np.sum(cells[row - 1:row + 2, column - 1:column + 2]) - cells[row,column]

        if cells[row, column] == 0:
            color = BACKGROUND_COLOR
        else:
            color = ALIVE_COLOR

        if cells[row,column] == 1:
            if nb_alive_neighbors < 2 or nb_alive_neighbors > 3:
                if playing:
                    color = GOING_TO_DIE_COLOR
            elif 2 <= nb_alive_neighbors <= 3:
                grid[row, column] = 1
                if playing:
                    color = ALIVE_COLOR
        else:
            if nb_alive_neighbors == 3:
                grid[row, column] = 1
                if playing:
                    color = ALIVE_COLOR

        pygame.draw.rect(screen, color, (column*size, row*size, size - 1, size - 1))

    return grid