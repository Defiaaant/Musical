from tkinter import*
import os
import time
import threading
import pygame
import repertório
import json

Gravando = False
Tempo_inicial = 0
Gravação_atual = []
Memoria_musical = {}

base_dir = os.path.dirname(os.path.abspath(__file__))
notas =  os.path.join(base_dir, 'notas')
Salvar_notas = os.path.join(base_dir, 'musicas_salvas')

def carregar_musicas_memoria():
   global Memoria_musical
   if os.path.exists(Salvar_notas):
      try:
         with open(Salvar_notas, 'r', encoding='utf-8') as arquivo:
            Memoria_musical = json.load(arquivo)
      except:
         Memoria_musical = {}

carregar_musicas_memoria()

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

                try:
                    with open(Salvar_notas, 'w', encoding= 'utf-8') as arquivo:
                        json.dump(Memoria_musical, arquivo, indent= 4)
                except Exception as e:
                   print('Erro ao salvar:', e)
                   
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

  retorno=Button(janela, image=voltar, width=50, height=50,
                 bg='#484886',
                 activebackground="#484886", activeforeground="#484886",
                 relief='flat',
                 command=lambda: janela.destroy())
  retorno.pack(anchor='nw')

  Label(janela, text="Aperte no botão da música que quer escutar", image=img, compound='top',
        font=("Arial",12, 'bold'),
        fg="#ffffff", bg='#484886').pack(anchor='center')

  frame2=Frame(janela, relief=FLAT, bg='#484886')

  if not Memoria_musical:

    b=Button(frame2, text= 'Soundtrack', command=lambda: repertório.Sound_Track()).pack(side='bottom')
    b_=Button(frame2, text= 'Brilha brilha estrelinha', command=lambda: repertório.twinkle_twinkle_little_star()).pack(side='bottom')
    b_b=Button(frame2, text= 'Parabéns pra você', command= lambda: repertório.parabens()).pack(side='bottom')
  else:
 
    b=Button(frame2, text= 'Soundtrack', command=lambda: repertório.Sound_Track()).pack(side='bottom')
    b_=Button(frame2, text= 'Brilha brilha estrelinha', command= lambda: repertório.twinkle_twinkle_little_star()).pack(side='bottom')
    b_b=Button(frame2, text= 'Parabéns pra você', command= lambda: repertório.parabens()).pack(side='bottom')

    for nome_musica in Memoria_musical.keys():
        Button(frame2, text=f"{nome_musica}", command=lambda n=nome_musica: tocar_da_memoria(n)).pack(side='bottom', fill='x', pady=2)

  frame2.pack(padx=70, pady=70)

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

root.config(background="#484886")

frame=Frame(root, relief=FLAT)
bl=Frame(root, relief=FLAT, bg="#484886")

Pyano=Label(root, image=img,
            text ='PYANO',
            font=('Lato', 50),
            background="#484886",
            compound='right',
            border=4, padx= 4, pady= 4,
            relief='flat')
Pyano.pack(anchor='center')


'''Teclas Brancas'''

#------------------------------------------
Do = Button(frame, image=branca,text='C1', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "c1.wav"))).pack(side=LEFT)
#------------------------------------------
Re = Button(frame, image=branca, text= 'D1', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "d1.wav"))).pack(side=LEFT)
#------------------------------------------
Mi = Button(frame, image=branca, text='E1', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "e1.wav"))).pack(side=LEFT)
#------------------------------------------
Fa = Button(frame, image=branca, text='F1', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "f1.wav"))).pack(side=LEFT)
#------------------------------------------
Sol = Button(frame, image=branca, text= 'G1', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "g1.wav"))).pack(side=LEFT)
#------------------------------------------
La = Button(frame, image=branca, text='A1', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "a1.wav"))).pack(side=LEFT)
#------------------------------------------
Si = Button(frame, image=branca, text= 'B1', compound='center',
             width=30, height=130, 
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "b1.wav"))).pack(side=LEFT)
#------------------------------------------
Do_ = Button(frame, image=branca, text='C2', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "c2.wav"))).pack(side=LEFT)
#------------------------------------------
Re_ = Button(frame, image=branca, text='D2', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "d2.wav"))).pack(side=LEFT)
#------------------------------------------
Mi_ = Button(frame, image=branca, text='E2', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "e2.wav"))).pack(side=LEFT)
#------------------------------------------
Fa_ = Button(frame, image=branca, text='F2', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "f2.wav"))).pack(side=LEFT)
#------------------------------------------
Sol_ = Button(frame, image=branca, text='G2', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "g2.wav"))).pack(side=LEFT)
#------------------------------------------
La_ = Button(frame, image=branca, text='A2', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "a2.wav"))).pack(side=LEFT)
#------------------------------------------
Si_ = Button(frame, image=branca, text='B2', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "b2.wav"))).pack(side=LEFT)
#------------------------------------------
Do__ = Button(frame, image=branca, text='C3', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "c3.wav"))).pack(side=LEFT)
#------------------------------------------
Re__ = Button(frame, image=branca, text='D3', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "d3.wav"))).pack(side=LEFT)
#------------------------------------------
Mi__ = Button(frame, image=branca, text='E3', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "e3.wav"))).pack(side=LEFT)
#------------------------------------------
Fa__ = Button(frame, image=branca, text='F3', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "f3.wav"))).pack(side=LEFT)
#------------------------------------------
Sol__ = Button(frame, image=branca, text='G3', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "g3.wav"))).pack(side=LEFT)
#------------------------------------------
La__ = Button(frame, image=branca, text='A3', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "a3.wav"))).pack(side=LEFT)
#------------------------------------------
Si__ = Button(frame, image=branca, text='B3', compound='center',
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "b3.wav"))).pack(side=LEFT)
#------------------------------------------



'''Teclas pretas '''

#------------------ AQUIIII TIAGOOOO YUHUUUUUUUUUUUUL ------------------------
Button(bl, image=preta, text='CD1', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "cd1.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='DE1', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "de1.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='FG1', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "fg1.wav"))).pack(side=LEFT, padx=15)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='GA1', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "ga1.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='AB1', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "ab1.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
Button(bl, image=preta, text='CD2', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "cd2.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='DE2', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "de2.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='FG2', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "fg2.wav"))).pack(side=LEFT, padx=15)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='GA2', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "ga2.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='AB2', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "ab2.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
Button(bl, image=preta, text='CD3', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "cd3.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='DE3', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "de3.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='FG3', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "fg3.wav"))).pack(side=LEFT, padx=15)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='GA3', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "ga3.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------
Button(bl, image=preta, text='AB3', fg='#ffffff', compound='center',
             width=15, height=65,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "ab3.wav"))).pack(side=LEFT, padx=1)
#-----------------------------------------------------------------------------







bl.pack()
frame.pack(padx=10)

botao = Button(root, text = 'Clique aqui para gravar ou parar de gravar a sua música',
                command = alternar_gravacao, relief= 'flat',
                bg = "#c3ba67", fg='black',
                activebackground='#c3ba67', activeforeground='#000000', border=2,
                padx=1, pady=1,
                font = ('Eczar', 15, 'bold'))
botao.pack(pady=10)

root.mainloop()
