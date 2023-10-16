#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from os import system, name

def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

def display_hangman(tentativas):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 4
                """ 
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """ 
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
    ]
    return stages[tentativas]

def game():

    limpa_tela()
    print("\nBem vindo ao jogo da forca!\n")
    print("Adivinhe a palavra abaixo:\n")
    
    palavras = ["gato", "cachorro", "grilo", "giraffa", "papagaio", "cobra"]
    palavra = random.choice(palavras)
    charrada = [letra for letra in palavra]
    tabuleiro = ["_"] * len(charrada)
    
    corretas = []
    erradas = []

    tentativas =6

    while tentativas > 0 and "_" in tabuleiro:
        
        print(display_hangman(tentativas))
        print("Palavra: ", tabuleiro)
        print("\n")
        
        letra = input("Digite uma letra: ").lower()

        if letra in corretas or letra in erradas:
            print("Você já tentou essa letra. Escolha outra!")
        elif letra in charrada:
            print("Você acertou a letra!")
            corretas.append(letra)

            for i, l in enumerate(charrada):
                if l == letra:
                    tabuleiro[i] = letra
        else:
            print("Você errou a letra!")
            erradas.append(letra)
            tentativas += 1

    if "_" not in tabuleiro:
        print("Parabéns, você ganhou!")
    else:
        print("Game over! A palavra era", palavra)

game()

