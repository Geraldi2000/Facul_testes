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
        vjogador +=1
        print("Jogador Wins")
    elif jogador == "Papel" and computador == "Pedra":
        vjogador +=1
        print("Jogador Wins")
    elif jogador == "Tesoura" and computador == "Papel":
        vjogador +=1
        print("Jogador Wins")
    elif jogador == computador:
        empates +=1
        print("EMPATE")
    else:
        vcomputador +=1
        print("Computador Wins")
    
    print("Placar: ")
    print(f"Jogador: {vjogador} ")
    print(f"Computador: {vcomputador}")
    print(f"Empates: {empates} ")
    respostas = input("Deseja continuar s/n? ")
    if respostas=="n":
        break
    
    
    
    




