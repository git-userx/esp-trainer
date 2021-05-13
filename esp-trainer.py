
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pygame==1.9.6
# written by __gituserx__
# box200a@gmail.com  Daytona Beach Florida USA..

"""
The player is presented with four colored squares. For each trial, one has been selected at random by the ESP Trainer.
Your task is to choose the correct square.
If you succeed, you will hear a chime, feel a vibration, and see a large color picture. Otherwise, the system lights up
 the correct square, and you proceed with the next trial. The score indicator at the top counts the number of correct
 choices. Words of encouragement appear as you achieve the scoring levels of 6, 8. 10, 12 or 14 hits. After 24 trials
  you may begin a new game.
The game offers multi-sensory feedback, reinforcement, and an opportunity to Pass, meeting all the requirements needed
for learning this skill. ESP Trainer improves your ability to recognize your intuitive impressions, and it can bring
 you to a level of intuitive awareness beyond anything you've experienced before.
The purpose of the trainer is to allow you to become aware of what it feels like when you psychically choose the correct
square. When you don't have that special feeling, we encourage you to press the Pass button. (So this is not a "forced
 choice" test.)
In a year long NASA program with 145 subjects (under Contract 953653 NAS7-100) many were able to significantly improve
their scores. Four of the subjects improved their scores at the hundred-to-one level or better. This approach has been
used with surprising success on Wall Street. But of course, past results are no guarantee of future performance.
Because you are learning a new skill, slower is better than faster.
If you find yourself frequently scoring 12, write to the original developer Russell Targ:
                                                                             Contact Russell Targ @: https://espresearch.com/russells-contact-form/
This game can provide the first steps toward experiencing and developing the psychic abilities hidden within us all.
"""


# TODO: score blocks logic!!!
# TODO: get score image
# TODO: reset loop line-113
# TODO:  cleanup code!



import random
import pygame
import time

# TODO: create some RGBA surfaces and fill them with the semi transparent colors for opaque buttons


pygame.init()

# ---- color pallet ---- #
white = (255, 255, 255)
white_smoke = (224, 224, 224)
white_dark_smoke = (202, 202, 202)
black = (0, 0, 0)
gray = (128, 128, 128)

purple = (146, 39, 143)
dark_purple = (126, 34, 123)
dark_dark_purple = (106, 29, 103)
gold = (248, 147, 31)
dark_gold = (208, 127, 11)
dark_dark_gold = (188, 107, 0)
lt_blue = (9, 130, 205)
dark_lt_blue = (0, 110, 185)
dark_dark_lt_blue = (0, 70, 131)
red = (255, 0, 0)
dark_red = (180, 0, 0)
dark_dark_red = (150, 0, 0)
green = (0, 255, 0)
dark_green = (0, 180, 0)
dark_dark_green = (0, 150, 0)
blue = (0, 0, 219)
dark_blue = (0, 0, 168)
dark_dark_blue = (25, 25, 112)
yellow = (255, 255, 0)
dark_yellow = (219, 219, 0)
dark_dark_yellow = (168, 168, 0)
# magenta = (255, 0, 255)

# --- game display properties --- #
display_width = 460
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(black)
clock = pygame.time.Clock()


# mainLoop = True


def game_loop():
    mainLoop = True
    return mainLoop


def click():
    getClick = pygame.mouse.get_pressed()
    return getClick


def pos():
    position = pygame.mouse.get_pos()
    return position


