class Settings:
   #存储该游戏的所有设置的类 
    def __init__(self):
        #初始化游戏设置
        #屏幕设置
        self.screen_width =1200
        self.screen_height=800
        self.bg_color =(230,230,230)
        #飞船设置速度
        self.ship_speed = 1.5
        self.ship_limit =3

        #子弹设置
        self.bullet_speed =1.5
        self.bullet_width =3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed =10
        #fleet_direction为1表示右移，-1表示左移
        self.fleet_direction = 1

        #加快游戏节奏的速度
        self.speedup_scale =1.1
        self.initialize_dynamic_settings()
        #外星人分数的的提高速度
        self.score_scale =1.5
    
    def initialize_dynamic_settings(self):
        #初始化随游戏进行而变化的设置
        self.ship_speed =1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction =1
        #计分
        self.alien_points =50
    
    def increase_speed(self):
        #提高速度设置
        self.ship_speed *=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        #调用Print函数会影响性能
        #print(self.alien_points)
    
    
