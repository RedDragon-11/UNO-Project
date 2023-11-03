import pygame as pg
import random

global screen

pg.init()

window = screen_width, screen_height = 1600, 900
scale_size = window
scale_card_size = 0

card_width = 130
card_height = 182
def_rect = pg.Rect(0,0, card_width, card_height)

screen = pg.display.set_mode(window)
clock = pg.time.Clock()
screen.fill('black')


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    #creates background

    pg.draw.rect(screen, black, (0, 0, screen_width, 600, 0))
    pg.display.flip()
    clock.tick(60)







