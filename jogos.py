import forca
import adivinhacao

def escolhe_jogo():
    print("***************************")
    print("*****Escola seu jogo!******")
    print("***************************\n")



    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando forca\n")
        forca.jogar()

    elif(jogo == 2):
        print("Jogando adivinhação\n")
        adivinhacao.jogar()

if(__name__ == "__main__"):