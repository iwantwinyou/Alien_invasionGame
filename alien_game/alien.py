import pygame 
from pygame.sprite import  Sprite

class Alien(Sprite):
    #表示单个外星人的类
    def __init__(self, ai_game):
        #初始化外星人并设置其初始位置
        super().__init__()
        self.screen =ai_game.screen

        self.image =pygame.image.load('alien_game/images/alien.png')
        self.rect = self.image.get_rect()

        #每个外星人都在屏幕左上角
        self.rect.x =self.rect.width
        self.rect.y =self.rect.height

        #储存外星人的精确水平位置
        self.x =float(self.rect.x)