from random import *
from tkinter import *
#Função que vai gerar o nome
def nome():
    escolha = int(input('''Qual sua classe?\n 
                       [ 1 ] Mago\n 
                       [ 2 ] Ladino\n 
                       [ 3 ] Necromante\n 
                       [ 4 ] Cavaleiro\n 
                       [ 5 ] Arqueiro\n 
                       [ 6 ] Bardo\n 
                       [ 7 ] Feitiçeiro\n
                       [ 8 ] Bruxo\n
                    Escolha: '''))
    classe = [ 'Mago', 'Ladino', 'Necromante', 'Cavaleiro', 'Arqueiro', 'Bardo', 'Feitiçeiro', 'Bruxo']
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caracteres = int(input('Quantos caractéres seu nome terá? '))
    sorteio = choice(letras)
    #Usar for para o número de sorteio de letras atingir o número de caractéres.
    print(sorteio*caracteres)



#Criando tela
tela = Tk()
tela.title('Gerador de nomes RPG')
tela.geometry('800x600')
#Criando Botão
botao = Button(tela, text='Teste', command=nome)
botao.pack()

tela.mainloop()