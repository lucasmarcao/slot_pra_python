#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
# para um n informado pelo usuário.
#  Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
import random
import ctypes, sys

def printColorizedInWindows(text, color):
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    for i in range(0, len(color)):
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
        sys.stdout.write(text)
    # cor padrão é 7, white
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
    
if __name__ == "__main__":
    text = u"digite a palavra que vc quer: -->"
    color = [2] # número da cor do texto
    infinito = 0
    while (infinito==0):
      try:
        textao = printColorizedInWindows(text,color)
        textao
        entrevista =  int(input(""))
        infinito = 1
      except Exception as e:
        print("É PRA ESCREVER UM NUMERO INTEIRO SEU IDIOTA!!!. \n")
    total = []
    letra = []
    
    for value in range(15):
      total.append([value])
    for value in range(entrevista):
      letra.append(value+1)
    for value in range(entrevista):
      tudo = letra[value]
      vetor = random.choice(total[random.randint(1,14)])
      novalista = []
      novalista.append(vetor)
      printColorizedInWindows((str(tudo)+" + "),novalista)
      novalista.clear()
    
    entrevista= (entrevista+1)*(entrevista/2)
    resultadofinal = "\n a soma de todos esses numeros é = "+str(entrevista)
    newvetor = random.choice(total[random.randint(1,14)])
    novalistafinal = []
    novalistafinal.append(newvetor)
    printColorizedInWindows(resultadofinal, novalistafinal)



    
    
