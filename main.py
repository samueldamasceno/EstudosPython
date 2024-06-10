import random

def regras():
    print("""Já conhece as regras?
      \t1.Sim
      \t2.Não""")
    opcao = input("Escolha uma opção: ")
    match opcao:
        case "1":
            print("Ótimo! Então vamos começar.")
            return
        case "2":
            print("""\tFunciona assim:
                  Em cada rodada, vou pedir para você escolher entre três opções: pedra, papel ou tesoura.
                  Então, o computador irá escolher aleatoriamente entre as mesmas opções.
                  Dependendo das respostas, um de vocês ganha! Fácil, né?
                  
                  Pedra ganha de tesoura e perde de papel.
                  Papel ganha de pedra e perde de tesoura.
                  Tesoura ganha de papel e perde de pedra.
                  
                  Vamos lá?""")
            input("Digite ENTER para continuar.")
            return

def pedra_papel_tesoura():
    print("Pedra, papel ou tesoura?")
    print("\t1. Pedra \n\t2. Papel \n\t3. Tesoura")
    print()
    jogada_usurio = input("Escolha sua opção: ")
    print()

    jogada_computador = random.choice(["pedra", "papel", "tesoura"])
    match jogada_usurio:
        case "1":
            print("Você: Pedra")
            print("Computador: ", jogada_computador)
            print()
            if jogada_computador == "pedra":
                print("Empate")
            elif jogada_computador == "papel":
                print("Você perdeu")
            elif jogada_computador == "tesoura":
                print("Você ganhou")
        case "2":
            print("Você escolheu Papel")
            print("Computador escolheu", jogada_computador)
            print()
            if jogada_computador == "pedra":
                print("Você ganhou")
            elif jogada_computador == "papel":
                print("Empate")
            elif jogada_computador == "tesoura":
                print("Você perdeu")
        case "3":
            print("Você escolheu Tesoura")
            print("Computador escolheu", jogada_computador)
            print()
            if jogada_computador == "pedra":
                print("Você perdeu")
            elif jogada_computador == "papel":
                print("Você ganhou")
            elif jogada_computador == "tesoura":
                print("Empate")

print("Vamos jogar Pedra, Papel ou Tesoura?")
print()
input("Digite ENTER para continuar.")
print()
regras()
pedra_papel_tesoura()