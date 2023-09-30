from setting import *
from random import *


class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.speedy = None
        self.image = cars[randint(0, len(cars)-1)]
        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def update(self):
        self.speedy = randint(1, 7)
        if self.rect.y != setting['w']:
            self.rect.y += self.speedy
        else:
            self.kill()
