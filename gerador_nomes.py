from random import randint

print('\033[31m-=\033[m'*75)
print('Esse é um programa de geração de nomes de personagens de RPG')
opção = input('Quer começar?[S/N]\nEscolha: ').strip().upper()
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if opção == 'S':
    classe = int(input('''Qual sua classe?\n 
                       [ 1 ] Mago\n 
                       [ 2 ] Ladino\n 
                       [ 3 ] Necromante\n 
                       [ 4 ] Cavaleiro\n 
                       [ 5 ] Arqueiro\n 
                       [ 6 ] Bardo\n 
                       [ 7 ] Feitiçeiro\n
                       [ 8 ] Bruxo\n
                    Escolha: '''))
    clas = [ 'Mago', 'Ladino', 'Necromante', 'Cavaleiro', 'Arqueiro', 'Bardo', 'Feitiçeiro', 'Bruxo']
    letras_nome = []
    quantidade_letras = int(input('Quantos caractéres você vai querer em seu nome? '))
    for x in range(1, quantidade_letras+1):
        nome = randint(0, quantidade_letras)
        nome_sorteado = letras[nome]
        letras_nome.append(nome_sorteado)
    classe_completa = clas[classe-1]
    nome_completo = ''.join(letras_nome)
    print('Seu nome é:')
    print('{}, {}'.format(classe_completa, nome_completo.title()))
elif opção == 'N':
    print('FIM DO PROGRAMA')
else:
    while opção != 'S':
        print('\033[31m[ERROR]\033[m')
        opção = input('Quer começar o programa?[S/N]\nEscolha: ').strip().upper()
print('\033[31m-=\033[m'*75)