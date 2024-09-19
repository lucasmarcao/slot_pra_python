class Carro:
    def __init__(
            self,
            marca,
            modelo,
            ano,
            cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def imprimirInformacoes(self):
        print(f"marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"marca: {self.ano}")
        print(f"cor: {self.cor}")
        print(f"velocidade: {self.velocidade} km/h")
