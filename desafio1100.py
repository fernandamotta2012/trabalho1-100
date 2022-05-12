import random


def gera():
    return random.randint(1, 100)

def game():
    resposta = gera()
    tentativa = 0
    print("_______________")
    print("Seja bem-vindo ao ADIVINHE SE PUDER!")
    print("_______________\n")
    print("O objetivo é acertar um número escolhido pelo o programa com a menor quantidade de tentativas.\n")
    print("\nQual será seu Palpite?")

    chute = 0
    while chute is not resposta:
        tentativa += 1
        chute = int(input("\nDigite um número entre 1 e 100: "))

        if chute > resposta:
            print(" Que pena, você errou! É um valor menor que ", chute)
        elif chute < resposta:
            print("Errou feio em?! É um valor maior que", chute)
        else:
            print("\nParabéns! O número gerado foi ", resposta, \
                  "Acertou em ", tentativa, " tentativas!")

            print("\nObrigada(o) por jogar!")


while True:
    game()