import pygame
from tkinter import * #gui
import time

pygame.init()

# gui 창 만들기
root = Tk()
root.title("piano")
root.geometry('1920x700+0+0')

frame = Frame(root, bg="medium purple", bd=20, relief=RIDGE)
frame.grid()

frame1 = Frame(frame, bg="medium purple", bd=20, relief=RIDGE)
frame1.grid()
frame2 = Frame(frame, bg="medium purple", relief=FLAT)
frame2.grid()
frame3 = Frame(frame, bg="medium purple", relief=FLAT)
frame3.grid()

str1 = StringVar()
str1.set("Just Like Music")
Date1 = StringVar()
Time1 = StringVar()

Date1.set(time.strftime("%Y-%m-%d"))
Time1.set(time.strftime("%H:%M/%S"))

#======================백건 소리=============================
def value_C3_Click():
      str1.set("C3")
      sound = pygame.mixer.Sound("C3.wav")
      sound.play()

def value_D3_Click():
      str1.set("D3")
      sound = pygame.mixer.Sound("D3.wav")
      sound.play()

def value_E3_Click():
      str1.set("E3")
      sound = pygame.mixer.Sound("E3.wav")
      sound.play()

def value_F3_Click():
      str1.set("F3")
      sound = pygame.mixer.Sound("F3.wav")
      sound.play()

def value_G3_Click():
      str1.set("G3")
      sound = pygame.mixer.Sound("G3.wav")
      sound.play()

def value_A3_Click():
      str1.set("A3")
      sound = pygame.mixer.Sound("A3.wav")
      sound.play()

def value_B3_Click():
      str1.set("B3")
      sound = pygame.mixer.Sound("B3.wav")
      sound.play()

def value_C4_Click():
      str1.set("C4")
      sound = pygame.mixer.Sound("C4.wav")
      sound.play()

def value_D4_Click():
      str1.set("D4")
      sound = pygame.mixer.Sound("D4.wav")
      sound.play()

def value_E4_Click():
      str1.set("E4")
      sound = pygame.mixer.Sound("E4.wav")
      sound.play()

def value_F4_Click():
      str1.set("F4")
      sound = pygame.mixer.Sound("F4.wav")
      sound.play()

def value_G4_Click():
      str1.set("G4")
      sound = pygame.mixer.Sound("G4.wav")
      sound.play()

def value_A4_Click():
      str1.set("A4")
      sound = pygame.mixer.Sound("A4.wav")
      sound.play()

def value_B4_Click():
      str1.set("B4")
      sound = pygame.mixer.Sound("B4.wav")
      sound.play()

def value_C5_Click():
      str1.set("C5")
      sound = pygame.mixer.Sound("C5.wav")
      sound.play()


def value_D5_Click():
      str1.set("D5")
      sound = pygame.mixer.Sound("D5.wav")
      sound.play()


def value_E5_Click():
      str1.set("E5")
      sound = pygame.mixer.Sound("E5.wav")
      sound.play()


def value_F5_Click():
      str1.set("F5")
      sound = pygame.mixer.Sound("F5.wav")
      sound.play()


def value_G5_Click():
      str1.set("G5")
      sound = pygame.mixer.Sound("G5.wav")
      sound.play()


def value_A5_Click():
      str1.set("A5")
      sound = pygame.mixer.Sound("A5.wav")
      sound.play()


def value_B5_Click():
      str1.set("B5")
      sound = pygame.mixer.Sound("B5.wav")
      sound.play()

#======================흑건 소리=============================
def value_C3s_Click():
      str1.set("C3#")
      sound = pygame.mixer.Sound("C3s.wav")
      sound.play()

def value_D3s_Click():
      str1.set("D3#")
      sound = pygame.mixer.Sound("D3s.wav")
      sound.play()


def value_F3s_Click():
      str1.set("F3#")
      sound = pygame.mixer.Sound("F3s.wav")
      sound.play()

def value_G3s_Click():
      str1.set("G3#")
      sound = pygame.mixer.Sound("G3s.wav")
      sound.play()

def value_A3s_Click():
      str1.set("A3#")
      sound = pygame.mixer.Sound("A3s.wav")
      sound.play()

def value_C4s_Click():
      str1.set("C4#")
      sound = pygame.mixer.Sound("C4s.wav")
      sound.play()

