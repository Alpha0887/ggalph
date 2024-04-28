#Создай собственный Шутер!
from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('pygame window')
table = transform.scale(image.load("table.jpg"), (700, 500))
app = True
finish = False
clock = time.Clock()
FPS = 60
from time import time as timer  
class GameSprite(sprite.Sprite):

#конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
#метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):

  #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
           self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
           self.rect.y += self.speed
player = Player('ping.pong.png', 8,50,250,25,25)
player2 = Player('ping.pong.png', 600,550,250,25,25)
while app:
    for e in event.get():
        if e.type == QUIT:
            app = False
    window.blit(table, (0,0))
    player.reset()
    player.update_l()
    player2.reset()
    player2.update_r()
    clock.tick(FPS)
    display.update()
    
