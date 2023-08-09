#variaveis
import random


jogador = ""
computador = ""
opcao = ["Pedra", "Papel", "Tesoura"]
vjogador = 0
vcomputador = 0
empates = 0

while True:
    print("Jogo Jokenpo")
    print("\n")
    print("Opções:")
    print("Pedra")
    print("Papel")
    print("Tesoura")
    print("\n")

    jogador = input("Digite sua opcao: ")
    computador = random.choice(opcao)
    print(jogador, computador)

    if jogador == "Pedra" and computador == "Tesoura":
        print("Jogador Wins")
    elif jogador == "Papel" and computador == "Pedra":
        print("Jogador Wins")
    elif jogador == "Tesoura" and computador == "Papel":
        print("Jogador Wins")
    elif jogador == computador:
        print("EMPATE")
    else:
        print("Computador Wins")
    
    break



