import pygame
import os
import sys
pygame.init()


class Idle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 9):
            img = pygame.image.load(os.path.join(
                'images', 'idle' + str(i) + '.png'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.idle = True
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.rate = 0

    def update(self):
        # Idle animation cycle
        if self.idle == True:
            self.frame += 1
            if self.frame > 7*ani:
                self.frame = 0
            self.image = self.images[(self.frame//ani)]


idle = Idle()
idle.rect.x = 20
idle.rect.y = 180
idle_list = pygame.sprite.Group()
idle_list.add(idle)
# animation cycles
ani = 6


def titlescreen():
    import pygame

    # Loading the background images

    background_one = pygame.image.load('background.png')
    background_two = pygame.image.load('background2.png')

    # Loading main logo and instructions

    logo = pygame.image.load('logo.png')
    instructions = pygame.image.load('instructions.png')

    # Setting variables for x-coordinates

    background_one_x = 0
    background_two_x = background_one.get_width()

    # Setting window display size

    width = background_one.get_width()
    height = background_one.get_height()
    screen = pygame.display.set_mode((width, height))

    # Initializing pygame, the clock, and setting the game caption.

    pygame.init()
    pygame.display.set_caption('Jumper Guy')
    clock = pygame.time.Clock()

    # Setting Speed
    speed = 10

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.KEYDOWN:
                stop_game = True
            if event.type == pygame.QUIT:
                exit()

        # displaying the background on the screen.
        screen.blit(background_one, [background_one_x, 0])
        screen.blit(background_two, [background_two_x, 0])

        background_one_x -= speed
        background_two_x -= speed

        if background_one_x <= -1 * background_one.get_width():
            background_one_x = background_two_x + background_two.get_width()
        if background_two_x <= -1 * background_two.get_width():
            background_two_x = background_one_x + background_one.get_width() + 1

        # Displaying main logo and instructions

        screen.blit(logo, [0, -90])
        screen.blit(instructions, [0, 90])

        # Game display
        idle_list.draw(screen)
        idle.update()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