def rand_color():  # get a random color
    colors = ['red', 'green', 'blue', 'yellow']
    newcolor = random.choice(colors)
    random.shuffle(colors)
    return newcolor


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def text_objects_Two(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def small_text():
    return pygame.font.Font('freesansbold.ttf', 20)


def score_box(color, left, top, width, height):  # (white, 50, 40, 350, 30)
    # pygame.Rect(left, top, width, height), line weight) line weight for framed
    draw = pygame.draw.rect(gameDisplay, color, (left, top, width, height))
    return draw



def score_blocks(color, left, top, width, height):  # use a list of coordinates to control were blocks go
    """
    :param color: green, red
    :param left: 50
    :param top:  40
    :param width: 350
    :param height: 30
    :return: draw
    """
    draw = pygame.draw.rect(gameDisplay, color, (left, top, width, height))
    return draw


def gameGrid():
    pygame.draw.rect(gameDisplay, red, (110, 140, 100, 100))  # inactive
    if 110 + 100 > pos()[0] > 110 and 140 + 100 > pos()[1] > 140:
        pygame.draw.rect(gameDisplay, dark_red, (110, 140, 100, 100))  # hover
        if click()[0] == 1:
            pygame.draw.rect(gameDisplay, dark_dark_red, (110, 140, 100, 100))  # onclick
    pygame.draw.rect(gameDisplay, blue, (230, 140, 100, 100))  # inactive
    if 230 + 100 > pos()[0] > 230 and 140 + 100 > pos()[1] > 140:
        pygame.draw.rect(gameDisplay, dark_blue, (230, 140, 100, 100))  # hover
        if click()[0] == 1:
            pygame.draw.rect(gameDisplay, dark_dark_blue, (230, 140, 100, 100))  # onclick
    pygame.draw.rect(gameDisplay, yellow, (110, 260, 100, 100))  # inactive
    if 110 + 100 > pos()[0] > 110 and 260 + 100 > pos()[1] > 260:
        pygame.draw.rect(gameDisplay, dark_yellow, (110, 260, 100, 100))  # hover
        if click()[0] == 1:
            pygame.draw.rect(gameDisplay, dark_dark_yellow, (110, 260, 100, 100))  # onclick
    pygame.draw.rect(gameDisplay, green, (230, 260, 100, 100))  # inactive
    if 230 + 100 > pos()[0] > 230 and 260 + 100 > pos()[1] > 260:
        pygame.draw.rect(gameDisplay, dark_green, (230, 260, 100, 100))  # hover
        if click()[0] == 1:
            pygame.draw.rect(gameDisplay, dark_dark_green, (230, 260, 100, 100))  # onclick


def button(mesg, x, y, w, h, inactive_color, active_color, on_click_color):
    if x + w > pos()[0] > x and y + h > pos()[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, w, h))  # button active HOVER
        small_text()
        textSurf, textRect = text_objects(mesg, small_text())
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)
        if click()[0] == 1:  # button active ON CLICK
            pygame.draw.rect(gameDisplay, on_click_color, (x, y, w, h))
        small_text()
        textSurf, textRect = text_objects(mesg, small_text())
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, w, h))  # button inactive
        small_text()
        textSurf, textRect = text_objects(mesg, small_text())
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)


def message_display(text):  # relies on def score line 141
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects_Two(text, largeText, )
    TextRect.left = 100
    TextRect.top = 44.75
    # TextRect.center = (display_width/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update(TextRect)
    time.sleep(2)
    gameDisplay.fill(black)


def display_info():  # score blit
    message_display('wrong the color was {}'.format(getcolor))


# _____ variables _____ #
wrong_answer = True
score = 0
attempts = 0
cell_click = 0
getcolor = rand_color()
print(getcolor)


# ----------  Main Program Loop ---------- #

