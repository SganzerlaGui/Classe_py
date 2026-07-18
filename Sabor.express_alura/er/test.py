class Carro:

    carros = []

    def __init__(self, carros, cor, ano, status):
        self.carros = carros
        self.cor = cor
        self.ano = ano
        self.status = status
        Carro.carros.append(self)
    
    def __str__(self):
        return f'{self.carro} | {self.cor} | {self.ano} | {self.status}'
    
    def Listar_Carros():
        for carro in Carro.carros:
            print(f'{carro.carro} | {carro.cor} | {carro.ano} | {carro.status}')