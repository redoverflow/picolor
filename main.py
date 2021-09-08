import pygame
import settings

def main():
    pygame.init()

    pygame.display.set_caption("picolor")
    screen = pygame.display.set_mode((640,480))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    

    screen.fill((255, 255, 255))


if __name__=="__main__":
    main()