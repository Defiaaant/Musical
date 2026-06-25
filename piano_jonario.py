from tkinter import*
from tkinter import ttk
import os
import time
import threading

import pygame

#----------------------------------------------------------------------
#só pra testar essas variaveis

Gravando = False
Tempo_inicial = 0
Gravação_atual = []
Memoria_musical = {}

#----------------------------------------------------------------------
def tocar_som(entrada):
    global Gravando, Tempo_inicial, Gravação_atual
    if Gravando:
        tempo = time.time() - Tempo_inicial
        Gravação_atual.append((tempo, os.path.basename(entrada)))

    try:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(entrada))
    except:
        pass
     
#funções para gravação
def alternar_gravacao():
    global Gravando, Tempo_inicial, Gravação_atual
    if not Gravando:
        Gravando = True
        Gravação_atual = []
        Tempo_inicial = time.time()
        botão_g.config(bg = '#ffff44')
    #como vai ser o botão?

    else:
        Gravando = False
        botão_g.config(bg = '#ff4fff') 
        if Gravação_atual:
            from tkinter import simpledialog
            nome = simpledialog.askstring('Salvar', 'Nome da musica:')
            if nome:
                Memoria_musical[nome.strip()] = Gravação_atual

def tocar_da_memoria(nome_musica):
    def toca_musica():
            reprodutor = pygame.mixer.Channel(1)
            tempo_anterior = 0
            for tempo_atual, arquivo in Memoria_musical[nome_musica]:
                time.sleep(tempo_atual - tempo_anterior)
                try:
                    reprodutor.play(pygame.mixer.Sound(os.path.join(notas, arquivo)))
                except:
                    pass
                tempo_anterior = tempo_atual

    threading.Thread(target = toca_musica, daemon = True).start()
    
#----------------------------------------------------------------------

def seletor(event):
  janela = Toplevel()
  janela.config(background='#484886')
  janela.geometry('700x500')

  retorno=Button(janela, image=voltar, width=30, height=30,
                 bg='#484886',
                 activebackground="#484886", activeforeground="#484886",
                 relief='flat',
                 command=lambda: janela.destroy())
  retorno.pack(anchor='nw')

  Label(janela, text="Aperte no botão da música que quer escutar", image=img, compound='top',
        font=("Arial",12, 'bold'),
        fg="#ffffff", bg='#484886').pack(anchor='center')

  frame2=Frame(janela, relief=FLAT)

#juntar as musicas feitas por tigas as que forem gravadas
  if not Memoria_musical:
    Button(frame2, text= 'musga q tiago vai por (1)', command=NONE).pack(side='bottom')
    Button(frame2, text= 'musga q tiago vai por (2)', command=NONE).pack(side='bottom')
    Button(frame2, text= 'musga q tiago vai por (3)', command=NONE).pack(side='bottom')
    Button(frame2, text= 'musga q tiago vai por (4)', command=NONE).pack(side='bottom')
  else:
    Button(frame2, text= 'musga q tiago vai por (1)', command=NONE).pack(side='bottom')
    Button(frame2, text= 'musga q tiago vai por (2)', command=NONE).pack(side='bottom')
    Button(frame2, text= 'musga q tiago vai por (3)', command=NONE).pack(side='bottom')
    Button(frame2, text= 'musga q tiago vai por (4)', command=NONE).pack(side='bottom')
    for nome_musica in Memoria_musical.keys():
        Button(frame2, text=f"& {nome_musica}", command=lambda n=nome_musica: tocar_da_memoria(n)).pack(side='bottom', fill='x', pady=2)
      
  frame2.pack(padx=100, pady=100)

pygame.mixer.init()

base_dir = os.path.dirname(os.path.abspath(__file__))
notas = os.path.join(base_dir, "Notas")

#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

root = Tk()
root.geometry('700x500')

img = PhotoImage(file='pyano.png')
voltar = PhotoImage(file='voltar.png')
lista=PhotoImage(file='lista.png')

salvar=Label(root, image=lista, width=50, height=50, bg='#484886')
salvar.pack(anchor='nw')
salvar.bind("<Button-1>", seletor)

tecla1= PhotoImage(file='tecla2.png')
tecla2= PhotoImage(file='tecla3.png')
tecla3= PhotoImage(file='tecla1.png')
preta = PhotoImage(file='t_preta.png')

root.iconphoto(True, img)

root.config(background="#484886")

#botão né pae
botão_g = Button(root, text = 'gavar né pae', command = alternar_gravacao, bg = '#467830', font = ('Eczar', 15, 'bold'))
botão_g.pack(pady = 5)

frame=Frame(root, relief=FLAT)

Pyano=Label(root, image=img,
            text ='PYANO',
            font=('Lato', 50),
            background="#484886",
            compound='right',
            border=4, padx= 4, pady= 4,
            relief='flat')
Pyano.pack(anchor='center')
#Pyano.bind("<Button-1>", seletor)

#------------------------------------------
Do = Button(frame, image=tecla1,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "Do.wav"))).pack(side=LEFT)
#------------------------------------------
Re = Button(frame, image=tecla2,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "Re.wav"))).pack(side=LEFT)
#------------------------------------------
Mi = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "Mi.wav"))).pack(side=LEFT)
#------------------------------------------
Fa = Button(frame, image=tecla1,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "Fa.wav"))).pack(side=LEFT)
#------------------------------------------
Sol = Button(frame, image=tecla2,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "Sol.wav"))).pack(side=LEFT)
#------------------------------------------
La = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "La.wav"))).pack(side=LEFT)
#------------------------------------------
Si = Button(frame, image=tecla1,
             width=30, height=130, 
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "Si.mp3"))).pack(side=LEFT)
#------------------------------------------
Do_ = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "Do#.wav"))).pack(side=LEFT)
#------------------------------------------

frame.pack(padx=100, pady=100)

root.mainloop()
