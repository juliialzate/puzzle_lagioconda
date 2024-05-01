import pygame
from cuadros import Puzzle  # Import cuadros module

pygame.init()

ejecutar = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False

    puzzle = Puzzle() 
    puzzle.run() 

    pygame.display.update()

    if not ejecutar:
        pygame.quit()  