def value_D4s_Click():
      str1.set("D4#")
      sound = pygame.mixer.Sound("D4s.wav")
      sound.play()


def value_F4s_Click():
      str1.set("F4#")
      sound = pygame.mixer.Sound("F4s.wav")
      sound.play()

def value_G4s_Click():
      str1.set("G4#")
      sound = pygame.mixer.Sound("G4s.wav")
      sound.play()

def value_A4s_Click():
      str1.set("A4#")
      sound = pygame.mixer.Sound("A4s.wav")
      sound.play()


def value_C5s_Click():
      str1.set("C5#")
      sound = pygame.mixer.Sound("C5s.wav")
      sound.play()


def value_D5s_Click():
      str1.set("D5#")
      sound = pygame.mixer.Sound("D5s.wav")
      sound.play()


def value_F5s_Click():
      str1.set("F5#")
      sound = pygame.mixer.Sound("F5s.wav")
      sound.play()


def value_G5s_Click():
      str1.set("G5#")
      sound = pygame.mixer.Sound("G5s.wav")
      sound.play()


def value_A5s_Click():
      str1.set("A5#")
      sound = pygame.mixer.Sound("A5s.wav")
      sound.play()

#======================백건 소리=============================
def pressKey(event):
      if (event.char == 'a'):
            str1.set("C3")
            sound = pygame.mixer.Sound("C3.wav")
            sound.play()

      if (event.char == 's'):
            str1.set("D3")
            sound = pygame.mixer.Sound("D3.wav")
            sound.play()

      if (event.char == 'd'):
            str1.set("E3")
            sound = pygame.mixer.Sound("E3.wav")
            sound.play()

      if (event.char == 'f'):
            str1.set("F3")
            sound = pygame.mixer.Sound("F3.wav")
            sound.play()

      if (event.char == 'g'):
            str1.set("G3")
            sound = pygame.mixer.Sound("G3.wav")
            sound.play()

      if (event.char == 'h'):
            str1.set("A3")
            sound = pygame.mixer.Sound("A3.wav")
            sound.play()

      if (event.char == 'j'):
            str1.set("B3")
            sound = pygame.mixer.Sound("B3.wav")
            sound.play()

      if (event.char == 'k'):
            str1.set("C4")
            sound = pygame.mixer.Sound("C4.wav")
            sound.play()

      if (event.char == 'l'):
            str1.set("D4")
            sound = pygame.mixer.Sound("D4.wav")
            sound.play()

      if (event.char == ';'):
            str1.set("E4")
            sound = pygame.mixer.Sound("E4.wav")
            sound.play()

      if (event.char == "'"):
            str1.set("F4")
            sound = pygame.mixer.Sound("F4.wav")
            sound.play()

      if (event.char == 'w'):
            str1.set("C3#")
            sound = pygame.mixer.Sound("C3s.wav")
            sound.play()

      if (event.char == 'e'):
            str1.set("D3#")
            sound = pygame.mixer.Sound("D3s.wav")
            sound.play()

      if (event.char == 't'):
            str1.set("F3#")
            sound = pygame.mixer.Sound("F3s.wav")
            sound.play()

      if (event.char == 'y'):
            str1.set("G3#")
            sound = pygame.mixer.Sound("G3s.wav")
            sound.play()

      if (event.char == 'u'):
            str1.set("A3#")
            sound = pygame.mixer.Sound("A3s.wav")
            sound.play()

      if (event.char == 'o'):
            str1.set("C4#")
            sound = pygame.mixer.Sound("C4s.wav")
            sound.play()

      if (event.char == 'p'):
            str1.set("D4#")
            sound = pygame.mixer.Sound("D4s.wav")
            sound.play()

      if (event.char == ']'):
            str1.set("F4#")
            sound = pygame.mixer.Sound("F4s.wav")
            sound.play()
