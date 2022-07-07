from datetime import *
import pygame

song = '02 Rick Astley - Never Gonna Give You Up.mp3'


def alarm():
    alarm_set = ''
    for i in range(3):
        alarm_inp = input("enter 'hour' and press enter after that 'minutes' and 'seconds': ")
        if (i == 0 and len(alarm_inp) == 1) or (i == 1 and len(alarm_inp) == 1):
            alarm_set += '0' + alarm_inp + ':'
        elif i == 2 and len(alarm_inp) == 1:
            alarm_set += '0' + alarm_inp
        else:
            if i == 2:
                alarm_set += alarm_inp
            else:
                alarm_set += alarm_inp + ':'
    print(alarm_set)

    while True:
        if datetime.now().strftime("%H:%M:%S") == alarm_set:
            pygame.init()
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            print('ring ring')

alarm()
