contador= 0
while(contador == 0 ):
    print ("esse projeto calcula a quantidade de moedas para que vc precisa receber para seu troco")
    troco = int(input("seu troco : "))
    substituto = troco

    moedade50 = troco//50
    sobras = troco%50

    moedade25 = sobras//25
    sobras2 = sobras%25

    moedade10 = sobras2//10
    sobras3 = sobras2%10

    moedade5 = sobras3//5
    sobras4 = sobras3%5

    moedade1 = sobras4//1

    total = moedade50 + moedade25 + moedade10 +moedade5 + moedade1
    if(substituto//50!=0):
        substituto = substituto - moedade50*50
    print(troco, " centavos menos  ", moedade50 ," moedas de 50 centavos é = ",substituto, "centavos.")
    if(sobras//25!=0):
        substituto = substituto - moedade25*25
    print(sobras, " centavos menos ", moedade25 ," moedas de 25 centavos é = ",substituto, "centavos.")
    if(sobras2//10!=0):
        substituto = substituto - moedade10*10
    print(sobras2, " centavos menos ", moedade10 ," moedas de 10 centavos é = ",substituto, "centavos.")
    if(sobras3//5!=0):
        substituto = substituto - moedade5*5
    print(sobras3, " centavos menos ", moedade5 ," moedas de 5 centavos é = ",substituto, "centavos.")
    if(sobras4//1==0):
        substituto = substituto - moedade1*1
    print(sobras4, " centavos menos ", moedade1 ," moedas de 1 centavos é = ",substituto, "centavos.")
        
    print("")
    print("total de moedas necessárias",total )
    print("")
    print("moedas de 50 centavos necessárias", moedade50)
    print("moedas de 25 centavos necessárias", moedade25)        
    print("moedas de 10 centavos necessárias", moedade10)
    print("moedas de 5 centavos necessárias", moedade5)
    print("moedas de 1 centavos necessárias", moedade1)
    print("################################################################################")
    print("")
    confirmação = input("deseja continuar?")
    if (confirmação == "sim" or confirmação == "SIM"  or confirmação == "Sim" or confirmação == "S" or confirmação == "s" or confirmação == "afirmativo" ):
        contador = 0
    if (confirmação == "nao" or confirmação == "não"  or confirmação == "N" or confirmação == "Não" or confirmação == "n" or confirmação == "negativo" ):
        contador = 1
        print("fim do projeto.")

    