'''
def value_G4(event):
      str1.set("G4")
      sound = pygame.mixer.Sound("G4.wav")
      sound.play()

def value_A4(event):
      str1.set("A4")
      sound = pygame.mixer.Sound("A4.wav")
      sound.play()

def value_B4(event):
      str1.set("B4")
      sound = pygame.mixer.Sound("B4.wav")
      sound.play()

def value_C5(event):
      str1.set("C5")
      sound = pygame.mixer.Sound("C5.wav")
      sound.play()


def value_D5(event):
      str1.set("D5")
      sound = pygame.mixer.Sound("D5.wav")
      sound.play()


def value_E5(event):
      str1.set("E5")
      sound = pygame.mixer.Sound("E5.wav")
      sound.play()


def value_F5(event):
      str1.set("F5")
      sound = pygame.mixer.Sound("F5.wav")
      sound.play()


def value_G5(event):
      str1.set("G5")
      sound = pygame.mixer.Sound("G5.wav")
      sound.play()


def value_A5(event):
      str1.set("A5")
      sound = pygame.mixer.Sound("A5.wav")
      sound.play()


def value_B5(event):
      str1.set("B5")
      sound = pygame.mixer.Sound("B5.wav")
      sound.play()
'''
#======================흑건 소리=============================

'''
def value_G4s(event):
      str1.set("G4#")
      sound = pygame.mixer.Sound("G4s.wav")
      sound.play()

def value_A4s(event):
      str1.set("A4#")
      sound = pygame.mixer.Sound("A4s.wav")
      sound.play()


def value_C5s(event):
      str1.set("C5#")
      sound = pygame.mixer.Sound("C5s.wav")
      sound.play()


def value_D5s(event):
      str1.set("D5#")
      sound = pygame.mixer.Sound("D5s.wav")
      sound.play()


def value_F5s(event):
      str1.set("F5#")
      sound = pygame.mixer.Sound("F5s.wav")
      sound.play()


def value_G5s(event):
      str1.set("G5#")
      sound = pygame.mixer.Sound("G5s.wav")
      sound.play()


def value_A5s(event):
      if(event.char == 'a'):
            str1.set("A5#")
            sound = pygame.mixer.Sound("A5s.wav")
            sound.play()
'''
#=======================Label with Title============================

Label(frame1, text="Piano",font=('arial', 25, 'bold'), padx=8, pady=8, bd=5, bg="medium purple",
      fg="white", justify=CENTER).grid(row=0, column=0, columnspan=4)

#=================================제목==================================

txtDisplay = Entry(frame1, textvariable=str1, font=('arial', 18, 'bold'), bd=34, bg="medium purple",
                   fg="white", justify=CENTER).grid(row=1, column=0)
txtDate = Entry(frame1, textvariable=Date1, font=('arial', 18, 'bold'), bd=34, bg="medium purple",
                   fg="white", justify=CENTER).grid(row=1, column=1)
txtTime = Entry(frame1, textvariable=Time1, font=('arial', 18, 'bold'), bd=34, bg="medium purple",
                   fg="white", justify=CENTER).grid(row=1, column=2)

#===============================백건 버튼====================================
ButtonWidth = 3
ButtonHeight = 4

btnC3 = Button(frame3,width=ButtonWidth, height=ButtonHeight, text="C3",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_C3_Click (),
      fg="black")
btnC3.grid(row=1, column=1)

btnD3 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="D3",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_D3_Click(),
      fg="black")
btnD3.grid(row=1, column=2)

btnE3 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="E3",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_E3_Click(),
      fg="black")
btnE3.grid(row=1, column=3)

btnF3 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="F3",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_F3_Click(),
      fg="black")
btnF3.grid(row=1, column=4)

btnG3 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="G3",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_G3_Click(),
      fg="black")
btnG3.grid(row=1, column=5)

btnA3 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="A3",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_A3_Click(),
      fg="black").grid(row=1, column=6)

btnB3 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="B3",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_B3_Click(),
      fg="black").grid(row=1, column=7)

btnC4 = Button(frame3,width=ButtonWidth, height=ButtonHeight, text="C4",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_C4_Click(),
      fg="black").grid(row=1, column=8)

btnD4 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="D4",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_D4_Click(),
      fg="black").grid(row=1, column=9)

btnE4 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="E4",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_E4_Click(),
      fg="black").grid(row=1, column=10)

btnF4 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="F4",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_F4_Click(),
      fg="black").grid(row=1, column=11)

btnG4 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="G4",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_G4_Click(),
      fg="black").grid(row=1, column=12)

btnA4 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="A4",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_A4_Click(),
      fg="black").grid(row=1, column=13)

btnB4 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="B4",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_B4_Click(),
      fg="black").grid(row=1, column=14)

