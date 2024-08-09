from random import *
from tkinter import *
#Função que vai gerar o nome
def nome():
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
    opção = Entry(tela).pack()
    classe = [ 'Mago', 'Ladino', 'Necromante', 'Cavaleiro', 'Arqueiro', 'Bardo', 'Feitiçeiro', 'Bruxo']
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caracteres = (input('Quantos caractéres seu nome terá? '))
    for s in range(0, caracteres):
        sorteio = choice(letras)
        print('{} o {}'.format(sorteio.capitalize(), classe[0]), end='')
    
#Fazer com que o print da classe fique na mesma linha que a do nome e por fim colocar o programa na janela e personalizala. =)


#Criando tela
tela = Tk()
tela.title('Gerador de nomes RPG')
tela.geometry('800x600')
#Criando Botão
botao = Button(tela, text='Teste', command=nome)
botao.pack()

tela.mainloop()