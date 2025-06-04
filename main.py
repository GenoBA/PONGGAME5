#Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 480
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (131, 10, 245)

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 20
        self.height = 80
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -15
        if keystate[pygame.K_s]:
            self.speedy = 15
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        self.rect.y += self.speedy

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 20
        self.height = 80
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-self.width
        self.rect.y = 200
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -15
        if keystate[pygame.K_DOWN]:
            self.speedy = 15
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        self.rect.y += self.speedy

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 20
        self.height = 20
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH//2
        self.rect.y = HEIGHT//2
        self.speedy = 1
        self.speedx = -4

    def update(self):
        if self.rect.left <= 0:
            self.speedx = -1*self.speedx
        if self.rect.bottom >= HEIGHT:
            self.speedy = -1*self.speedy
        if self.rect.right >= WIDTH:
            self.speedx = -1*self.speedx
        if self.rect.top <= 0:
            self.speedy = -1*self.speedy
        self.rect.x += self.speedx
        self.rect.y += self.speedy


# initialize pygame and create window
pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()

left_player = Player1()
all_sprites.add(left_player)
right_player = Player2()
all_sprites.add(right_player)

gameball = Ball()
all_sprites.add(gameball)
balls.add(gameball)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    hit_left_paddle = pygame.sprite.spritecollide(left_player,balls,False)
    if hit_left_paddle:
        gameball.speedx = -1*gameball.speedx

    hit_right_paddle = pygame.sprite.spritecollide(right_player, balls, False)
    if hit_right_paddle:
        gameball.speedx = -1 * gameball.speedx

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()