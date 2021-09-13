from hooman import Hooman
import pygame
import pygame.freetype
import random
# modules from files
import sys
sys.path.append("./modules/")

import colors
import colorconv
import outline

window_width, window_height = 640, 480
hapi = Hooman(window_width, window_height)
COLOR_NAME_FONT = pygame.font.Font("assets/fonts/inkythinpixels.ttf", 24)
SLIDER_FONT = pygame.font.Font("assets/fonts/inkythinpixels.ttf", 18)
MENUS_FONT = pygame.font.Font("assets/fonts/inkythinpixels.ttf", 28)

# 0 - main menu
# 1 - settings
# 2 - game
# 3 - results
# 4 - help
# 5 - exit
gamestate = 0

# [0] is main menu
# [1] is game
# [2] is settings
# [3] is results
# [4] is help
initstates = [0, 0, 0, 0, 0]

# score for results screen
score = ["", "", ""]
scoreperc = ["", "", ""]

# [0] is bg
# [1] is fg
themecols = [(255, 255, 255), (0, 0, 0)]

hapi.background(themecols[0])

while gamestate != 5:
    if gamestate == 0:
        print(gamestate)
        if initstates[0] == 0:
            hapi.fill(themecols[0])
            hapi.rect(0, 0, window_width, window_height)

            playbtn = MENUS_FONT.render("Play", 0, themecols[1])
            settingsbtn = MENUS_FONT.render("Settings", 0, themecols[1])
            helpbtn = MENUS_FONT.render("Help", 0, themecols[1])
            exitbtn = MENUS_FONT.render("Exit", 0, themecols[1])

            playbtnrect = playbtn.get_rect()
            settingsbtnrect = settingsbtn.get_rect()
            helpbtnrect = helpbtn.get_rect()
            exitbtnrect = exitbtn.get_rect()

            logo = pygame.image.load("assets/images/logo.png")

            playbtnrect.update(((window_width-playbtn.get_width())/2-settingsbtn.get_width()-exitbtn.get_width(), 300), (playbtn.get_width(), playbtn.get_height()))
            settingsbtnrect.update(((window_width-settingsbtn.get_width())/2-exitbtn.get_width(), 300), (settingsbtn.get_width(), settingsbtn.get_height()))
            helpbtnrect.update(((window_width-settingsbtn.get_width())/2+settingsbtn.get_width()-(exitbtn.get_width()/2), 300), (helpbtn.get_width(), helpbtn.get_height()))
            exitbtnrect.update(((window_width-settingsbtn.get_width())/2+settingsbtn.get_width()+exitbtn.get_width(), 300), (exitbtn.get_width(), exitbtn.get_height()))
            def handle_events_mm(event):
                global gamestate
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if playbtnrect.collidepoint(mouse_pos):
                            print('Play button was pressed at {0}'.format(mouse_pos))
                            initstates[0] = 0
                            gamestate = 2
                    if settingsbtnrect.collidepoint(mouse_pos):
                            print('Settings button was pressed at {0}'.format(mouse_pos))
                            initstates[0] = 0
                            gamestate = 1
                    if exitbtnrect.collidepoint(mouse_pos):
                            print('Exit button was pressed at {0}'.format(mouse_pos))
                            initstates[0] = 0
                            gamestate = 5
                    if helpbtnrect.collidepoint(mouse_pos):
                            print('Help button was pressed at {0}'.format(mouse_pos))
                            initstates[0] = 0
                            gamestate = 4
                if event.type == pygame.K_ESCAPE:
                    print("exiting")
                    initstates[0] = 0
                    gamestate = 5
                if event.type == pygame.QUIT:
                    print("exiting")
                    gamestate = 5


            hapi.handle_events = handle_events_mm
            initstates[0] = 1
        
        while hapi.is_running:
            if gamestate != 0:
                break
            hapi.screen.blit(logo, ((window_width-logo.get_width())/2, (window_height-logo.get_height())/2))

            hapi.screen.blit(playbtn, playbtnrect)
            hapi.screen.blit(settingsbtn, settingsbtnrect)
            hapi.screen.blit(helpbtn, helpbtnrect)
            hapi.screen.blit(exitbtn, exitbtnrect)

            hapi.flip_display()
            hapi.event_loop()
    elif gamestate == 1:
        if initstates[2] == 0:
            hapi.fill(themecols[0])
            hapi.rect(0, 0, window_width, window_height)

            nothinghere = MENUS_FONT.render("Nothing here... yet...", 1, themecols[1])
            def handle_events_stt(event):
                global gamestate
                if event.type == pygame.QUIT:
                    print("exiting")
                    gamestate = 5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        initstates[2] = 0
                        gamestate = 0
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
            
            r_slider_options = {"value_range": [1, 255], "starting_value": random.randint(1, 255)}
            g_slider_options = {"value_range": [1, 255], "starting_value": random.randint(1, 255)}
            b_slider_options = {"value_range": [1, 255], "starting_value": random.randint(1, 255)}

            logo.fill((0, 0, 0, 0))
            r_slider = hapi.slider((window_width-400)/2, 320, 400, 10, r_slider_options)
            g_slider = hapi.slider((window_width-400)/2, 360, 400, 10, g_slider_options)
            b_slider = hapi.slider((window_width-400)/2, 400, 400, 10, b_slider_options)

            def handle_events_mg(event):
                global gamestate, x
                if event.type == pygame.QUIT:
                    print("exiting")
                    gamestate = 5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # percentage error formula used
                        print(r_slider.value(), g_slider.value(), b_slider.value())
                        print(targetcolor)
                        print(f"R: {round(int(str(round(r_slider.value())-targetcolor[0]).replace('-', ''))/targetcolor[0]*100)}%")
                        print(f"G: {round(int(str(round(g_slider.value())-targetcolor[1]).replace('-', ''))/targetcolor[1]*100)}%")
                        print(f"B: {round(int(str(round(b_slider.value())-targetcolor[2]).replace('-', ''))/targetcolor[2]*100)}%")
                        scoreperc[0] = round(int(str(round(r_slider.value())-targetcolor[0]).replace('-', ''))/targetcolor[0]*100)
                        scoreperc[1] = round(int(str(round(g_slider.value())-targetcolor[1]).replace('-', ''))/targetcolor[1]*100)
                        scoreperc[2] = round(int(str(round(b_slider.value())-targetcolor[2]).replace('-', ''))/targetcolor[2]*100)
                        score[0] = round(r_slider.value())
                        score[1] = round(g_slider.value())
                        score[2] = round(b_slider.value())
                        print(score)
                        x = 0
                        for y in scoreperc:
                            if y > 255:
                                score[x] = 255
                                x += 1
                            else:
                                x += 1
                        initstates[1] = 0
                        gamestate = 3
            
            hapi.handle_events = handle_events_mg

            targetcolor, targetcolorname = random.choice(colors.getcolornames())
            targetcolor = colorconv.hextorgb(targetcolor)
            x = 0
            targetcolor = list(targetcolor)
            for color in targetcolor:
                if color == 0:
                    targetcolor[x] = 1
                    x += 1
                else:
                    x += 1

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
        print(gamestate)
        if initstates[3] == 0:
            hapi.fill(themecols[0])
            hapi.rect(0, 0, window_width, window_height)

            def handle_events_res(event):
                global gamestate
                if event.type == pygame.QUIT:
                    print("exiting")
                    gamestate = 5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        initstates[3] = 0
                        gamestate = 0
                    if event.key == pygame.K_RETURN:
                        initstates[3] = 0
                        gamestate = 2
            hapi.handle_events = handle_events_res
            resultstext = MENUS_FONT.render("Your Results", 0, themecols[1])
            initstates[3] = 1
        
        while hapi.is_running:
            if gamestate != 3:
                break
            
            scoretext = [outline.render_outline(str(scoreperc[0])+"%" if scoreperc[0] < 100 else "Bigger than 100%!", MENUS_FONT, hapi.colors["white"], hapi.colors["red"]), outline.render_outline(str(scoreperc[1])+"%" if scoreperc[1] < 100 else "Bigger than 100%!", MENUS_FONT, hapi.colors["white"], hapi.colors["green"]), outline.render_outline(str(scoreperc[2])+"%" if scoreperc[2] < 100 else "Bigger than 100%!", MENUS_FONT, hapi.colors["white"], hapi.colors["blue"])]
            hapi.screen.blit(resultstext, ((window_width-resultstext.get_width())/2, 20))
            hapi.screen.blit(scoretext[0], ((window_width-scoretext[0].get_width())/2, 80))
            hapi.screen.blit(scoretext[1], ((window_width-scoretext[1].get_width())/2, 120))
            hapi.screen.blit(scoretext[2], ((window_width-scoretext[2].get_width())/2, 160))

            targetcolortext = outline.render_outline('Color given: '+', '.join(map(str, targetcolor))+' ('+targetcolorname+')', MENUS_FONT, hapi.colors["black"], targetcolor, 2)
            guesstext = outline.render_outline('Your guess: '+', '.join(map(str, score)), MENUS_FONT, hapi.colors["black"], score, 2)
            
            hapi.screen.blit(targetcolortext, ((window_width-targetcolortext.get_width())/2, 220))
            hapi.screen.blit(guesstext, ((window_width-targetcolortext.get_width())/2, 260))

            entercode = MENUS_FONT.render("Press Enter to continue,", 0, hapi.colors["grey"])
            esccode = MENUS_FONT.render("Or Escape to go to main menu.", 0, hapi.colors["grey"])
            hapi.screen.blit(entercode, ((window_width-entercode.get_width())/2, window_height-80))
            hapi.screen.blit(esccode, ((window_width-esccode.get_width())/2, window_height-40))
            
            hapi.flip_display()
            hapi.event_loop()
    elif gamestate == 4:
        print(gamestate)
        if initstates[4] == 0:
            hapi.fill(themecols[0])
            hapi.rect(0, 0, window_width, window_height)
            
            nothinghere = MENUS_FONT.render("Nothing here... yet...", 1, themecols[1])

            def handle_events_hlp(event):
                global gamestate
                if event.type == pygame.QUIT:
                    print("exiting")
                    gamestate = 5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        initstates[4] = 0
                        gamestate = 0

            initstates[4] = 1

        hapi.handle_events = handle_events_hlp
        
        while hapi.is_running:
            if gamestate != 4:
                break
            hapi.screen.blit(nothinghere, ((window_width-nothinghere.get_width())/2, 30))

            hapi.flip_display()
            hapi.event_loop()

    elif gamestate == 5:
        quit()
