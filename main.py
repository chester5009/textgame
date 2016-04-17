#-*-coding: cp1251 -*-
import sys
import tty
from unit import Unit
import locale
from django.utils.autoreload import termios
import os

clear=lambda: os.system('clear')

class _Getch:
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
            tty.setraw(sys.stdin.fileno())
            ch=sys.stdin.read(1)
        finally:
           termios.tcsetattr(fd,termios.TCSANOW,old_settings)
        return ch
    
        

class _GetchWindows:
    def __init__(self):
        import msvcrt
    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch=_Getch()
symbol=getch()

print symbol

gameArea=[[1,1,1,1,1,1],
          [1,0,0,0,0,1],
          [1,0,0,0,0,1],
          [1,0,0,2,0,1],
          [1,0,0,0,0,1],
          [1,1,1,1,1,1]]
def showField(f):
    for i in range(len(f)):
        oneRow = ""
        for j in range(len(f[i])):
            oneRow+= str(f[i][j]);
        print oneRow
    pass

def main():
    
    showField(gameArea)
    clear()
    coding = sys.getdefaultencoding()
    preferCoding=locale.getpreferredencoding()
    consoleCoding=sys.stdout.encoding
    print coding+" "+preferCoding+" "+consoleCoding
    print u"������� ��� ��������� .."
    name=raw_input()
    
    print u"������,"+unicode(name,consoleCoding)+u",������ ����� ���������.."
    print u"1-���� 2-��������� 3-���������..."
    typeHeroe=raw_input()
    
    if typeHeroe=="1":
        myHeroe=Unit(name, 12, 12, 6, 7, 6,u"����")
    elif typeHeroe=="2":
        myHeroe=Unit(name, 17, 17, 2, 3, 10,u"���������")
    elif typeHeroe=="3":
        myHeroe=Unit(name, 10, 10, 5, 12, 5,u"���������")
    
    print u"�������� ������ \n"
    print u"����� :"+myHeroe.get_type()
    print u"��� :"+unicode(myHeroe.get_name(),consoleCoding)
    print u"�������� :"+str(myHeroe.get_hp())
    print u"����������� ����� :"+str(myHeroe.get_min_damage())
    print u"������������ ����� :"+str(myHeroe.get_max_damage())
    print u"������ :"+str(myHeroe.get_defence())
    
    getch()
    
    while(True):
        
        showField(gameArea)
        c=getch()
        print c
        if c==' ':
            sys.exit()
        
        pass
    
    pass

main();

    