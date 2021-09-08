from hooman import Hooman
import pygame
import pygame.freetype
import settings

window_width, window_height = 640, 480
hapi = Hooman(window_width, window_height)
GAME_FONT = pygame.freetype.Font("inkythinpixels.ttf", 24)


slider_options = {"value_range": [0, 255]}

r_slider = hapi.slider((window_width-400)/2, 300, 400, 10, slider_options)
g_slider = hapi.slider((window_width-400)/2, 340, 400, 10, slider_options)
b_slider = hapi.slider((window_width-400)/2, 380, 400, 10, slider_options)

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

    text_surface, rect = GAME_FONT.render(f"R: {round(r_slider.value())}", fgcolor = (255, 255, 255), size = 18)
    hapi.screen.blit(text_surface, (((window_width-text_surface.get_width())/2, 280)))
    text_surface1, rect1 = GAME_FONT.render(f"G: {round(g_slider.value())}", fgcolor = (255, 255, 255), size = 18)
    hapi.screen.blit(text_surface1, (((window_width-text_surface1.get_width())/2, 320)))
    text_surface2, rect2 = GAME_FONT.render(f"B: {round(b_slider.value())}", fgcolor = (255, 255, 255), size = 18)
    hapi.screen.blit(text_surface2, (((window_width-text_surface2.get_width())/2, 360)))

    hapi.fill((r_slider.value(), g_slider.value(), b_slider.value()))
    hapi.rect((window_width-250)/2, 0, 250, 250)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()