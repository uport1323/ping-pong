from pygame import *
import pygame
from random import randint
font.init()
mixer.init()
pygame.init()
window= display.set_mode((700,500))
display.set_caption('сs2')
background = transform.scale(image.load('galaxy.jpg'),(700,500))
game = True
clock = pygame.time.Clock()
bullets = sprite.Group()
x=400
y=400
s=10
x2=randint(20,700)
y2=0
s2=10
font1 = font.SysFont('Arial',36)
mixer.music.load('space.ogg')


mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed,size_z,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_z,size_y))
        self.speed = player_speed
        self.rect= self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Play_game(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_a]and self.rect.x <700:
            self.rect.x-=10
        if keys_pressed[K_d]and self.rect.x <700:
            self.rect.x+=10
        for e in event.get():
            if e.type==QUIT:
                game = False
