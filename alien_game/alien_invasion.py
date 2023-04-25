import sys
import pygame

from settings import Settings
from ship import Ship
class AlienInvasion:
    #管理游戏资源和行为的类
    def __init__(self):
        pygame.init()
        #创建一个实例赋给self.settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # self.screen  = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # self.bgColor = (230,230,230)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_1:
            sys.exit()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        #监控键盘和鼠标事件
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        #每次循环都重绘屏幕
        #self.screen.fill(self.bgColor)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
    def run_game(self):
        while True:
            #事件管理
            self._check_events()
            #更新飞船调整位置
            self.ship.update()
            #屏幕更新
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()