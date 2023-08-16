import sys

import pygame

screen = pygame.display.set_mode((640, 480))

x=50
y=50

rectangle = pygame.Rect(x, y, 100, 50)
pygame.draw.rect(screen, "white", rectangle, 0)

while True:
    pygame.display.flip()
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

           # pygame.draw.rect(screen, "white", rectangle, 0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rectangle.move_ip(0, -5)
                #print("Вверх")
            elif event.key == pygame.K_DOWN:
                rectangle.move_ip(0, 5)
                #print("Вниз")
            elif event.key == pygame.K_LEFT:
                rectangle.move_ip(-5,0)
            elif event.key == pygame.K_RIGHT:
                rectangle.move_ip(5, 0)

    pygame.draw.rect(screen, "white", rectangle, 0)
    pygame.display.flip()
