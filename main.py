import pygame
import numpy as np
import time

BACKGROUND_COLOR = (50, 50, 50)
GRID_COLOR = (20, 20, 20)
GOING_TO_DIE_COLOR = (110, 110, 110)
ALIVE_COLOR = (255, 255, 255)


def update_state(screen, cells, size, nb_generation, playing=False):
    grid = np.zeros((cells.shape[0], cells.shape[1]))

    for row, column in np.ndindex(cells.shape):
        nb_alive_neighbors = np.sum(cells[row - 1:row + 2, column - 1:column + 2]) - cells[row, column]

        if cells[row, column] == 0:
            color = BACKGROUND_COLOR
        else:
            color = ALIVE_COLOR

        if cells[row, column] == 1:
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

        pygame.draw.rect(screen, color, (column * size, row * size, size - 1, size - 1))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Generation: {int(nb_generation)}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    return grid


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))

    cells = np.zeros((80, 100))
    nb_generations = 0

    screen.fill(GRID_COLOR)

    update_state(screen, cells, 10, nb_generations)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update_state(screen, cells, 10, nb_generations)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                cells[position[1] // 10, position[0] // 10] = 1
                update_state(screen, cells, 10, nb_generations)
                pygame.display.update()
            if pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                cells[position[1] // 10, position[0] // 10] = 0
                update_state(screen, cells, 10, nb_generations)
                pygame.display.update()

        screen.fill(GRID_COLOR)

        if running:
            cells = update_state(screen, cells, 10, nb_generations, playing=True)
            nb_generations += 0.5
            pygame.display.update()

        time.sleep(0.0001)


if __name__ == "__main__":
    main()
