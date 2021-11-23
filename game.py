import pygame

def main ():
    pygame.init()
    logo = pygame.image.load ("android-icon.png")
    background = pygame.image.load ("background.jpg")
    pygame.display.set_icon(logo)
    screen = pygame.display.set_mode ((640,480))
    screen.blit (background, (50,50))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
