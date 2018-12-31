from modules.generators import *
from modules.corr_rot import rot_center


def testing():
    global curr_screen, show_menu, is_lens_on, frame, curr_anim, curr_tst_potion
    screen.blit(bg_lab, (0, 0))
    if curr_anim:
        if type(rat[curr_anim]) == list:
            if frame > len(rat[curr_anim]) - 2:  # DO NOT TOUCH!!!
                if not timer % 5:
                    frame = 0
            else:
                if not timer % 5:
                    frame += 1
            screen.blit(rat[curr_anim][frame], (80 - rat[curr_anim][frame].get_width() // 2,
                                                48 - rat[curr_anim][frame].get_height() + rat['idle'].get_height()))
        else:
            screen.blit(rat[curr_anim], (80 - rat[curr_anim][frame].get_width() // 2,
                                         48 - rat[curr_anim][frame].get_height() + rat['idle'].get_height()))
    else:
        screen.blit(rat['idle'], (80 - rat['idle'].get_width() // 2, 48))

    if potions_cooked['brew']:
        x_pos = 80 - len(potions_cooked['brew']) * 15 // 2
        for i in range(len(potions_cooked['brew'])):
            screen.blit(ptn_tile, (x_pos, 85))
            screen.blit(potions[potions_cooked['brew'][i]], (x_pos, 85))
            if curr_tst_potion == i:
                screen.blit(tst_sel, (x_pos, 85))
            x_pos += 15
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_v:
                is_lens_on = not is_lens_on
            elif event.key == pg.K_RIGHT:
                curr_tst_potion += 1
                if curr_tst_potion > len(potions_cooked['brew']) - 1:
                    curr_tst_potion = 0
            elif event.key == pg.K_LEFT:
                curr_tst_potion -= 1
                if curr_tst_potion < 0:
                    curr_tst_potion = len(potions_cooked['brew']) - 1
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if guide_btn.is_interacted() and show_menu:
                    curr_screen = 'guide'
                elif brew_btn.is_interacted() and show_menu:
                    curr_screen = 'brewing'
                elif inv_btn.is_interacted() and show_menu:
                    curr_screen = 'outside(invert)'
                elif inf_btn.is_interacted() and show_menu:
                    curr_screen = 'infusion'
                elif show_menu_btn.is_interacted():
                    show_menu = False if show_menu else True
            elif event.button == 4:
                curr_anim = 'hypnosis'
            elif event.button == 5:
                curr_anim = ''


def infusion():
    global is_lens_on, curr_screen, show_menu, arelh_essence, arelh_sparkles, curr_inf_potion, curr_sel_inf_potion
    screen.blit(bg, (0, 0))
    if inf_ptn_sel.is_interacted() and curr_sel_inf_potion == '':
        inf_ptn_sel.draw()
        x_pos = 80 - len(potions_cooked['brew']) * 15 // 2
        if potions_cooked:
            for i in range(len(potions_cooked['brew'])):
                screen.blit(ptn_tile, (x_pos, 85))
                screen.blit(potions[potions_cooked['brew'][i]], (x_pos, 85))
                if curr_inf_potion == i:
                    screen.blit(inf_sel, (x_pos, 85))
                x_pos += 15
    elif curr_sel_inf_potion != '':
        N_btn.draw()
        Y_btn.draw()
        screen.blit(potions[curr_sel_inf_potion], (inf_ptn_sel.x, inf_ptn_sel.y))

    essence_container_pic = pic_import('Arelh essence container')
    essence_container = pg.Surface(essence_container_pic.get_size(), pg.SRCALPHA, 32)
    if arelh_essence:
        pg.draw.rect(essence_container, (0, 192, 255), (1, 14 - arelh_essence, 7, arelh_essence))
    essence_container.blit(essence_container_pic, (0, 0))
    screen.blit(essence_container, (145, 10))
    if randint(0, 20) < arelh_essence:
        arelh_sparkles.append(Floater(randint(146, 150), 21, arelh_sparkle_pic, 3))
    for i in arelh_sparkles:
        i.move()
        i.draw()
    if not (curr_sel_inf_potion in potions_cooked['brew']):
        curr_sel_inf_potion = ''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_v:
                is_lens_on = not is_lens_on
            if inf_ptn_sel.is_interacted():
                if event.key == pg.K_LEFT:
                    curr_inf_potion -= 1
                    if curr_inf_potion < 0:
                        curr_inf_potion = len(potions_cooked['brew']) - 1
                elif event.key == pg.K_RIGHT:
                    curr_inf_potion += 1
                    if curr_inf_potion > len(potions_cooked['brew']) - 1:
                        curr_inf_potion = 0
                elif event.key == pg.K_SPACE:
                    curr_sel_inf_potion = potions_cooked['brew'][curr_inf_potion]
                    if curr_inf_potion > len(potions_cooked['brew']) - 1:
                        curr_inf_potion = len(potions_cooked['brew']) - 1
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if guide_btn.is_interacted() and show_menu:
                    curr_screen = 'guide'
                elif brew_btn.is_interacted() and show_menu:
                    curr_screen = 'brewing'
                elif inv_btn.is_interacted() and show_menu:
                    curr_screen = 'outside(invert)'
                elif show_menu_btn.is_interacted():
                    show_menu = False if show_menu else True
                elif tst_btn.is_interacted() and show_menu:
                    curr_screen = 'testing'
                elif N_btn:
                    curr_sel_inf_potion = ''
                elif Y_btn and arelh_essence >= 2:
                    if curr_sel_inf_potion in inf_potions:
                        potions_cooked['inf'].append(inf_potions[curr_sel_inf_potion])
                        arelh_sparkles.append(
                            Floater(inf_ptn_sel.x + 5, inf_ptn_sel.y,
                                    inf_potions_pics[inf_potions[curr_sel_inf_potion]],
                                    3))
                        potions_cooked['brew'].remove(curr_sel_inf_potion)
                        arelh_essence -= 2
                    curr_sel_inf_potion = ''


def after_render():
    show_menu_btn.draw()
    if show_menu:
        inv_btn.draw()
        brew_btn.draw()
        guide_btn.draw()
        inf_btn.draw()
        tst_btn.draw()

    if curr_screen == 'nowhere':
        if breach.is_interacted():
            draw_sign([breach.name, 'Oh look! It''s a breach, which', "materialized because of authors'",
                       'laziness!(this scene is either', 'WIP, or the link leads to nowhere)'])
    elif curr_screen == 'brewing':
        for i in dusts.keys():
            if dusts[i].is_interacted():
                draw_sign((dusts[i].name, 'a magic powder you', 'can cook for potions'))
    elif curr_screen == 'outside(invert)':
        if MFD.is_interacted():
            draw_sign(['MoonlightFocusingDevice(MFD)', 'A device able to concentrate moonlight',
                       'into strong inverting beam!', 'What about that, Ilon Mask?!'])
    elif curr_screen == 'guide':
        if curr_page:
            oup_screen.blit(pages[curr_page - 1], (45 * zoom, 0))
    text = pg.font.Font('GeosansLight.ttf', 40).render(version, True, (200, 50, 200))
    oup_screen.blit(text, (160 * zoom - text.get_size()[0], 0))


def guide():
    global curr_dusts_added, curr_bubbles, curr_screen, show_menu, potions_cooked, curr_page, rot
    screen.blit(bg, (0, 0))
    screen.blit(rot_center(aura, rot), (80 - aura.get_width() // 2, 0))
    rot += 1
    if rot > 359:
        rot = 0
    if curr_page == 0:
        screen.blit(title_page, (40, 0))
    else:
        screen.blit(page, (40, 0))

    if curr_page < len(pages):
        next_page_btn.draw()
    if curr_page > 0:
        prev_page_btn.draw()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if next_page_btn.is_interacted():
                    if curr_page < len(pages):
                        curr_page += 1
                elif prev_page_btn.is_interacted():
                    if curr_page > 0:
                        curr_page -= 1
                elif brew_btn.is_interacted() and show_menu:
                    curr_screen = 'brewing'
                elif inf_btn.is_interacted() and show_menu:
                    curr_screen = 'infusion'
                elif inv_btn.is_interacted() and show_menu:
                    curr_screen = 'outside(invert)'
                elif tst_btn.is_interacted() and show_menu:
                    curr_screen = 'testing'
                elif show_menu_btn.is_interacted():
                    show_menu = False if show_menu else True


def not_made_yet():
    global curr_screen, show_menu, glitches, timer
    timer += 1
    if timer == 10:
        timer = 0

    if not timer % randint(1, 6):
        glitches.append(Glitch(randint(0, 158), randint(0, 98)))
    screen.blit(corrupted_bg, (0, 0))
    breach.draw()
    for i in glitches:
        i.move()
        i.draw()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if brew_btn.is_interacted() and show_menu:
                    curr_screen = 'brewing'
                elif inf_btn.is_interacted() and show_menu:
                    curr_screen = 'infusion'
                elif inv_btn.is_interacted() and show_menu:
                    curr_screen = 'outside(invert)'
                elif guide_btn.is_interacted():
                    curr_screen = 'guide'
                elif tst_btn.is_interacted() and show_menu:
                    curr_screen = 'testing'
                elif show_menu_btn.is_interacted():
                    show_menu = False if show_menu else True


def moonlight():
    global curr_screen, show_menu, potions_cooked, curr_potion, curr_sel_potion, inv_potions, inv_potion, is_lens_on, arelh_essence
    screen.blit(bg_out_1, (0, 0))

    if not timer % randint(1, 10):
        p = choice(star_pos_l)
        stars.append(Star(p[0], p[1], 3))
    for i in stars:
        i.move()
        i.draw()
    MFD.draw()
    if is_lens_on:
        mx, my = pg.mouse.get_pos()[0] // zoom, pg.mouse.get_pos()[1] // zoom
        visor = pg.Surface(lens_pic.get_size(), pg.SRCALPHA, 32)
        visor.blit(invis_inv, (-mx + 7, -my + 5))
        visor.blit(lens_pic, (0, 0))
        screen.blit(visor, (mx - 7, my - 5))
    pg.mouse.set_visible(not is_lens_on)

    if inv_ptn_sel.is_interacted() and curr_sel_potion == '':
        inv_ptn_sel.draw()
        x_pos = 80 - len(potions_cooked['brew']) * 15 // 2
        if potions_cooked:
            for i in range(len(potions_cooked['brew'])):
                screen.blit(ptn_tile, (x_pos, 85))
                screen.blit(potions[potions_cooked['brew'][i]], (x_pos, 85))
                if curr_potion == i:
                    screen.blit(moonlight_sel, (x_pos, 85))
                x_pos += 15
    if curr_sel_potion != '':
        N_btn.draw()
        screen.blit(potions[curr_sel_potion], (139, 16))
    if inv_potion:
        for i in inv_potion:
            i.draw()
            i.move()
    if not (curr_sel_potion in potions_cooked['brew']):
        curr_sel_potion = ''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_v:
                is_lens_on = not is_lens_on
            if inv_ptn_sel.is_interacted():
                if event.key == pg.K_LEFT:
                    curr_potion -= 1
                    if curr_potion < 0:
                        curr_potion = len(potions_cooked['brew']) - 1
                elif event.key == pg.K_RIGHT:
                    curr_potion += 1
                    if curr_potion > len(potions_cooked['brew']) - 1:
                        curr_potion = 0
                elif event.key == pg.K_SPACE:
                    curr_sel_potion = potions_cooked['brew'][curr_potion]

        elif event.type == pg.MOUSEBUTTONDOWN:
            if brew_btn.is_interacted() and show_menu:
                curr_screen = 'brewing'
            elif inf_btn.is_interacted() and show_menu:
                curr_screen = 'infusion'
            elif guide_btn.is_interacted() and show_menu:
                curr_screen = 'guide'
            elif tst_btn.is_interacted() and show_menu:
                curr_screen = 'testing'
            elif N_btn.is_interacted():
                curr_sel_potion = ''
            elif MFD.is_interacted():
                if curr_sel_potion != '':
                    if curr_sel_potion in inv_potions and inv_potions[curr_sel_potion] not in potions_cooked['inv']:
                        potions_cooked['inv'].append(inv_potions[curr_sel_potion])
                        inv_potion.append(Floater(139, 16, inv_potions_pics[inv_potions[curr_sel_potion]], 3))
                        for i in range(8):
                            surf = pg.Surface((1, randint(1, 4)))
                            surf.fill((70, 50, 255))
                            inv_potion.append(Floater(139 + i * 2, 31 - surf.get_size()[1], surf, 6))
                    else:
                        inv_potion.append(Floater(139, 16, arelh_essence_pic, -6))
                        arelh_essence += 1 if arelh_essence < 10 else 0
                    potions_cooked['brew'].remove(curr_sel_potion)

                    curr_sel_potion = ''
            elif show_menu_btn.is_interacted():
                show_menu = False if show_menu else True


def brewing():
    global curr_dusts_added, curr_bubbles, curr_screen, show_menu, potions_cooked, is_lens_on
    screen.blit(bg, (0, 0))
    screen.blit(shelf, (55, 30))
    for i in dusts.keys():
        dusts[i].draw()
    screen.blit(cauldron, (80 - cauldron.get_size()[0] // 2, 100 - cauldron.get_size()[1]))
    if curr_dusts_added and timer + 10 > randint(0, 50) > timer - 10:
        curr_bubbles.append(Floater(randint(95 - cauldron.get_size()[0], 65 + cauldron.get_size()[0]),
                                    104 - cauldron.get_size()[1], bubbles[choice(curr_dusts_added)], 5))
    for i in curr_bubbles:
        i.move()
        i.draw()
    if len(curr_dusts_added) > 0:
        N_btn.draw()
        if len(curr_dusts_added) > 1:
            Y_btn.draw()
    curr_dusts_added.sort()
    if is_lens_on:
        mx, my = pg.mouse.get_pos()[0] // zoom, pg.mouse.get_pos()[1] // zoom
        visor = pg.Surface(lens_pic.get_size(), pg.SRCALPHA, 32)
        visor.blit(invis_brew, (-mx + 7, -my + 5))
        visor.blit(lens_pic, (0, 0))
        screen.blit(visor, (mx - 7, my - 5))
    pg.mouse.set_visible(not is_lens_on)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_v:
                is_lens_on = not is_lens_on
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if N_btn.is_interacted():
                    curr_dusts_added = []
                elif Y_btn.is_interacted() and len(curr_dusts_added) > 1:
                    if recipies[tuple(curr_dusts_added)] not in potions_cooked['brew']:
                        potions_cooked['brew'].append(recipies[tuple(curr_dusts_added)])
                        curr_bubbles = [Floater(80 - potions['Healing'].get_size()[0] // 2,
                                                100 - cauldron.get_size()[1] - potions['Healing'].get_size()[1],
                                                potions[recipies[tuple(curr_dusts_added)]], 5)]
                        for i in range(5):
                            surf = pg.Surface((3, 3))
                            surf.set_colorkey((0, 0, 0))
                            surf.blit(particle_ptn_sheet, (randint(0, 2) * -3, 0))
                            curr_bubbles.append(Floater(80 - randint(-10, 11),
                                                        100 - cauldron.get_size()[1],
                                                        surf, randint(1, 5)))
                    curr_dusts_added = []
                elif guide_btn.is_interacted() and show_menu:
                    curr_screen = 'guide'
                elif inf_btn.is_interacted() and show_menu:
                    curr_screen = 'infusion'
                elif tst_btn.is_interacted() and show_menu:
                    curr_screen = 'testing'
                elif inv_btn.is_interacted() and show_menu:
                    curr_screen = 'outside(invert)'
                elif show_menu_btn.is_interacted():
                    show_menu = False if show_menu else True
                else:
                    for i in dusts.keys():
                        if dusts[i].is_interacted():
                            if i not in curr_dusts_added and len(curr_dusts_added) < 2:
                                curr_dusts_added.append(i)


def draw_sign(text=None):
    if text is None:
        text = ['abc', 'def']
    s = sign(text)
    oup_screen.blit(s, (80 * zoom - s.get_size()[0] // 2, 100 * zoom - s.get_size()[1]))


class Interactable:
    def __init__(self, x, y, pic, after_rendered=False, name=''):
        self.pic = pic
        self.rect = self.pic.get_rect()
        self.x = x
        self.y = y
        self.after_rendered = after_rendered
        if not after_rendered:
            self.rect.x = x * zoom
            self.rect.y = y * zoom
            self.rect.width *= zoom
            self.rect.height *= zoom
        else:
            self.rect.x = x
            self.rect.y = y
        self.name = name

    def flip(self, axis='v'):
        if axis == 'v':
            self.pic = pg.transform.flip(self.pic, False, True)
        else:
            self.pic = pg.transform.flip(self.pic, True, False)

    def is_interacted(self):
        mousex, mousey = pg.mouse.get_pos()
        if self.rect.collidepoint(mousex, mousey):
            return True
        else:
            return False

    def draw(self):
        if self.after_rendered:
            oup_screen.blit(self.pic, (self.x, self.y))
        else:
            screen.blit(self.pic, (self.x, self.y))

    def __bool__(self):
        return self.is_interacted()


class Floater:
    def __init__(self, x, y, pic, time):
        self.x = x
        self.y = y
        self.pic = pic
        self.time = time

    def move(self):
        self.y -= self.time
        if self.time == 0:
            if curr_bubbles.count(self):
                curr_bubbles.remove(self)
            elif inv_potion.count(self):
                inv_potion.remove(self)
            elif arelh_sparkles.count(self):
                arelh_sparkles.remove(self)
        self.time -= 1 if self.time > 0 else -1

    def draw(self):
        screen.blit(self.pic, (self.x, self.y))


class Star:
    def __init__(self, x, y, speed=2):
        self.pic = star
        self.time = 0
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.time += 1
        if self.time == self.speed * 3:
            stars.remove(self)

    def draw(self):
        screen.blit(self.pic, (self.x, self.y), (5 * (self.time // self.speed), 0, 5, 5))


class Glitch:
    def __init__(self, x, y):
        self.pic = glitch
        self.time = 10
        self.x = x
        self.y = y
        self.type = randint(0, 3)

    def move(self):
        self.time -= 1
        self.x += randint(-1, 1)
        self.y += randint(-1, 1)
        if self.time == 0:
            glitches.remove(self)

    def draw(self):
        screen.blit(self.pic, (self.x, self.y), (3 * self.type, 0, 3, 3))


zoom = 9
debug_mode = True
version = 'GameChemy v0.65a'
screen = pg.display.set_mode((160, 100))
pic_import = lambda x: pg.image.load('New_Sprites/' + x + '.png')
bg = pic_import('BG')
bg_out_1 = pic_import('BG(outside moonlight)')
oup_screen = pg.display.set_mode((160 * zoom, 100 * zoom))
ptn_types = ['normal', 'amplified', 'moonlight']

rat = {'idle': pic_import('Rat/Idle'),
       'burn': [pic_import('Rat/Burn 1'),
                pic_import('Rat/Burn 2')],
       'happy': pic_import('Rat/Happy'),
       'hypnosis': [pic_import('Rat/Hypnosis 1'),
                    pic_import('Rat/Hypnosis 2'),
                    pic_import('Rat/Hypnosis 3')],
       'fungus': None,
       'scorched': pic_import('Rat/Scorched')}

shelf = pic_import('Shelf')
cauldron = pic_import('Cauldron')
curr_dusts_added = []
curr_potion = 0
curr_inf_potion = 0
curr_tst_potion = 0
curr_sel_potion = ''
curr_sel_inf_potion = ''
dusts = {'watre': Interactable(60, 25, make_a_dust_pic((0, 0, 200)), name='watre essence'),
         'erthe': Interactable(70, 25, make_a_dust_pic((0, 150, 0)), name='erthe essence'),
         'frie': Interactable(80, 25, make_a_dust_pic((255, 50, 0)), name='frie essence'),
         'aier': Interactable(90, 25, make_a_dust_pic((255, 255, 0)), name='aier essence')}
bubbles = {'watre': make_a_bubble_pic((0, 0, 200)),
           'erthe': make_a_bubble_pic((0, 150, 0)),
           'frie': make_a_bubble_pic((255, 50, 0)),
           'aier': make_a_bubble_pic((255, 255, 0))}
potions = {'Healing': make_a_potion_pic('normal', (235, 0, 0)),
           'Flame': make_a_potion_pic('normal', (255, 150, 0)),
           'Happiness': make_a_potion_pic('normal', (255, 100, 100)),
           'Hypnosis': make_a_potion_pic('normal', (0, 0, 200)),
           'Fungal': make_a_potion_pic('normal', (200, 0, 255)),
           'Slightly acidic': make_a_potion_pic('normal', (150, 255, 150))}
inv_potions = {'Healing': 'Harming',
               'Flame': 'Ice',
               'Happiness': 'Sadness'}
inf_potions = {'Slightly acidic': 'Evaporator',
               'Hypnosis': 'Otherworldly connection',
               'Fungal': 'Infestation'}
inv_potions_pics = {'Harming': make_a_potion_pic('moonlight', (125, 50, 0)),
                    'Ice': make_a_potion_pic('moonlight', (100, 100, 255)),
                    'Sadness': make_a_potion_pic('moonlight', (50, 10, 155))}
inf_potions_pics = {'Evaporator': make_a_potion_pic('amplified', (150, 255, 0)),
                    'Otherworldly connection': make_a_potion_pic('amplified', (25, 0, 35)),
                    'Infestation': make_a_potion_pic('amplified', (250, 10, 55))}
recipies = {('erthe', 'frie'): 'Healing',
            ('aier', 'watre'): 'Flame',
            ('erthe', 'watre'): 'Happiness',
            ('frie', 'watre'): 'Hypnosis',
            ('aier', 'erthe'): 'Fungal',
            ('aier', 'frie'): 'Slightly acidic'}
inv_potion = []
ptn_tile = pic_import('Potion tile')
star_pos_l = [(20, 12), (40, 65), (50, 30), (90, 30), (60, 55), (80, 35), (130, 25), (150, 10),
              (110, 15), (85, 5), (72, 13), (55, 16), (77, 10), (85, 16), (67, 19)]
show_menu = False
show_menu_btn = Interactable(0, 0, make_a_button_pic('V menu V', 35), True)
curr_bubbles = []
glitches = []
potions_cooked = {'brew': [],
                  'inv': [],
                  'inf': []}
N_btn, Y_btn = Interactable(0, 85, pic_import('N_btn')), Interactable(15, 85, pic_import('Y_btn'))
brew_btn, inv_btn, guide_btn = Interactable(0, 35, make_a_button_pic('brewing'), True), \
                               Interactable(0, 64, make_a_button_pic('invert'), True), \
                               Interactable(0, 92, make_a_button_pic('guide'), True)

inf_btn, tst_btn = Interactable(0, 120, make_a_button_pic('infuse'), True), \
                   Interactable(0, 146, make_a_button_pic('test'), True)

timer = 0
curr_screen = 'testing'
star = pic_import('Star sheet')
glitch = pic_import('Breach effects')
stars = []
MFD = Interactable(13, 12, pic_import('MFD'))
inv_ptn_sel = Interactable(139, 16, pic_import('Potion selector'))
inf_ptn_sel = Interactable(142, 28, pic_import('Potion selector'))
particle_ptn_sheet = pic_import('Potion particles')
moonlight_sel = make_a_selector_pic((50, 50, 255))
inf_sel = make_a_selector_pic((200, 50, 200))
tst_sel = make_a_selector_pic((50, 200, 100))

if debug_mode:
    potions_cooked['brew'] = list(potions.keys())
breach = Interactable(70, 40, pic_import('Breach of WIP'), name='breach')
corrupted_bg = pic_import('Corrupted BG')
tmp = open('pages text', 'r')
tmp = tmp.readlines()
texts = []
lens = []
invis_inv = pic_import('BG(outside moonlight)(invisible stuff)')
invis_brew = pic_import('BG(invisible stuff)')

islen = False
for i in tmp:
    if islen:
        lens.append(int(i[:-1]))
    else:
        texts.append(i[:-1])
    islen = not islen

pages = []
title_page = pic_import('Title page')
bg_lab = pic_import('BG(testing)')
curr_page = 0
next_page_btn, prev_page_btn = Interactable(120, 0, pic_import('btn')), \
                               Interactable(35, 0, pg.transform.flip(pic_import('btn'), True, False))
page = pic_import('Page')
for i in range(len(texts)):
    tmp = generate_a_page(texts[i], lens[i])
    surf = pg.Surface((pic_import('Page').get_size()[0] * zoom, pic_import('Page').get_size()[1] * zoom),
                      pg.SRCALPHA, 32)
    for j in range(len(tmp)):
        surf.blit(tmp[j], (6, 2 + 35 * j))
    pages.append(surf)

lens_pic = pic_import('Lens')
is_lens_on = False
arelh_essence = 5
arelh_essence_pic = pic_import('Arelh essence')
arelh_sparkle_pic = pic_import('Arelh sparkle')
arelh_sparkles = []

frame = 0
curr_anim = ''
aura = pic_import('Aura')
rot = 0
while True:
    screen = pg.Surface((160, 100))
    timer += 1
    if timer > 50:
        timer = 0

    if curr_screen == 'brewing':
        brewing()
    elif curr_screen == 'outside(invert)':
        moonlight()
    elif curr_screen == 'guide':
        guide()
    elif curr_screen == 'infusion':
        infusion()
    elif curr_screen == 'testing':
        testing()
    else:
        curr_screen = 'nowhere'
        not_made_yet()

    screen = pg.transform.scale(screen, (160 * zoom, 100 * zoom))
    oup_screen.blit(screen, (0, 0))
    after_render()
    pg.display.flip()

    pg.time.Clock().tick(50)
