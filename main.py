import pygame
import random

WIDTH = 620
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (131, 10, 245)

font_name = pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y,color):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 20
        self.height = 80
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200
        self.speedy = 0
        self.score1 = 0

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
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-self.width
        self.rect.y = 200
        self.speedy = 0
        self.score2 = 0

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
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH//2
        self.rect.y = HEIGHT//2
        self.speedy = random.randint(3,8)
        self.speedx = random.randint(3,8)
        horiz = random.choice(["left", "right"])
        if horiz == "left":
            self.speedx = -1 * self.speedx
        vert = random.choice(["up", "down"])
        if vert == "up":
            self.speedy = -1*self.speedy

    def update(self):
        # if self.rect.left <= 0:
        #     self.speedx = -1*self.speedx
        if self.rect.bottom >= HEIGHT:
            self.speedy = -1*self.speedy
        # if self.rect.right >= WIDTH:
        #     self.speedx = -1*self.speedx
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
new_ball = False
gameover = False
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
        gameball.speedx += 1

    hit_right_paddle = pygame.sprite.spritecollide(right_player, balls, False)
    if hit_right_paddle:
        gameball.speedx = -1 * gameball.speedx
        gameball.speedx += -1
    if gameball.rect.right <=0:
        right_player.score2 +=1
        gameball.kill()
        if right_player.score2>=11:
            right_player.score2 = 11
            gameover=True
        else:
            new_ball = True

    if gameball.rect.left >=WIDTH:
        left_player.score1 +=1
        gameball.kill()
        if left_player.score1>=11:
            left_player.score1 = 11
            gameover=True
        else:
            new_ball = True
    if new_ball == True:
        gameball = Ball()
        all_sprites.add(gameball)
        balls.add(gameball)
        new_ball = False
    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    draw_text(screen,'Pong',32,WIDTH//2,10,'Black')
    draw_text(screen, str(left_player.score1), 32, WIDTH // 4, 20, 'RED')
    draw_text(screen, str(right_player.score2), 32, 3*WIDTH // 4, 20, 'BLUE')
    if gameover == True:
        if left_player.score1>=11:
            draw_text(screen,"Left Player Wins!!!",32,WIDTH//2,HEIGHT//2,RED)
        else:
            draw_text(screen,"Right Player Wins!!!",32,WIDTH//2,HEIGHT//2,BLUE)
    pygame.display.flip()

pygame.quit()