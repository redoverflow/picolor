from hooman import Hooman
import pygame
import pygame.freetype
import random
import settings
import colors
import hextorgb
import pygame

_circle_cache = {}
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

def render_outline(text, font, gfcolor=pygame.Color('dodgerblue'), ocolor=(255, 255, 255), opx=2):
    textsurface = font.render(text, True, gfcolor)
    textsurface = textsurface.convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    x = font.render(text, True, ocolor).convert_alpha()
    osurf.blit(x, (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf

window_width, window_height = 640, 480
hapi = Hooman(window_width, window_height)
COLOR_NAME_FONT = pygame.font.Font("inkythinpixels.ttf", 24)
SLIDER_FONT = pygame.font.Font("inkythinpixels.ttf", 18)

r_slider_options = {"value_range": [0, 255], "starting_value": random.randint(0, 255)}
g_slider_options = {"value_range": [0, 255], "starting_value": random.randint(0, 255)}
b_slider_options = {"value_range": [0, 255], "starting_value": random.randint(0, 255)}

themecols = [(255, 255, 255), (0, 0, 0)]
if settings.getsettings()["darkmode"] == 1:
    themecols[0] = (11, 11, 11)
    themecols[1] = (255, 255, 255)
    print("dark mode")
elif settings.getsettings()["darkmode"] == 0:
    print("white mode")
else:
    print("incorrect darkmode setting")

hapi.background(themecols[0])

r_slider = hapi.slider((window_width-400)/2, 320, 400, 10, r_slider_options)
g_slider = hapi.slider((window_width-400)/2, 360, 400, 10, g_slider_options)
b_slider = hapi.slider((window_width-400)/2, 400, 400, 10, b_slider_options)

targetcolor, targetcolorname = random.choice(colors.getcolornames())
targetcolor = hextorgb.hextorgb(targetcolor)

hapi.fill(targetcolor)
hapi.rect((window_width-250)/2, 20, 250, 250)
colornametext = COLOR_NAME_FONT.render(targetcolorname, 1, (255, 255, 255))
hapi.screen.blit(render_outline(targetcolorname, COLOR_NAME_FONT, hapi.color["white"], hapi.color["black"], opx=4), ((window_width-colornametext.get_width())/2, (250-colornametext.get_height())/2+20))

while hapi.is_running:
    r_slider.update()
    g_slider.update()
    b_slider.update()

    hapi.fill(themecols[0])
    hapi.rect((window_width-400)/2, 300, 400, 20)
    hapi.rect((window_width-400)/2, 340, 400, 20)
    hapi.rect((window_width-400)/2, 380, 400, 20)

    text_surface = SLIDER_FONT.render(f"R: {str(round(r_slider.value())).zfill(3)}", 0, themecols[1])
    hapi.screen.blit(text_surface, (((window_width-text_surface.get_width())/2, 300)))
    text_surface1 = SLIDER_FONT.render(f"G: {str(round(g_slider.value())).zfill(3)}", 0, themecols[1])
    hapi.screen.blit(text_surface1, (((window_width-text_surface1.get_width())/2, 340)))
    text_surface2 = SLIDER_FONT.render(f"B: {str(round(b_slider.value())).zfill(3)}", 0, themecols[1])
    hapi.screen.blit(text_surface2, (((window_width-text_surface2.get_width())/2, 380)))

    hapi.fill((r_slider.value(), g_slider.value(), b_slider.value()))
    hapi.rect((window_width-400)/2, 430, 400, 20)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()