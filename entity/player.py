from setting import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.speedx = None
        self.speedy = None
        self.image = player_img
        self.rect = self.image.get_rect()
        self.radius = 1
        self.rect.center = (400, 400)
        self.last_update = pg.time.get_ticks()

    def update(self):

        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        if keystate[pg.K_UP]:
            self.speedy = -8
        self.rect.y += self.speedy

        if keystate[pg.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy


        if self.rect.right > setting['w']:
            self.rect.right = setting['w']
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > setting['h']:
            self.rect.bottom = setting['h']
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom < setting["h"]:
            self.rect.y += 5

        else:
            self.rect.bottom = setting["h"]

        if self.rect.top < 0:
            self.rect.top = 0
