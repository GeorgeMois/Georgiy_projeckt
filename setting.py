import os
import pygame as pg

setting = {
    "w" : 600,
    "h" : 436,
    "title" : "Carpy-py",
    "fps" : 30,
}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, "media")


player_img = pg.image.load(os.path.join(media_folder, "player.png"))
prise_img = pg.image.load(os.path.join(media_folder, "prise.webp"))
obstacle1_img = pg.image.load(os.path.join(media_folder, "obstacle 1.png"))
obstacle2_img = pg.image.load(os.path.join(media_folder, "obstacle 2.png"))
obstacle3_img = pg.image.load(os.path.join(media_folder, "obstacle 3.png"))
obstacle4_img = pg.image.load(os.path.join(media_folder, "obstacle 4.png"))

cars = [obstacle1_img, obstacle2_img, obstacle3_img, obstacle4_img]

background_img = pg.image.load(os.path.join(media_folder, "дорога2.webp"))


clock = pg.time.Clock()