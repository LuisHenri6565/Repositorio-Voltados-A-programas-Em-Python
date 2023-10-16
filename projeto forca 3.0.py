#!/usr/bin/env python
# coding: utf-8

# In[57]:


# importções

import random
from os import system, name

# Função para limpar a tela a cada execução

def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# tabuleiro
tabuleiro= ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
                  # Metodos:
        
    # O construtor
    def __init__(self,palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []
        
    # Para advinhar a letra
    def sera(self, letra):
        if len (letra) < 1:
            print('\nVocê precisa digitar UMA letra.')
            return False
        elif len(letra) > 1:
            print('\nPor favor, insira apenas uma letra por vez.')
            return False
        elif not letra.isalpha():
            print ('\nPor favor, insira apenas letras.')
        
        # Se a letra escolhida estiver na palavra secreta, e não estiver na lista...
        #... de palavras escolhidas, adicionar a letra em letras escolhidas
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
            
        # Se a letra escolhida não estiver na palvra secreta e não estiver na lista...
        # de palavras erradas, adicionar a letra em letras erradas
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
            
        else:
            return False
        return True
    
    # Ver se o jogador perdeu
    def jogador_perdeu (self):
        return self.jogador_ganhou() or (len(self.letras_erradas) == 6)
    
    # Ver se o jogador ganhou
    def jogador_ganhou (self):
        
        if '_' not in self.palavra_escolhida():
            return True
        return False
        
    # Mostra a palavra oculta 
    def palavra_escolhida(self):
        
        vaco = ''
        
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                vaco += ' _'
            else:
                vaco += letra
        return vaco
        
    # Ver o estado o game e mostrar na tela as informações
    def imprimir_estatus_do_jogo(self):
            
        print (tabuleiro[len(self.letras_erradas)])
            
        print ('\nPalavra: ' + self.palavra_escolhida())
            
        print ('\nletras erradas: ', end= '')
            
        for letra in self.letras_erradas:
            print (letra, end=' ')
                
        print ()
            
        print ('letras corretas: ', end=' ')
            
        for letra in self.letras_escolhidas:
            print (letra, end=' ')
                
        print ()
                
# Ler a palavra de forma aleartória de banco de palavras
def escolha_da_palavra():
    
    # Daonde vem as plavras usados no jogo
    with open("C:/Users/luiso/Videos/personagem.txt", "r") as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    
    # A randomicidade da escolha da palavra misteriosa
    palavra = random.choice(palavras)
    return palavra

# Principal, A execução 
def main():
    
    limpa_tela()
    
    game = Hangman(escolha_da_palavra())
    
    while not game.jogador_ganhou() and len(game.letras_erradas) < 6:
        
        #status do jogo 
        game.imprimir_estatus_do_jogo()
        
        # Envia a solicitação para usuario inserir uma letra
        letra_digitada = input('\nDigite uma letra: ')
        
        # Confere se a letra esta presente na palavra secreta
        game.sera(letra_digitada)
        
    # Confere o estado do jogo
    game.imprimir_estatus_do_jogo()
    
    if game.jogador_ganhou():
        print ('\nVocê venceu!!')
        
    else:
        print ('\nVocê perdeu.')
        print ('A palavra era', ''.join (game.palavra))

# O que executa o programa
if __name__ == '__main__':
    main()


# In[ ]:




