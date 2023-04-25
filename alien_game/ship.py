import pygame
class Ship:
    #管理飞船的类
    def __init__(self,ai_game):
        #初始化飞船并设置其初始位置
        self.screen =ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()
        

        #加载飞船图像并获取外接矩形
        #此时要注意图片路径
        self.image = pygame.image.load('alien_game/images/ship.png')
        self.rect = self.image.get_rect()

        #放置位置
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    #调整飞船的位置
    def update(self):
        #根据移动标志来调整飞船的位置
        if self.moving_right and self.rect.right <self.screen_rect.right:
            #self.rect.x +=1
            #更新飞船而不是rect的值
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            #self.rect.x -=1
            self.x -= self.settings.ship_speed
        #根据self.x更新rect对象
        self.rect.x = self.x