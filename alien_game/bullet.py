import pygame
from pygame.sprite import Sprite

#继承自Sprite
class Bullet(Sprite):
    #管理飞船发射子弹的类
    def __init__(self,ai_game):
        #在飞船当前位置创造一个子弹对象
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y =self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)