def score_progress_bar():
    # draw a green or red rec according to if answer is right or not
    if score == 1:
        score_block = {'left': 50, 'top': 40, 'width': 25, 'height': 30}
        # return score_block.values()
        left = score_block['left']
        top = score_block['top']
        width = score_block['width']
        height = score_block['height']
        color = green
        draw = pygame.draw.rect(gameDisplay, color, (left, top, width, height))
        return draw

    elif score == 2:
        score_block = {'left': 77, 'top': 40, 'width': 25, 'height': 30}
        color = green
        left = score_block['left']
        top = score_block['top']
        width = score_block['width']
        height = score_block['height']
        draw = pygame.draw.rect(gameDisplay, color, (50, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (left, top, width, height))
        return draw

    elif score == 3:
        score_block = {'left': 104, 'top': 40, 'width': 25, 'height': 30}
        color = green
        left = score_block['left']
        top = score_block['top']
        width = score_block['width']
        height = score_block['height']
        draw = pygame.draw.rect(gameDisplay, color, (50, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (77, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (left, top, width, height))
        return draw

    elif score == 4:
        score_block = {'left': 131, 'top': 40, 'width': 25, 'height': 30}
        color = green
        left = score_block['left']
        top = score_block['top']
        width = score_block['width']
        height = score_block['height']
        draw = pygame.draw.rect(gameDisplay, color, (50, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (77, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (104, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (left, top, width, height))
        return draw

    elif score == 5:  # STARTHERE: 1!!!!!
        score_block = {'left': 158, 'top': 40, 'width': 25, 'height': 30}
        color = green
        left = score_block['left']
        top = score_block['top']
        width = score_block['width']
        height = score_block['height']
        draw = pygame.draw.rect(gameDisplay, color, (50, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (77, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (104, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (131, 40, 25, 30)), \
               pygame.draw.rect(gameDisplay, color, (left, top, width, height))
        return draw


while game_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEMOTION:
            # print(pygame.mouse.get_pos())  # testing!
            pass

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 300 + 100 > pos()[0] > 300 and 460 + 100 > pos()[1] > 460:
                button('QUIT', 300, 460, 100, 50, lt_blue, dark_lt_blue, dark_dark_lt_blue)
                pygame.display.update()
                quit()

            # pos = pygame.mouse.get_pos()
            if 110 + 100 > pos()[0] > 110 and 140 + 100 > pos()[1] > 140 and getcolor is 'red':
                getcolor = rand_color()  # updates getcolor
                score += 1
                attempts += 1
                score_progress_bar()
                print('score = {}' ' \n ' 'color = {}'.format(score, getcolor))
                break

            if 230 + 100 > pos()[0] > 230 and 140 + 100 > pos()[1] > 140 and getcolor is 'blue':
                getcolor = rand_color()
                score += 1
                attempts += 1
                print('score = {}' ' \n ' 'color = {}'.format(score, getcolor))
                break

            if 110 + 100 > pos()[0] > 110 and 260 + 100 > pos()[1] > 260 and getcolor is 'yellow':
                getcolor = rand_color()
                score += 1
                attempts += 1
                print('score = {}' ' \n ' 'color = {}'.format(score, getcolor))
                break

            if 230 + 100 > pos()[0] > 230 and 260 + 100 > pos()[1] > 260 and getcolor is 'green':
                getcolor = rand_color()
                score += 1
                attempts += 1
                print('score = {}' ' \n ' 'color = {}'.format(score, getcolor))
                break

            if 40 + 100 > pos()[0] > 40 and 460 + 50 > pos()[1] > 460:  # reset button
                score = 0
                attempts += 1
                getcolor = rand_color()
                print('reset the game', 'score = {} the new color is {}'.format(score, getcolor))
                break

            else:
                if 170 + 100 > pos()[0] > 170 and 460 + 50 > pos()[1] > 460:  # pass button
                    attempts += 0
                    getcolor = rand_color()
                    print('pass', getcolor)
                    break

                else:  # wrong answer
                    attempts += 1
                    display_info()
                    print('wrong', getcolor, attempts)
                    getcolor = rand_color()
                    print('the new color is {}'.format(getcolor))
                    break

            # \TODO\  write test for attempts start / stop game

    else:  # draw the game board and user interface
        score_box(white, 50, 40, 347, 30)
        score_progress_bar()
        gameGrid()
        button('RESET', 40, 460, 100, 50, purple, dark_purple, dark_dark_purple)
        button('PASS', 170, 460, 100, 50, gold, dark_gold, dark_dark_gold)
        button('QUIT', 300, 460, 100, 50, lt_blue, dark_lt_blue, dark_dark_lt_blue)

    pygame.display.update()
    clock.tick(60)
