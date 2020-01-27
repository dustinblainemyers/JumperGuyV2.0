import os
import sys
import pygame


# sprite for exit screen


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ground1.png')
        self.rect = self.image.get_rect()


ground = Ground()
ground.rect.x = 220
ground.rect.y = 200
ground_list = pygame.sprite.Group()
ground_list.add(ground)


def exitfun():
    import pygame
    from pygame import mixer
    # music
    mixer.music.load('failed.wav')
    mixer.music.play(-1)

    # from tryagain import tryagain

    # Loading the background image and setting variables for x coordinates

    background_one = pygame.image.load('background.png')
    background_two = pygame.image.load('background2.png')

    # loading the death logo and death instructions.

    death = pygame.image.load('death.png')

    # Setting background x-coordinate variables.

    background_one_x = 0
    background_two_x = background_one.get_width()

    # Setting window display size

    width = background_one.get_width()
    height = background_one.get_height()
    screen = pygame.display.set_mode((width, height))

    # initializing pygame, the clock, and setting game caption.
    pygame.init()
    pygame.display.set_caption('Jumper Guy')
    clock = pygame.time.Clock()

    # Setting Speed
    speed = 10

    # Setting font

    myfont = pygame.font.Font('8bit16.ttf', 28)
    # score_text = myfont.render('final score =  {}'.format(score), 1, (255,255,255))

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    

                    import jumperguy

                    jumperguy.main()

            if event.type == pygame.QUIT:
                exit()

        # Draw background
        screen.blit(background_one, [background_one_x, 0])
        screen.blit(background_two, [background_two_x, 0])

        background_one_x -= speed
        background_two_x -= speed

        if background_one_x <= -1 * background_one.get_width():
            background_one_x = background_two_x + background_two.get_width()
        if background_two_x <= -1 * background_two.get_width():
            background_two_x = background_one_x + background_one.get_width() + 1

        # Adding the exit screen logo, score, and text.

        screen.blit(death, [0, 50])

        # Game display
        ground_list.draw(screen)
        pygame.display.update()
        clock.tick(60)
