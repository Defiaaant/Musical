from tkinter import*
import os
import time
import threading
import pygame
import musica1

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

def alternar_gravacao():
    global Gravando, Tempo_inicial, Gravação_atual
    if not Gravando:
        Gravando = True
        botao.config(bg = 'grey')
        Gravação_atual = []
        Tempo_inicial = time.time()
    else:
        Gravando = False
        botao.config(bg = '#c3ba67')
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

  if not Memoria_musical:
    b1=Button(frame2, text= 'musga q tiago vai por (1)', command=NONE).pack(side='bottom')
    b2=Button(frame2, text= 'Sound_Track', command= lambda: musica1.Sound_Track()).pack(side='bottom')
    b3=Button(frame2, text= 'twinkle_twinkle_little_star', command= lambda: musica1.twinkle_twinkle_little_star()).pack(side='bottom')
    b4=Button(frame2, text= 'Parabéns pra você', command= lambda: musica1.parabens()).pack(side='bottom')
  else:
    b1=Button(frame2, text= 'musga q tiago vai por (1)', command=NONE).pack(side='bottom')
    b2=Button(frame2, text= 'Sound_Track', command= lambda: musica1.Sound_Track()).pack(side='bottom')
    b3=Button(frame2, text= 'twinkle_twinkle_little_star', command= lambda: musica1.twinkle_twinkle_little_star()).pack(side='bottom')
    b4=Button(frame2, text= 'Parabéns pra você', command= lambda: musica1.parabens()).pack(side='bottom')

    for nome_musica in Memoria_musical.keys():
        Button(frame2, text=f"{nome_musica}", command=lambda n=nome_musica: tocar_da_memoria(n)).pack(side='bottom', fill='x', pady=2)

  frame2.pack(padx=100, pady=100)

pygame.mixer.init()

base_dir = os.path.dirname(os.path.abspath(__file__))
notas = os.path.join(base_dir, "Notas")

#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

root = Tk()
root.geometry('700x600')

img = PhotoImage(file='pyano.png')
voltar = PhotoImage(file='voltar.png')
lista=PhotoImage(file='lista.png')

salvar=Label(root, image=lista, width=50, height=50, bg='#484886')
salvar.pack(anchor='nw')
salvar.bind("<Button-1>", seletor)

branca=PhotoImage(file='branca.png')
preta = PhotoImage(file='t_preta.png')

root.iconphoto(True, img)

root.config(width=800, height=500, background="#484886")

frame=Frame(root, relief=FLAT)

Pyano=Label(root, image=img,
            text ='PYANO',
            font=('Lato', 50),
            background="#484886",
            compound='right',
            border=4, padx= 4, pady= 4,
            relief='flat')
Pyano.pack(anchor='center')

#------------------------------------------
Do = Button(frame, image=branca,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "c1.wav"))).pack(side=LEFT)
#------------------------------------------
Re = Button(frame, image=branca,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "d1.wav"))).pack(side=LEFT)
#------------------------------------------
Mi = Button(frame, image=branca,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "e1.wav"))).pack(side=LEFT)
#------------------------------------------
Fa = Button(frame, image=branca,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "f1.wav"))).pack(side=LEFT)
#------------------------------------------
Sol = Button(frame, image=branca,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "g1.wav"))).pack(side=LEFT)
#------------------------------------------
La = Button(frame, image=branca,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "a1.wav"))).pack(side=LEFT)
#------------------------------------------
Si = Button(frame, image=branca,
             width=30, height=130, 
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "b1.wav"))).pack(side=LEFT)
#------------------------------------------
Do_ = Button(frame, image=branca,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "c2.wav"))).pack(side=LEFT)
#------------------------------------------

frame.pack(padx=100, pady=100)

botao = Button(root, text = 'Clique aqui para gravar ou parar de gravar a sua música',
                command = alternar_gravacao, relief= 'flat',
                bg = "#c3ba67", fg='black',
                activebackground='#c3ba67', activeforeground='#000000', border=2,
                padx=1, pady=1,
                font = ('Eczar', 15, 'bold'))
botao.pack(pady=5)

root.mainloop()
