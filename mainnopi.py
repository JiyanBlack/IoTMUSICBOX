
import pygame
import json
import os
from os import listdir
from time import sleep  # used for tempo of songs
import multiprocessing
import msvcrt
#from randomflash import blinkblink

# https://beatproduction.net/piano-sound-kit/

listofsounds = []
pathbase = "/home/pi/Desktop/IoTMUSICBOX"
soundstr = ""

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

def getchar():
    # Returns a single character from standard input

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def pianomode_win():
    while True:
        print("Press 'q' to quit")
        pianopieces = {'twinkle':twinkle, 'ode_to_joy':ode_to_joy}
        print("Which sound effect would you like to choose? Input q to quit.")
        piece = input("Piano pieces you can choose are " + " ".join(pianopieces) +
                      " \n")

        if piece in pianopieces:            
            p1 = multiprocessing.Process(target = pianopieces[piece], args=())
            p2 = multiprocessing.Process(target = pianoplay_win, args=())
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            print("Piece completed")
            p1.terminate()
            p2.terminate()
        elif piece == 'q':
            print("Leaving piano mode")
            break
        else:
            print("No such song")

def pianoplay_win():
    pygame.mixer.init()
    getchar = _GetchWindows()
    with open("piano.json", 'r') as f:
        sounds = json.load(f)
        print("Press 'q' to quit")
        while True:
            if msvcrt.kbhit():
                ch = ord(getchar())
                ch = chr(ch)
                # print(ch)
                if ch == 'q':  # break when q is hit
                    print("Exiting")
                    break
                elif ch in sounds:
                    sounda = pygame.mixer.Sound(file=sounds[ch])
                    sounda.play()
                else:
                    continue

def pianomode_linux():
    while True:
        print("Press 'q' to quit")
        pianopieces = {'twinkle':twinkle, 'ode_to_joy':ode_to_joy}
        print("Which sound effect would you like to choose? Input q to quit.")
        piece = input("Piano pieces you can choose are " + " ".join(pianopieces) +
                      " \n")

        if piece in pianopieces:            
            p1 = multiprocessing.Process(target = pianopieces[piece], args=())
            p2 = multiprocessing.Process(target = pianoplay_linux, args=())
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            print("Piece completed")
            p1.terminate()
            p2.terminate()
        elif piece == 'q':
            print("Leaving piano mode")
            break
        else:
            print("No such song")    

def pianoplay_linux():
    pygame.init()
    pygame.mixer.init()    
    with open("piano.json", 'r') as f:
        sounds = json.load(f)
        print("Press 'q' to quit")
        while True:
            ch = getchar()
            if ch == 'q': 
                print("Exiting")
                break
            elif ch in sounds:
                print(sounds[ch])
                filepath = os.path.join(pathbase, sounds[ch])
                print(filepath)
                sounda = pygame.mixer.Sound(file=filepath)
                #blinkblink(0.2)
                sounda.play()
            else:
                print(ch)
                continue



def twinkle():
    speed = 0.5  # tempo of the piece, lower numbers are faster
    twinklesong = [['C', 1], ['C', 1], ['G', 1], ['G', 1], ['A', 1], ['A', 1],
                   ['G', 2], ['F', 1], ['F', 1], ['E', 1], ['E', 1], ['D', 1],
                   ['D',
                    1], ['C', 2], ['G', 1], ['G', 1], ['F', 1], ['F', 1], [
                        'E', 1
    ], ['E', 1], ['D', 2], ['G', 1], ['G', 1], ['F', 1], [
                        'F', 1
    ], ['E', 1], ['E', 1], ['D', 2], ['C', 1], ['C', 1], [
                        'G', 1
    ], ['G', 1], ['A', 1], ['A', 1], ['G', 2], ['F', 1],
        ['F', 1], ['E', 1], ['E', 1], ['D', 1], ['D', 1], ['C', 2]]
    for note, duration in twinklesong:
        print(note + '\n', end="")
        sleep(duration * speed)
    print("Press q to quit")
    return

