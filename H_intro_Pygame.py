#import library
import pygame
from pygame.locals import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('bird2.gif').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
    def move(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 800:
            self.rect.bottom = 800

class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        self.image = pygame.image.load('acorn.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(random.randint(820, 900), random.randint(0, 600)))
        #self.rect = self.surf.get_rect(center=(820, random.randint(0, 800)))
        self.speed = random.randint(1,2)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
#Initialize pygame modules
pygame.init()

#Create your screen
screen = pygame.display.set_mode((800, 800))

#Create the Player object
player = Player()

#Create the Opponent Object
opponent = Opponent()

#Set Background Color
background = pygame.Surface(screen.get_size())
background.fill((52, 54, 87))

#Group the Sprites together
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(opponent)

opponents = pygame.sprite.Group()
opponents.add(opponent)

#Create ADDOPPONENT Event
ADDOPPONENT = pygame.USEREVENT + 1

#Set a timer for the ADDOPPONENT Event to occur every 250 milliseconds
pygame.time.set_timer(ADDOPPONENT, 250)

#create game clock, create variable for frames per second
clock = pygame.time.Clock()
fps = 450



#Game Loop Logic
running = True
while running:

    #set game FPS
    clock.tick(fps)

    #for loop through the event queue
    for event in pygame.event.get():
        #Check for KEYDOWN event
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            print("Escape")
        #Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
            print("QUIT the Game")

        #Check for the ADDOPONENT Event; if required, create an instance
        elif event.type == ADDOPPONENT:
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
            
    #Draw Background
    screen.blit(background, (0, 0))
    
    #Get Pressed keys
    pressed_keys = pygame.key.get_pressed()
    
    #Update player position
    player.move(pressed_keys)
    
    #Update the opponent player
    opponent.update()

    #Update the opponent instances
    opponents.update()
    
    #Draw all Sprites on the screen
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    #Kill the Player Instance if it and an opponent collide
    if pygame.sprite.spritecollideany(player, opponents):
        player.kill()
    
    #Draw surf onto screen
    pygame.display.flip()
      
#Unintialize pygame modules
pygame.quit()

