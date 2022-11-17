import pygame
import pygame.locals

"""Class that handles the field. Properties of size..."""
class Field():

    def do_something():
        pass


if __name__ == '__main__':
    pygame.init()
    running = True

    while running:
        screen = pygame.display.set_mode((600, 400))
        screen.fill((225, 225, 128))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

