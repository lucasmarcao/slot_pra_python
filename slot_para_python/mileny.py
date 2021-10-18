g = 0
m = 0
f = 0

while (g == 0):
    print ("solicite quantas pessoas voce quer registrar")
    a= 0
    a = int(input("numero de pessoas---->"))
    for i in range (0,a):
        print("digite o sexo da pessoa.")
        z = input("pessoa :--> ")
        
        
        if (z == "m" or z == "M"):
            m = m + 1
        if (z == "f" or z == "F"):
            f = f + 1
    print("numero de homens: ",m)
    print("numero de mulheres: ",f)
    porcentagem_masculina = m/(m+f)*100
    porcentagem_feminina = f/(f+m)*100
    print("porcentagem masculina: ",porcentagem_masculina,"%")
    print("porcentagem feminina: ",porcentagem_feminina,"%")
    print("deseja continuar?")
    m = 0
    f = 0
    c = (input("sim ou não: -->"))
    if (c=="sim" or c=="s"  or c=="afirmativo" or c=="S"):
        g = 0
    if (c== "não" or c =="nao" or c=="n" or c=="N" or c=="negativo" ):
        g = 1
    
