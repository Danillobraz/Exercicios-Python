"""
COLOCAR TODOS OS EXERCICIOS AQUI PARA QUANDO TERMINAR O CURSO
SUBIR PARA O GITHUB 

"""


"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
# nome = input('Digite o seu nome: ')
# idade = input('Digite sua idade: ')

# if nome and idade:
#     print(f'Seu nome é {nome}')
#     print(f'Seu nome invertido é {nome[::-1]}')

#     if ' ' in nome:
#         print('Seu nome contém espaços')
#     else:
#         print('Seu nome NÃO contém espaços')

#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A última letra do seu nome é {nome[-1]}')
# else:
#     print("Desculpe, você deixou campos vazios.")
''''''


# tentativas= 0
# pergunta= int(input("Digite o número secreto entre 0 a 10 R:"))

# # Bloco do Código 
# numero_secreto = 7
# while pergunta != numero_secreto:
#     pergunta= int(input(("Você errou o número, tente de novo R:")))
#     tentativas += 1 
# # Bloco do Código 

# print('Parabéns ! Você acertou o número')
# print(f'Você teve {tentativas} tentativas')
''''''

'''
Crie um código onde o usuário precisa adicionar a senha correta !
'''
# pergunta= int(input('Qual a senha armazenada ?\n' \
# 'R:'))
# senha_armazenada= 4810
# tentativa= 0

# while pergunta != senha_armazenada:
#     pergunta= int(input("Senha incorreta, tente de novo\n" \
#     "R:"))
#     tentativa += 1
#     if tentativa == 5:
#         print(f'Você bateu o limite de tentativas !')
#         break
# else:
#     print('Senha correta')
''''''

'''
Aula - 54 Exercício - Crie uma lista de compras com listas
'''
# import os

# pergunta01= input('Você deseja ficar no acessar sua lista ?\n [Sim] ou [Não] R:').strip().capitalize()

# lista = []

# ver_lista = 'Ver'
# adicionar= 'Adicionar'
# excluir= 'Excluir'
# sair= 'Sair'

# while True:

#     while pergunta01 not in ['Sim', 'Não']:
#         print("Digite apenas 'Sim' ou 'Não'.")
#         pergunta01 = input("Deseja usar a lista de compras? (Sim/Não): ").strip().capitalize()

#     if pergunta01 == 'Não':
#         print('saindo do sistema')
#         break
        
#     elif pergunta01 == 'Sim':
#         pergunta02= input('Oque você gostaria de fazer com sua lista de compras ?\n[Ver] Ver sua lista, [Adicionar] Adicionar itens ou [Excluir] Excluir itens.\nSe desejar sair digite o comando [Sair]\n R:')

        
#         if pergunta02 == ver_lista:
#             if len(lista) != 0:
#                 for i,item in enumerate(lista, start=1):
#                     print(i,item)
#             else:
#                 os.system('cls')
#                 print('Você não tem itens na lista')
#         elif pergunta02 == adicionar:
#             item_adicionado= input('Qual item deseja adicionar ?\n Digite: ')
#             lista.append(item_adicionado)
#             os.system('cls')
#         elif pergunta02 == excluir:
#             item_excluido= input('Qual o número do item que deseja excluir ?\nR:')
#             lista.pop(int(item_excluido) - 1)
#             os.system('cls')
#         elif pergunta02 == sair:
#                 os.system('cls')
#                 print('Saindo da lista')
#                 break
#         elif pergunta02 not in[ver_lista, excluir, adicionar, sair]:
#             print('\nEscolha apenas as funções sugeridas!\n')
''''''

'''
Criando um gerador de cpf 
'''


# from random import randint

# # Gera os 9 primeiros dígitos do CPF (aleatoriamente)
# nove_digitos = ''.join([str(randint(0, 9)) for _ in range(9)])

# # --- Cálculo do 1º dígito verificador ---
# soma = 0
# for i, digito in enumerate(nove_digitos):
#     soma += int(digito) * (10 - i)

# digito_1 = (soma * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# # --- Cálculo do 2º dígito verificador ---
# dez_digitos = nove_digitos + str(digito_1)
# soma = 0
# for i, digito in enumerate(dez_digitos):
#     soma += int(digito) * (11 - i)

# digito_2 = (soma * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# CPF final gerado
# cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

# print(f'CPF gerado: {cpf_gerado}')
''''''

'''
Escreva um programa que retorne o valor hora de um funcionário
com base no seu salário mensal e horas trabalhadas por mês.
(Código abaixo)
'''
# horas_trabalhadas= float(input('Você tem quantas horas de trabalho ?\n R:'))
# salario_mensal= float(input('Quanto é a sua remuneração de trabalho ?\n R:'))


# def valor_hora(horas_trabalhadas,salario_mensal):
#     divisao= float(salario_mensal / horas_trabalhadas)
#     return divisao

# ganha_por_hora= valor_hora(horas_trabalhadas, salario_mensal)
# print(f'Você ganha R$ {ganha_por_hora:.2f} por horas trabalhadas')
''''''

'''
Jogo: Faça um código onde o usuário digite um número e esse número precisa ser igual ao número aleatóriamente. 
'''
# import os
# import random
# print('Vamos brincar de "Advinhe o Número da vez"')
# usuario= int(input('Advinhe o número\nR:'))

# while True:
#     num_aleatorio= random.randint(0,10)
#     os.system('cls')
#     print(f'{num_aleatorio} | {usuario}')
#     if num_aleatorio != usuario:
#         usuario= int(input('Você errou, digite novamente\nR:'))
#         # num_aleatorio= random.randint(0,10)
#         # print(f'{num_aleatorio} | {usuario}')
#     else:
#         print('Parabéns, você acertou')
#         print('O Jogo se encerra aqui !')
#         break
''''''

# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# def multiplicacao(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total

# resultado= multiplicacao(10, 2)
# print(resultado)
''''''

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# perg= int(input('Diga um número:'))

# def par_impar(numero):
#     conta= numero % 2 == 0
#     if conta:
#         return f'{numero} é par'
#     return f'{numero} é impar'

# mostrar= par_impar(perg)
# print(mostrar)
''''''
# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))