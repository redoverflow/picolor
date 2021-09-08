from hooman import Hooman
import pygame
import pygame.freetype
import settings

window_width, window_height = 640, 480
hapi = Hooman(window_width, window_height)
GAME_FONT = pygame.freetype.Font("inkythinpixels.ttf", 24)


slider_options = {"value_range": [0, 255]}

r_slider = hapi.slider(50, 300, 400, 10, slider_options)
g_slider = hapi.slider(50, 340, 400, 10, slider_options)
b_slider = hapi.slider(50, 380, 400, 10, slider_options)

while hapi.is_running:
    if settings.getsettings()["darkmode"] == 1:
            hapi.background((11, 11, 11))
    elif settings.getsettings()["darkmode"] == 0:
        hapi.background((255, 255, 255))
    else:
        hapi.background((255, 255, 255))

    r_slider.update()
    g_slider.update()
    b_slider.update()

    """hapi.fill(hapi.color["black"])
    r_text = "r:{}".format(round(r_slider.value()))
    hapi.text(r_text, 50, 280)
    g_text = "g:{}".format(round(g_slider.value()))
    hapi.text(g_text, 50, 310)
    b_text = "b:{}".format(round(b_slider.value()))
    hapi.text(b_text, 50, 340)"""

    text_surface, rect = GAME_FONT.render(f"R: {round(r_slider.value())}", fgcolor = (255, 255, 255), size = 18)
    hapi.screen.blit(text_surface, ((400-text_surface.get_width())/2+50, 280))
    text_surface1, rect1 = GAME_FONT.render(f"G: {round(g_slider.value())}", fgcolor = (255, 255, 255), size = 18)
    hapi.screen.blit(text_surface1, ((400-text_surface1.get_width())/2+50, 320))
    text_surface2, rect2 = GAME_FONT.render(f"B: {round(b_slider.value())}", fgcolor = (255, 255, 255), size = 18)
    hapi.screen.blit(text_surface2, ((400-text_surface2.get_width())/2+50, 360))

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()