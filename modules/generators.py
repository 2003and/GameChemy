import pygame as pg
from random import choice, randint


pic_import = lambda x: pg.image.load('New_Sprites/' + x + '.png')
pg.init()
ptn_types = ['normal', 'amplified', 'moonlight']
ptn_pics = {'normal': pic_import('Potion'),
            'moonlight': pic_import('Moonlight potion'),
            'amplified': pic_import('Amplified potion')}


def generate_a_page(text='abcdefghijklmnopqrstuvwxyz', limit=10):
    oup = []
    while len(text) >= limit:
        oup.append(text[:limit])
        text = text[limit:]
    oup.append(text)

    font = pg.font.Font('HoneyScript-Light.ttf', 50)

    for i in range(len(oup)):
        oup[i] = font.render(oup[i], True, (0, 0, 50))
    return oup


def sign(text=None):
    if text is None:
        text = ['test', 'tset', 'esetnod32antivirus']
    text = list(text)
    font = pg.font.Font(None, 40)  # 'GeosansLight.ttf'
    font2 = pg.font.Font(None, 25)
    title = text[0]
    del text[0]
    title = font.render(title, True, (0, 0, 0))
    for i in range(len(text)):
        text[i] = font2.render(text[i], True, (20, 20, 0))
    W = title.get_size()[0]
    for i in range(len(text)):
        if text[i].get_size()[0] > W:
            W = text[i].get_size()[0]
    H = 40 + 25 * len(text) + (2 * (len(text) + 1))
    W += 15
    surf = pg.Surface((W, H))
    surf.fill((255, 255, 200))
    pg.draw.rect(surf, (100, 100, 25), (0, 0, W, H), 2)
    surf.blit(title, (5, 2))
    y = 34
    for i in text:
        surf.blit(i, (5, y))
        y += 27
    return surf


def make_a_button_pic(text='asdf', size=25):
    font = pg.font.Font(None, size)
    text = font.render(text, True, (255, 0, 255))
    surf = pg.Surface((text.get_size()[0] + 10, text.get_size()[1] + 10))
    surf.fill((100, 0, 100))
    surf.blit(text, (5, 5))
    pg.draw.rect(surf, (255, 0, 255), (0, 0, surf.get_size()[0], surf.get_size()[1]), 3)
    return surf


def make_a_selector_pic(color=(100, 100, 100)):
    surf = pg.Surface((4, 4))
    srf = pg.Surface((4, 4), pg.SRCALPHA, 32)
    pg.draw.rect(surf, color, (1, 0, 2, 4))
    pg.draw.rect(surf, color, (0, 1, 4, 2))
    surf.set_colorkey((0, 0, 0))
    surf.set_alpha(100)
    srf.set_colorkey((0, 0, 0))
    srf2 = srf
    srf2.blit(surf, (0, 0))
    pg.draw.rect(srf2, color, (1, 1, 2, 2))
    return srf2


def make_a_potion_pic(type='normal',
                      color=(255, 255, 255)):
    surf = pg.Surface((5 if type == 'amplified' else 15, 15))
    surf.fill(color)
    if type in ptn_types:
        surf.blit(ptn_pics[type], (0, 0))
    surf.set_colorkey((255, 255, 255))
    return surf


def make_a_bubble_pic(color=(255, 255, 255)):
    surf = pg.Surface((4, 4))
    surf.fill(color)
    surf.blit(pic_import('Bubble'), (0, 0))
    surf.set_colorkey(color)
    return surf


def make_a_dust_pic(color=(255, 255, 255)):
    surf = pg.Surface((10, 5))
    surf.fill(color)
    surf.blit(pic_import('Dust'), (0, 0))
    surf.set_colorkey(color)
    return surf
