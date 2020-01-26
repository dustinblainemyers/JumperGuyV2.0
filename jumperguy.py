from exitscreen import exitfun
from titlescreen import titlescreen
import os
import sys
import random
import pygame
from pygame import mixer
pygame.font.init()
# music
pygame.init()
mixer.music.load('intro.wav')
mixer.music.play(-1)

# Calling the title screen

lastloc = 1000

titlescreen()


# Player class object

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 8):
            img = pygame.image.load(os.path.join(
                'images', 'run' + str(i) + '.png'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.rate = 0
        self.jumping = False
        self.longjumping = False
        self.running = True
        self.hitbox = (self.rect.x, self.rect.y, 100, 150)

    # left / right functionality if wanted later
    def control(self, x, y):
        # self.movex += x
        #  self.movey = 10
        pass

    def update(self):
        # self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.hitbox = (self.rect.x, self.rect.y, 100, 150)

        # Jump logic
        if self.jumping == True and self.rect.y > 120:
            self.rect.y -= 250
            self.rect.x += 30
            # self.rect.x += 100

        if self.rect.y < 160 and self.jumping == False:
            self.rect.y += 3
            if self.rect.x > 170:
                self.rect.x -= 5
        if self.longjumping == True and self.rect.y > 120:
            self.rect.y -= 350
            # self.rect.x += 100

        if self.rect.y < 160 and self.longjumping == False:
            self.rect.y += 1.0
            # if self.rect.x > 130:
            # self.rect.x -= 2

            # Running animation cycle
        if self.running == True:
            self.frame += 1
            if self.frame > 6*ani:
                self.frame = 0
            self.image = self.images[(self.frame//ani)]

            # Calling the title screen.
# titlescreen()


player = Player()
player.rect.x = 130
player.rect.y = 160
player_list = pygame.sprite.Group()
player_list.add(player)
# animation cycles
ani = 7

# Main game function


def main():
    # Loading the background image and setting variables for x coordinates
    background_one = pygame.image.load('background.png')
    background_two = pygame.image.load('background2.png')
    background_one_x = 0
    background_two_x = background_one.get_width()
    # Setting window display size

    WIDTH = 1000
    HEIGHT = 350
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Initiliazing pygame, setting game caption, and initializing clock.
    pygame.init()
    # music
    mixer.music.load('main.wav')
    mixer.music.play(-1)

    pygame.display.set_caption('Jumper guy')
    clock = pygame.time.Clock()

    # frame tracker to randomly put obstacles on screen
    frame_tracker = 0

    # Setting the speed of FPS limit, and speed of the background, bigger numbers mean faster speed.

    FPS = 60
    speed = 10
    # Setting score variable and font
    myfont = pygame.font.Font('8bit16.ttf', 28)

    real_score = 0
    score = 0

    class Mob(pygame.sprite.Sprite):
        def __init__(self, x_location):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('can.png')
            # self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = x_location
            self.rect.y = 225
            self.speedy = 0
            self.speedx = -10
            self.hitbox = (self.rect.x + 20, self.rect.y, 60, 100)

            # lastloc = 1000

        def update(self):

            self.rect.x += self.speedx
            self.hitbox = (self.rect.x + 20, self.rect.y, 60, 100)

            if self.rect.x < -25:
                obstacle_generation(self)

            #    if lastloc > 3000:
            #        lastloc = 1000

    def obstacle_generation(obstacle):
        global lastloc
        obstacle.rect.x = lastloc + 100
        obstacle.rect.y = 225
        lastloc = obstacle.rect.x

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()

    for i in range(1):
        m = Mob(lastloc + random.randrange(1500))
        all_sprites.add(m)
        mobs.add(m)

    # Game initialization and starting of main loop
    stop_game = False
    hitcount = 0
    while not stop_game:
        for mob in mobs:
            if (mob.hitbox[0] - 30) > player.rect.x and (mob.hitbox[0] - 30) < (player.rect.x + 50) and (player.rect.y + 150) > (mob.hitbox[1]):
                hitcount += 1
                print("\033c")
                print(mob.hitbox[1])
                print(player.hitbox[1])
                exitfun()

        player.rate += 1
        player.jumping = False
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == ord('w'):
                    player.jumping = True
                if event.key == pygame.K_LEFT:
                    player.longjumping = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.jumping = False
                if event.key == pygame.K_LEFT:
                    player.longjumping = False

            # This needs to be changed once characters and dying are implemented.
            if event.type == pygame.QUIT:
                stop_game = True
        # Game logic

        # Logic to randomly place obstacles

        if frame_tracker % 300 == 0:
            for i in range(1):
                m = Mob(lastloc + random.randrange(1500))
                all_sprites.add(m)
                mobs.add(m)

        # Drawing the moving background
        screen.blit(background_one, [background_one_x, 0])
        screen.blit(background_two, [background_two_x, 0])
        background_one_x -= speed
        background_two_x -= speed

        if background_one_x <= -1 * background_one.get_width():
            background_one_x = background_two_x + background_two.get_width()
        if background_two_x <= -1 * background_two.get_width():
            background_two_x = background_one_x + background_one.get_width() + 1
        # Adding to the score and displaying it.
        real_score += 1
        score_text = myfont.render(
            'Score = {}'.format(score), 1, (255, 255, 255))
        screen.blit(score_text, [10, 320])
        if real_score % 10 == 0:
            score += 1

        all_sprites.update()
        player_list.draw(screen)
        all_sprites.draw(screen)
        # pygame.draw.rect(screen, RED,player.hitbox,2)
        # for mob in mobs:

        #     what = pygame.draw.rect(screen,RED,mob.hitbox,2)

        pygame.display.flip()
        pygame.display.update()
        player.update()
        frame_tracker += 1

        # Game clock
        clock.tick(FPS)

    pygame.quit()
    # Calling the Exit Function.
    # exitfun()


if __name__ == '__main__':
    main()
