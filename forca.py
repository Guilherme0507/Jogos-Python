import random

def jogar():

    palavra_secreta = escolhe_palavra()

    imprime_abertura()

    ##letras_acertadas = ["_" for letra in palavra_secreta]
    letras_acertadas = define_espacos(palavra_secreta)

    print(letras_acertadas)
    perdeu = False
    ganhou = False
    errou = 0

    while(not perdeu and not ganhou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        if(chute in palavra_secreta):
            chute_certo(palavra_secreta, letras_acertadas, chute)
        else:
            errou += 1
            desenha_forca(errou)

        perdeu = errou == 7
        ganhou ="_" not in letras_acertadas
        print(letras_acertadas)


    cst_resultado(ganhou, perdeu, palavra_secreta)




def imprime_abertura():
    print("***************************")
    print("Bem vindo ao jogo da forca!")
    print("***************************\n")


def escolhe_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def define_espacos(palavra):
    letras_acertadas = ["_"]
    qnt_palavra = len(palavra)
    for i in range(1, qnt_palavra):
        letras_acertadas.append("_")
    return letras_acertadas


def chute_certo(palavra,letras,chute):
    posicao = 0
    for letra in palavra:
        if (chute.upper() == letra.upper()):
            letras[posicao] = letra
            ##print("A letra %s foi encontrada na posição %d" %(letra.upper(), posicao))
        posicao = posicao + 1








def cst_resultado(ganhou, perdeu, palavra):
    if(ganhou):
            print("Parabéns, você ganhou!")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()

