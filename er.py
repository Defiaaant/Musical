from tkinter import*
from tkinter import simpledialog
import pygame
#----------------------------------------------------------------------
def tocar_som(entrada):
  nota = pygame.mixer.Sound(entrada)
  nota.play()

def toca_musica():
  janela = Tk()
  janela.title("Seleção de Musicas")
  janela.geometry('200x300')
  janela.config="#000000"
  label =Label(janela, Text="Aperte no botão da música que quer escutar", font=("Arial",12))
  label.pack(pady=10)

  janela.mainloop()
              

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
             command=lambda n=str("Do.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Re = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Re.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Mi = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Mi.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Fa = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Fa.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Sol = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Sol.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
La = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("La.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Si = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Si.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Do_ = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Do#.wav"):tocar_som(n)).pack(side='left')
#------------------------------------------
Toca_Musica = Button(root, image=preta,
             bg='#000000',
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command= toca_musica()).pack(side='left')




teclas= Frame(root)

teclas.pack()

root.mainloop()
