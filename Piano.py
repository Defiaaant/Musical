from tkinter import*
import pygame
#----------------------------------------------------------------------
def Do():
  nota = pygame.mixer.Sound("Do.wav")
  nota.play()
#----------------------------------------------------------------------
def Re():
  nota = pygame.mixer.Sound("Re.wav")
  nota.play()
#----------------------------------------------------------------------
def Mi():
  nota = pygame.mixer.Sound("Mi.wav")
  nota.play()
#----------------------------------------------------------------------
def Fa():
  nota = pygame.mixer.Sound("Fa.wav")
  nota.play()
#----------------------------------------------------------------------
def Sol():
  nota = pygame.mixer.Sound("Sol.wav")
  nota.play()
#----------------------------------------------------------------------
def La():
  nota = pygame.mixer.Sound("La.wav")
  nota.play()
#----------------------------------------------------------------------
def Si():
  nota = pygame.mixer.Sound("Si.mp3")
  nota.play()
#----------------------------------------------------------------------
def Do_():
  nota = pygame.mixer.Sound("Do (octave).wav")
  nota.play()

pygame.mixer.init()

#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

root = Tk()
root.geometry('600x400')

img = PhotoImage(file='piano.png')
preta = PhotoImage(file='t_preta.png')
root.iconphoto(True, img)

root.config(background="#484886")

Do = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=Do).pack(side=LEFT)
#------------------------------------------
Re = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=Re).pack(side=LEFT)
#------------------------------------------
Mi = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=Mi).pack(side=LEFT)
#------------------------------------------
Fa = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=Fa).pack(side=LEFT)
#------------------------------------------
Sol = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=Sol).pack(side=LEFT)
#------------------------------------------
La = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=La).pack(side=LEFT)
#------------------------------------------
Si = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=Si).pack(side=LEFT)
#------------------------------------------
Do_ = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=Do_).pack(side='left')
#------------------------------------------

teclas= Frame(root)

teclas.pack()

root.mainloop()