
# Projeto calculadora 09/09/2023!
import os  # Importa um modulo que disponibiliza funções a interagir com o sistema operacional
import math   # Importa o pacote matemático.
import statistics   # Importa o pacote estatístico.
from collections import Counter  # Importa a função Counter do pacote collections.
                       
# Definições de operções básicas:
def soma(x,y):
    return x + y

def subtraçao(x,y):
    return x - y

def multiplicaçao(x,y):
    return x * y

def divisao(x,y):
    return x / y

# Definições de operações avançadas:
def porcentagem(x):
    return (x / 100 ) 

def raiz_quadrada(x):
    return math.sqrt (x)

def potencia(x,y):
    return x ** y

# Definições de funções trigonométricas:
def seno(x) :
    angulo_radiano = math.radians(x)
    seno = math.sin(angulo_radiano)
    return seno

def cosseno(x):
    angulo_radiano = math.radians(x)
    cosseno = math.cos(angulo_radiano)
    return cosseno

def tangente(x):
    angulo_radiano = math.radians(x)
    tangente = math.tan(angulo_radiano)
    return tangente

# Definições de funções estatísticas:
def media(numeros_selecionados):
    return sum (numeros_selecionados) / len (numeros_selecionados)
    
def moda(numeros_selecionados): 
    contagem = Counter(numeros_selecionados)
    moda = contagem.most_common (1)[0][0]
    return moda