def ode_to_joy():
    speed = 0.4  # tempo of the piece, lower numbers are faster
    odesong = [['e', 1], ['e', 1], ['f', 1], ['g', 1], ['g', 1], ['f', 1], [
        'e', 1
    ], ['d', 1], ['c', 1], ['c', 1], ['d', 1], ['e', 1], ['e', 1.5], [
        'd', 0.5
    ], ['d', 2], ['e', 1], ['e', 1], ['f', 1], ['g', 1], ['g', 1], ['f', 1], [
        'e', 1
    ], ['d', 1], ['c', 1], ['c', 1], ['d', 1], ['e', 1], ['d', 1.5], [
        'c', 0.5
    ], ['c', 2], ['d', 1], ['d', 1], ['e', 1], ['c', 1], ['d', 1], ['e', 0.5],
        ['f', 0.5], ['e', 1], ['c', 1], ['d', 1], ['e',
                                                   0.5], ['f', 0.5],
        ['e', 1], ['d', 1], ['c', 1], ['d', 1], ['G', 1], ['e', 1], [
        'e', 1
    ], ['f', 1], ['g', 1], ['g', 1], ['f', 1], ['e', 1], ['d', 1], [
        'c', 1
    ], ['c', 1], ['d', 1], ['e', 1], ['d', 1.5], ['c',
                                                  0.5], ['c', 2]]
    for note, duration in odesong:
        print(note + '\n', end="")
        sleep(duration * speed)
    print("Press q to quit")
    return


def win_player():
    pygame.mixer.init()
    getchar = _GetchWindows()
    global soundstr
    while True:
        print("Which sound effect would you like to choose?" , soundstr, "\nInput q to quit.")
        soundfile = input("Choose a sound file:")
        if soundfile == 'q':
            break
        if soundfile == 'piano':
            pianomode_win()
        soundfile = soundfile + '.json'
        try:
            with open(soundfile, 'r') as f:
                sounds = json.load(f)
                print("Press 'q' to quit")
                while True:
                    if msvcrt.kbhit():
                        ch = ord(getchar())
                        ch = chr(ch)
                        print(ch)
                        if ch == 'q':  # break when q is hit
                            print("Exiting")
                            break
                        elif ch in sounds:
                            print(sounds[ch])
                            filepath = os.path.join(pathbase, sounds[ch])
                            print(filepath)
                            sounda = pygame.mixer.Sound(file=filepath)
                            #blinkblink(0.2)
                            sounda.play()
                        else:
                            continue
        except Exception as e:
            print('No such music file!')


def linux_player():
    pygame.init()
    pygame.mixer.init()
    global soundstr
    while True:
        print("Which sound effect would you like to choose?" , soundstr, "\nInput q to quit.")
        soundfile = input("Choose a sound file:")
        if soundfile == 'q':
            break
        soundfile = soundfile + '.json'
        try:
            with open(soundfile, 'r') as f:
                sounds = json.load(f)
                print("Press 'q' to quit")
                while True:
                    ch = getchar()
                    if ch == 'q':  # break when q is hit
                        print("Exiting")
                        break
                    elif ch in sounds:
                        print(sounds[ch])
                        filepath = os.path.join(pathbase, sounds[ch])
                        print(filepath)
                        sounda = pygame.mixer.Sound(file=filepath)
                        #blinkblink(0.2)
                        sounda.play()
                    else:
                        print(ch)
                        continue
        except Exception as e:
            print(e)


def main():
    # filter out all json files
    global listofsounds, soundstr
    jsonfiles = filter(lambda x: x[-5:] == '.json', listdir('./'))
    listofsounds = map(lambda x: x[:-5], jsonfiles)
    soundstr = ", ".join(listofsounds) + "\n"
    if os.name == 'nt':
        win_player()
    else:
        global tty, termios, sys
        import tty
        import termios
        import sys
        linux_player()


if __name__ == '__main__':
    main()
