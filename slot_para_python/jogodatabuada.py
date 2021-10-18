import random
cont=0
try:
    testandomatriz = random.sample([1,4,2],counts=[5,5,5], k=7)
    print(testandomatriz)   
except Exception as e:
    print("famoso erro")
print("Você precisa de 10 pontos para ganhar")
while(cont<10):
    prim = random.randint(1,11)

    seg = random.randint(1,11)

    print("a conta é : ",prim," X ",seg," = \n" )

    vezes = prim * seg
    
    resposta = int(input("O resultado desta conta é -------->"))


    
    if(resposta==vezes):
        print("você acertou!!!, o resultado realmente era: ", vezes)
        cont = cont + 1
        print("sua pontuação é:", cont)
        
    else:
        print("Você está errado, a resposta era: ", vezes)
        print("sua pontuação é:", cont)
        
    
    confirm = input("deseja continuar?")
    if(confirm=="sim" or confirm=="SIM" or confirm=="s" or confirm=="S" or confirm=="claro"):
        prim = 0
        seg = 0
        vezes = 0
    else:
        cont = 11
        print("até a proxima")

if(cont==10):
    print("Você ganhou  o jogo")

