import random

def regras():
    print("""Já conhece as regras?
      \t1.Sim
      \t2.Não""")
    while True:
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("Ótimo! Então vamos começar.")
            return
        elif opcao == "2":
            print("""\tFunciona assim:
                  Em cada rodada, vou pedir para você escolher entre três opções: pedra, papel ou tesoura.
                  Então, o computador irá escolher aleatoriamente entre as mesmas opções.
                  Dependendo das respostas, um de vocês ganha! Fácil, né?
                  
                  Pedra ganha de tesoura e perde de papel.
                  Papel ganha de pedra e perde de tesoura.
                  Tesoura ganha de papel e perde de pedra.
                  
                  Vamos lá?""")
            digite_enter()
            return
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

def pedra_papel_tesoura(numero_rodadas):
    for i in range(1, numero_rodadas + 1):
        print(f"====== Rodada {i} ======")
        print("Pedra, papel ou tesoura?")
        print("\t1. Pedra \n\t2. Papel \n\t3. Tesoura")
        print()
        while True:
            jogada_usuario = input("Escolha sua opção: ")
            if jogada_usuario in ["1", "2", "3"]:
                break
            else:
                print("Opção inválida.")

        jogada_computador = random.choice(["Pedra", "Papel", "Tesoura"])

        match jogada_usuario:
            case "1":
                jogada_usuario = "Pedra"
                print("Você: Pedra")

            case "2":
                jogada_usuario = "Papel"
                print("Você: Papel")

            case "3":
                jogada_usuario = "Tesoura"
                print("Você: Tesoura")

        calcular_resultado(jogada_usuario, jogada_computador)

def calcular_resultado(jogada_usuario, jogada_computador):
    if jogada_usuario == jogada_computador:
        print("Empate!")
    elif jogada_usuario == "Pedra":
        if jogada_computador == "Tesoura":
            print("Você ganhou!")
        else:
            print("Você perdeu!")
    elif jogada_usuario == "Papel":
        if jogada_computador == "Pedra":
            print("Você ganhou!")
        else:
            print("Você perdeu!")
    elif jogada_usuario == "Tesoura":
        if jogada_computador == "Papel":
            print("Você ganhou!")
        else:
            print("Você perdeu!")

def quantidade_rodadas():
    print("Quantas rodadas você quer jogar?")
    print("1. 1 rodada")
    print("2. 5 rodadas")
    print("3. 10 rodadas")
    print("4. 15 rodadas")

    while True:
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            return int(opcao)
        elif opcao in ["2", "3", "4"]:
            return (int(opcao) - 1) * 5
        else:
            print("Opção inválida.")

def digite_enter():
    input("Digite ENTER para continuar.")
    print()

print("Vamos jogar Pedra, Papel ou Tesoura?")
print()
digite_enter()
print()
regras()

while True:
    numero_rodadas = quantidade_rodadas()
    print()
    pedra_papel_tesoura(numero_rodadas)
    print()
    print("Deseja jogar novamente?")
    print("\t1. Sim \n\t2. Não")
    opcao = input("Escolha uma opção: ")
    print()
    match opcao:
        case "1":
            continue
        case "2":
            print("Obrigado por jogar!")
            break
