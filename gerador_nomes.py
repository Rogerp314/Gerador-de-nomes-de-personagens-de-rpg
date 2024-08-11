from random import *
from tkinter import *
#Função que vai gerar o nome
def nome(event):
    escolha = Label(tela, text='''Qual sua classe?\n 
                       [ 1 ] Mago\n 
                       [ 2 ] Ladino\n 
                       [ 3 ] Necromante\n 
                       [ 4 ] Cavaleiro\n 
                       [ 5 ] Arqueiro\n 
                       [ 6 ] Bardo\n 
                       [ 7 ] Feitiçeiro\n
                       [ 8 ] Bruxo\n
                    Escolha: ''')
    escolha.pack()
    opção = Entry(tela)
    opção.pack()
    botao = Button(tela, text='Clique aqui para confirmar o classe', command = sorvete)
    botao.pack()
    valor_classe = opção.get()
    valor_real_classe = int(valor_classe)
    def sorvete():
        classe = [ 'Mago', 'Ladino', 'Necromante', 'Cavaleiro', 'Arqueiro', 'Bardo', 'Feitiçeiro', 'Bruxo']
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        caracteres_pergunta = Label(tela, text='Quantos caractéres seu nome terá? ')
        caracteres_pergunta.pack()
        caracteres = Entry(tela)
        caracteres.pack()
        valor_caracteres = caracteres.get()
        valor_real_caracteres = int(valor_caracteres)
        for s in range(0, valor_real_caracteres):
            sorteio = choice(letras)
            Label(tela, text='{} o {}'.format(sorteio.capitalize(), classe[valor_real_classe]), end='')
    
#Fazer com que o print da classe fique na mesma linha que a do nome e por fim colocar o programa na janela e personalizala. =)


#Criando tela
tela = Tk()
tela.title('Gerador de nomes RPG')
tela.geometry('800x600')
#Fazendo com que ao clicado a tecla Enter começe o algoritmo
verificador = False

start = Label(tela, text='Clique Enter para começar!')
start.pack()
tela.bind('<Return>', nome)
verificador = True
def iniciar_codigo(event):
    global verificador
    if not verificador:
        print("Código iniciado!")
        verificador = True
    else:
        print("Ação já foi executada.")

tela.mainloop()