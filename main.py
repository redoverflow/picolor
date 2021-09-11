from hooman import Hooman
import pygame
import pygame.freetype
import random
# modules from files
import sys
sys.path.append("./modules/")

import colors
import hextorgb
import outline

window_width, window_height = 640, 480
hapi = Hooman(window_width, window_height)
COLOR_NAME_FONT = pygame.font.Font("assets/fonts/inkythinpixels.ttf", 24)
SLIDER_FONT = pygame.font.Font("assets/fonts/inkythinpixels.ttf", 18)
MENUS_FONT = pygame.font.Font("assets/fonts/inkythinpixels.ttf", 28)

logo = pygame.image.load("assets/images/logo.png")

r_slider_options = {"value_range": [0, 255], "starting_value": random.randint(0, 255)}
g_slider_options = {"value_range": [0, 255], "starting_value": random.randint(0, 255)}
b_slider_options = {"value_range": [0, 255], "starting_value": random.randint(0, 255)}

# 0 - main menu
# 1 - settings
# 2 - game
# 3 - exit
# 4 - results
gamestate = 0

# [0] is main menu
# [1] is game
# [2] is settings
# [3] is results
initstates = [0, 0, 0, 0]

# score for results screen
score = ["", "", ""]

# [0] is bg
# [1] is fg
themecols = [(255, 255, 255), (0, 0, 0)]

hapi.background(themecols[0])

while gamestate != 3:
    if gamestate == 0:
        print(gamestate)
        if initstates[0] == 0:
            playbtn = MENUS_FONT.render("Play", 0, themecols[1])
            settingsbtn = MENUS_FONT.render("Settings", 0, themecols[1])
            exitbtn = MENUS_FONT.render("Exit", 0, themecols[1])

            playbtnrect = playbtn.get_rect()
            settingsbtnrect = settingsbtn.get_rect()
            exitbtnrect = exitbtn.get_rect()

            playbtnrect.update(((window_width-playbtn.get_width())/2-settingsbtn.get_width(), 300), (playbtn.get_width(), playbtn.get_height()))
            settingsbtnrect.update(((window_width-settingsbtn.get_width())/2, 300), (settingsbtn.get_width(), settingsbtn.get_height()))
            exitbtnrect.update(((window_width-exitbtn.get_width())/2+settingsbtn.get_width(), 300), (exitbtn.get_width(), exitbtn.get_height()))
            def handle_events_mm(event):
                global gamestate
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if playbtnrect.collidepoint(mouse_pos):
                            print('Play button was pressed at {0}'.format(mouse_pos))
                            gamestate = 2
                    if settingsbtnrect.collidepoint(mouse_pos):
                            print('Settings button was pressed at {0}'.format(mouse_pos))
                            gamestate = 1
                    if exitbtnrect.collidepoint(mouse_pos):
                            print('Exit button was pressed at {0}'.format(mouse_pos))
                            gamestate = 3
                if event.type == pygame.QUIT:
                    print("exiting")
                    quit()


            hapi.handle_events = handle_events_mm
            initstates[0] = 1
        
        while hapi.is_running:
            if gamestate != 0:
                break
            hapi.screen.blit(logo, ((window_width-logo.get_width())/2, (window_height-logo.get_height())/2))

            hapi.screen.blit(playbtn, playbtnrect)
            hapi.screen.blit(settingsbtn, settingsbtnrect)
            hapi.screen.blit(exitbtn, exitbtnrect)

            hapi.flip_display()
            hapi.event_loop()
    elif gamestate == 1:
        if initstates[2] == 0:
            hapi.fill(themecols[0])
            hapi.rect(0, 0, window_width, window_height)

            nothinghere = MENUS_FONT.render("Nothing here... yet...", 1, themecols[1])
            def handle_events_stt(event):
                if event.type == pygame.QUIT:
                    print("exiting")
                    quit()
            hapi.handle_events = handle_events_stt
        
        while hapi.is_running:
            if gamestate != 1:
                break
            hapi.screen.blit(nothinghere, ((window_width-nothinghere.get_width())/2, 30))

            hapi.flip_display()
            hapi.event_loop()

    elif gamestate == 2:
        print(gamestate)
        if initstates[1] == 0:
            hapi.fill(themecols[0])
            hapi.rect(0, 0, window_width, window_height)
            
            logo.fill((0, 0, 0, 0))
            r_slider = hapi.slider((window_width-400)/2, 320, 400, 10, r_slider_options)
            g_slider = hapi.slider((window_width-400)/2, 360, 400, 10, g_slider_options)
            b_slider = hapi.slider((window_width-400)/2, 400, 400, 10, b_slider_options)

            def handle_events_mg(event):
                if event.type == pygame.QUIT:
                    print("exiting")
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # percentage error formula used
                        print(f"R: {round(int(str(round(r_slider.value())-targetcolor[0]).replace('-', ''))/targetcolor[0]*100)}%")
                        print(f"G: {round(int(str(round(g_slider.value())-targetcolor[1]).replace('-', ''))/targetcolor[1]*100)}%")
                        print(f"B: {round(int(str(round(b_slider.value())-targetcolor[2]).replace('-', ''))/targetcolor[2]*100)}%")
            
            hapi.handle_events = handle_events_mg

            targetcolor, targetcolorname = random.choice(colors.getcolornames())
            targetcolor = hextorgb.hextorgb(targetcolor)

            hapi.fill(targetcolor)
            hapi.rect((window_width-250)/2, 20, 250, 250)
            colornametext = COLOR_NAME_FONT.render(targetcolorname, 1, (255, 255, 255))
            hapi.screen.blit(outline.render_outline(targetcolorname, COLOR_NAME_FONT, hapi.color["white"], hapi.color["black"], opx=4), ((window_width-colornametext.get_width())/2, (250-colornametext.get_height())/2+20))

            initstates[1] = 1
        while hapi.is_running:
            if gamestate != 2:
                break
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
    elif gamestate == 3:
        pygame.quit()
    elif gamestate == 4:
        print(gamestate)