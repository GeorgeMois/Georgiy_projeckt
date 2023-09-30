from setting import *
import random
from entity.player import Player
from entity.prise import Prise
from entity.obstacle import Obstacle

pg.init()

screen = pg.display.set_mode((setting['w'], setting['h']))
pg.display.set_caption(setting['title'])

all_sprite = pg.sprite.Group()
player = Player()
all_sprite.add(player)

prise_group = pg.sprite.Group()
obstacle_group = pg.sprite.Group()

SPAWN_SPRITE = pg.USEREVENT + 1
SPAWN_CAR = pg.USEREVENT + 2
pg.time.set_timer(SPAWN_SPRITE, 700)
pg.time.set_timer(SPAWN_CAR, 1500)

font = pg.font.Font(None, 56)


def new_mobs():
    prise = Prise(random.randint(0, setting['w']), 0)
    all_sprite.add(prise)
    prise_group.add(prise)


def new_cars():
    cars = Obstacle(random.randint(0, setting['w']), 0)
    all_sprite.add(cars)
    obstacle_group.add(cars)


run = True
score = 0
while run:

    clock.tick(setting['fps'])
    pg.display.flip()
    screen.blit(background_img, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWN_SPRITE:
            new_mobs()
        if event.type == SPAWN_CAR:
            new_cars()

    text = font.render(f"{score}", True, (255, 255, 255))
    screen.blit(text, (setting['w'] - 80, 40))
    all_sprite.update()
    all_sprite.draw(screen)

    if pg.sprite.spritecollide(player, prise_group, True, pg.sprite.collide_circle):
        score += 1

    if pg.sprite.spritecollide(player, obstacle_group, False, pg.sprite.collide_circle):
        run = False


    pg.display.flip()

pg.quit()
