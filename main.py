import random

def pedra_papel_tesoura():
    print("Pedra, papel ou tesoura?")
    print("\t1. Pedra \n\t2. Papel \n\t3. Tesoura")
    print()
    jogada_usurio = input("Escolha sua opção: ")
    print()

    computador = random.choice(["pedra", "papel", "tesoura"])
    match jogada_usurio:
        case "1":
            print("Você: Pedra")
            print("Computador: ", computador)
            print()
            if computador == "pedra":
                print("Empate")
            elif computador == "papel":
                print("Você perdeu")
            elif computador == "tesoura":
                print("Você ganhou")
        case "2":
            print("Você escolheu Papel")
            print("Computador escolheu", computador)
            print()
            if computador == "pedra":
                print("Você ganhou")
            elif computador == "papel":
                print("Empate")
            elif computador == "tesoura":
                print("Você perdeu")
        case "3":
            print("Você escolheu Tesoura")
            print("Computador escolheu", computador)
            print()
            if computador == "pedra":
                print("Você perdeu")
            elif computador == "papel":
                print("Você ganhou")
            elif computador == "tesoura":
                print("Empate")

print("Vamos jogar Pedra, Papel ou Tesoura?")
print()
pedra_papel_tesoura()