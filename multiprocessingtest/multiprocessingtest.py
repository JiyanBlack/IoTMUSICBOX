# importing the multiprocessing module
import multiprocessing
from time import sleep
import pygame
import msvcrt
   

def ode_to_joy():
    speed = 0.04  # tempo of the piece, lower numbers are faster
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
        print(note, end="", flush=True)
        
        sleep(duration * speed)

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen.
Getch class taken from https://github.com/ActiveState/code"""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()




sounds = {'a': 'bell.wav', 'b': 'crow.wav', 'c': 'suction.wav',
'd': 'mower.wav', 'e': 'oogahhorn.wav', 'f': 'woodsaw.wav',
'g': 'meow.wav'}

def kb():
    #pygame.init()
    pygame.mixer.init()
    while True:
        if msvcrt.kbhit():
            ch = ord(getch())
            ch = chr(ch)
            #print(ch)
            if ch == 'q': #break when q is hit
                #print("Exiting")
                break
            elif ch in sounds:
                #print(sounds[ch])
                sounda = pygame.mixer.Sound(file = sounds[ch])
                sounda.play()
            else:
                #print(ch)
                continue    


if __name__ == "__main__":
    # creating processes
    while True:
        p1 = multiprocessing.Process(target = ode_to_joy, args =())
        p2 = multiprocessing.Process(target = kb, args =())
     
        # starting process 1
        p1.start()
        # starting process 2
        p2.start()
     
        # wait until process 1 is finished
        p1.join()
        # wait until process 2 is finished
        p2.join()
     
        # both processes finished
        print("Done !")
        p1.terminate()
        p2.terminate()