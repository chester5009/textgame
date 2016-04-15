#-*-coding: cp1251 -*-
import sys
import msvcrt
from unit import Unit


"""class _Getch:
    def __init__(self):
        try:
            self.impl= _GetchWindows()
        except ImportError:
            self.impl=_GetchLinux()
    
    def __call__(self): return self.impl()   

class _GetchLinux:
    def __init__(self):
        import tty,sys
    def __call__(self):
        import sys,tty
        fd=sys.stdin.fileno()
        old_settings=termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch=sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
        return ch
    
        

class _GetchWindows:
    def __init__(self):
        import msvcrt
    def __call__(self):
        import msvcrt
        return msvcrt.getch()"""


   

    



def main():
    
    print u"Введите имя персонажа .."
    name=raw_input()
    
    print u"Привет,"+unicode(name,'cp1251')+u"выбери класс персонажа.."
    typeHeroe=raw_input()
    #typeHeroe=raw_input()
    pass

main();

    