btnC5 = Button(frame3,width=ButtonWidth, height=ButtonHeight, text="C5",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_C5_Click(),
      fg="black").grid(row=1, column=15)

btnD5 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="D5",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_D5_Click(),
      fg="black").grid(row=1, column=16)

btnE5 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="E5",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_E5_Click(),
      fg="black").grid(row=1, column=17)

btnF5 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="F5",font=('arial',25,'bold'),bd=5,bg="white",command=lambda :value_F5_Click(),
      fg="black").grid(row=1, column=18)

btnG5 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="G5",font=('arial',25,'bold'),bd=5,bg="white", command=lambda :value_G5_Click(),
      fg="black").grid(row=1, column=19)
btnA5 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="A5",font=('arial',25,'bold'),bd=5,bg="white", command=lambda :value_A5_Click(),
      fg="black").grid(row=1, column=20)
btnB5 = Button(frame3, width=ButtonWidth, height=ButtonHeight, text="B5",font=('arial',25,'bold'),bd=5,bg="white", command=lambda :value_B5_Click(),
      fg="black").grid(row=1, column=21)


#=================================흑건 버튼==================================

SharpButtonWidth = 3
SharpButtonHeight = 4
BlankSpaceWidth = 9

blankspace = Button(frame2, width=BlankSpaceWidth, height=SharpButtonHeight, state=DISABLED, bg="medium purple", relief=FLAT,
      fg="white").grid(row=0, column=0)

btnC3sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="C3#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_C3s_Click(),
      fg="white").grid(row=0, column=1)

btnD3sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="D3#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_D3s_Click(),
      fg="white").grid(row=0, column=2)

blankspace = Button(frame2, width=BlankSpaceWidth, height=SharpButtonHeight, state=DISABLED, bg="medium purple", relief=FLAT,
      fg="white").grid(row=0, column=3)

btnF3sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="F3#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_F3s_Click(),
      fg="white").grid(row=0, column=4)

btnG3sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="G3#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_G3s_Click(),
      fg="white").grid(row=0, column=5)

btnA3sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="A3#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_A3s_Click(),
      fg="white").grid(row=0, column=6)

blankspace = Button(frame2, width=BlankSpaceWidth, height=SharpButtonHeight, state=DISABLED, bg="medium purple", relief=FLAT,
      fg="white").grid(row=0, column=7)

btnC4sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="C4#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_C4s_Click(),
      fg="white").grid(row=0, column=8)

btnD4sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="D4#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_D4s_Click(),
      fg="white").grid(row=0, column=9)

blankspace = Button(frame2, width=BlankSpaceWidth, height=SharpButtonHeight, state=DISABLED, bg="medium purple", relief=FLAT,
      fg="white").grid(row=0, column=10)

btnF4sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="F4#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_F4s_Click(),
      fg="white").grid(row=0, column=11)

btnG4sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="G4#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_G4s_Click(),
      fg="white").grid(row=0, column=12)

btnA4sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="A4#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_A4s_Click(),
      fg="white").grid(row=0, column=13)

blankspace = Button(frame2, width=BlankSpaceWidth, height=SharpButtonHeight, state=DISABLED, bg="medium purple", relief=FLAT,
      fg="white").grid(row=0, column=14)

btnC5sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="C5#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_C5s_Click(),
      fg="white").grid(row=0, column=15)

btnD5sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="D5#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_D5s_Click(),
      fg="white").grid(row=0, column=16)

blankspace = Button(frame2, width=BlankSpaceWidth, height=SharpButtonHeight, state=DISABLED, bg="medium purple", relief=FLAT,
      fg="white").grid(row=0, column=17)

btnF5sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="F5#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_F5s_Click(),
      fg="white").grid(row=0, column=18)

btnG5sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="G5#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_G5s_Click(),
      fg="white").grid(row=0, column=19)
btnA5sharp = Button(frame2, width=SharpButtonWidth, height=SharpButtonHeight, text="A5#",font=('arial',25,'bold'),bd=5,bg="black", command=lambda :value_A5s_Click(),
      fg="white").grid(row=0, column=20)

blankspace = Button(frame2, width=BlankSpaceWidth, height=SharpButtonHeight, state=DISABLED, bg="medium purple", relief=FLAT,
      fg="white").grid(row=0, column=21)


root.bind("<KeyPress>", pressKey) # 키보드 입력 명령어


root.mainloop()