def mediana(numeros_selecionados):
    dados_ordenados = sorted(numeros_selecionados)
    tamanho = len(numeros_selecionados)
    if tamanho % 2 == 0:
        meio = tamanho // 2
        mediana = (dados_ordenados[meio - 1] + dados_ordenados [meio]) / 2
    else:
        mediana = dados_ordenados[tamanho // 2]
    return mediana 
    
def desvio_padrão(numeros_digitados):
    return statistics.stdev(numeros_digitados)

# Definição que limpa a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()
# Titulo inicial do sistema!
print("\n******************* Calculadora em Python *****************") 

# O que sera impresso na tela de apresentação!
print("\nSelecione o NÚMERO da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")
print("6 - Porcentagem")
print("7 - Raiz quadrada")
print("8 - Seno")
print("9 - Cosseno")
print("10 - Tangente")
print("11 - Média")
print("12 - Moda")
print("13 - Mediana")
print("14 - Desvio padrão")

# Função que filtra opção escolhida pelo usuario já aplicadado os devidos cuidados com bugs e erros!  
def obter_escolha():
    while True:
        try:
            escolha = input("\nDigite o numero corespondente da operação desejada: ")
            if not escolha.isdigit():
                raise ValueError("\nDigite apenas número para realizar a operação desejada!")
            escolha = int(escolha)
            if escolha < 1 or escolha > 14:
                raise ValueError("\nOperação inválida.\n\nDigite o número da operação apresentada no quadro inicial.")
            return escolha
        except ValueError as ve:
            print(ve)
        except:
            print("\nAlgo deu errado. Tente novamente!")
            
# Essa função serve para iniciar as operções básicas e avançadas, pois nelas serão normalmnete utilizados 2 números.
def numeros():
    limpar_tela()
    while True:
        try:
            num1 = input("\nDigite o primeiro número: ")
            num1 = int(num1)
            num2 = input("\nDigite o segundo número: ")
            num2 = int(num2)
            return num1, num2
        except ValueError:
            print("\nDigite apenas números e um por vez para realizar a operação desejada: ")
            continue   
# Essa função serve para iniciar as operções trigonométricas, pois nelas serão normalmnete utilizado apenas 1 número.
def numero ():
    limpar_tela()
    while  True:
        try:
            num1 = input("\nDigite o primeiro número: ")
            num1 = int(num1)
            return num1
        except ValueError:
            print("\nDigite apenas um NÚMERO para realizar a operação desejada: ")
            continue
                
# Essa função serve para iniciar as operções estatisticas, pois nelas serão normalmnete utilizados mais de 2 números.
def numeros_digitados():
    limpar_tela()
    # Solicita os números ao usuário e cria a lista!
    numeros_digitados = []
    while True:
        try:
            num = float(input("\nDigite um número (ou 0 para encerrar a entrada): "))
            if num == 0:
                break
            numeros_digitados.append(num)
        except ValueError:
            print("\nDigite apenas números e um de cada vez para realizar a operação desejada.")
    
    return numeros_digitados
        
# Em seguida, o desenvolvimento das escolhas, tendo as divisões das operções e filtros na operação de divisão, raiz quadrada...
#...e nas demais necessárias para evitar bugs!
    
escolha = obter_escolha()

if escolha < 6:
    num1, num2 = numeros()
    if escolha == 1:     # Soma;
        print("\nRealizando a operação de soma...\n")
        print(num1, "+", num2, "=", soma(num1, num2))

    elif escolha == 2:   # Subtração;
        print("\nRealizando a operação de subtração...\n")
        print(num1, "-", num2, "=", subtraçao(num1, num2))

    elif escolha == 3:   # Multiplicação;
        print("\nRealizando a operação de multiplicação...\n")
        print(num1, "*", num2, "=", multiplicaçao(num1, num2))

    elif escolha == 4:   # Divisão;
        print("\nRealizando a operação da divisão...\n")
        while True:
            try:
                if num2 == 0:
                    raise ValueError("\nNão é possível dividir por zero. Digite um valor diferente de zero para o segundo número que sera o divisor.")
                else:
                    print("\n")
                    print(num1, "/", num2, "=", divisao(num1, num2))
                    break
            except ValueError as ve:
                print(ve)
                num2 = int(input("\nDigite um novo valor para o segundo número: "))

    elif escolha == 5:   # Potencia;
        print("\nRealizando a operação de potencia...\n")
        print(num1, "^", num2, "=", potencia(num1, num2))
    

else:
    if escolha == 6:    # Porcentagem;
        print("\nRealizando a operação de porcentagem...\n")
        while True:
            try:
                num1 = int(input("\nDigite o número para calcular a porcentagem: "))
                if num1 < 0 :
                    raise ValueError("\nO número não pode ser negativo para calcular a porcentagem.")
                print("\n")
                print(num1, "%", "=", porcentagem(num1))
                break
            except ValueError as ve:
                print("\nDigite apenas um número para realizar a operação desejada.")
                
    elif escolha == 7:       # Raiz quadrada;
        print("\nRealizando a operação da raiz quadrada...\n")
        while True:
            try:
                num1 = int(input("\nDigite o número para calcular a raiz quadrada: "))
                if num1 < 0:
                    raise ValueError("\nNão existe raiz de número negativo.\n\nDigite um valor positivo para realizar a operação.")
                else:
                    print("\nRaiz quadrada de", num1, "=", raiz_quadrada(num1))
                    break
            except ValueError as ve:
                print("\nDigite apenas um unico número para realizar a operação desejada.")
                
    elif escolha > 7:
        if escolha < 11:
            num1 = numero()
            angulo = num1
            if escolha == 8:     # Seno;
                print("\nRealizando a operação do seno...\n")
                print("\nSeno de", angulo, "graus =", seno(angulo))

            elif escolha == 9:    # Cosseno;
                print("\nRealizando a operação do cosseno...\n")
                print("\nCosseno de", angulo, "graus =", cosseno(angulo))

            elif escolha == 10:   # Tangente;
                print("\nRealizando a operação da tangente...\n")
                print("\nTangente de", angulo, "graus =", tangente(angulo))
            
        elif escolha >= 11:
            valores = numeros_digitados()
            if escolha == 11:  # Média;
                if valores:
                    print("\nRealizando a operação da média...\n")
                    print("\nMédia dos números digitados:", media(valores))
                else:
                    print("\nNão há números para calcular a media, a lista está vazia.")
                    
            elif escolha == 12:  # Moda;
                if valores:
                    print("\nRealizando a operação da moda...\n")
                    print("\nModa dos números digitados:", moda(valores))
                else:
                    print("\nNão há números para calcular a moda, a lista está vazia.")
                    
            elif escolha == 13:  # Mediana;
                if valores:
                    print("\nRealizando a operação da mediana...\n")
                    print("\nMediana dos números digitados:", mediana(valores))
                else:
                    print("\nNão há números para calcular a mediana, a lista está vazia.")
                    

            elif escolha == 14:  # Desvio padrão.
                if valores:
                    print("\nRealizando a operação do desvio padrão...\n")
                    print("\nDesvio padrão dos números digitados:", desvio_padrão(valores))
                else:
                    print("\nNão há números para calcular a desvio padrão, a lista está vazia.")
                    
print ("\nPrograma encerrado!\n")