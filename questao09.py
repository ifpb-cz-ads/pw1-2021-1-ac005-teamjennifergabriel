import random


def acerto():
    n = random.randint(1, 10)
    x = int(input("Escolha um número entre 1 e 10:"))
    if x == n:
        print("Você acertou!")
    else:
        print("Você errou.")


x = 0
chances = 3
while x < chances:
    print(" %d chance" % (x + 1))
    acerto()
    x += 1
