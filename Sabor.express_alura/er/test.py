import json 
import os
from datetime import datetime


class Carro:
     @staticmethod
     def limpar_tela():
        os.system('cls')

     @classmethod
     def salvar_json(cls):
         dados = []
         for carro in cls.estoque:
             dados.append({
                 
                'modelo': carro._modelo,
                'cor': carro._cor,
                'ano': carro._ano,
                'status': carro._status
             })

         with open('carros.json', 'w', encoding='utf-8') as arquivo:
             json.dump(dados, arquivo, indent=4, ensure_ascii=False)

     estoque = []

     def __init__(self, modelo, cor, ano):
         self._modelo = modelo
         self._cor = cor
         self._ano = ano
         self._status = False
         Carro.estoque.append(self)


     def __str__(self):
         return f'{self._modelo} | {self._cor} | {self._ano} | {self._status}'

     @classmethod
     def Listar_modelos(cls):
         print("   === ESTOQUE DOS VEÍCULOS ===    ")
         print(f"{'Modelo do veículo'.ljust(20)} | {' Cor do veículo'.ljust(20)} | {'Ano do veículo'.ljust(20)} | {'Status do veículo'.ljust(20)}")
         for carro in cls.estoque:

            #Como usar esse if/else: [O que eu quero] if [se isso for verdade] else [o que eu quero caso seja falso].
            status = 'Ativado' if carro._status else 'Desativado'
            print(f"{carro._modelo.ljust(20)} | {carro._cor.ljust(20)} | {str(carro._ano).ljust(20)} | {str(status).ljust(20)}")



     @classmethod
     def adicionar_modelos(cls):
         modelo = input(str('Qual o modelo?: '))
         cor = input(str('Qual o Cor?: '))
         ano = input(str('Qual o Ano?: '))
                  
         Carro(modelo, cor, ano)
         cls.salvar_em_json()

     @classmethod
     def ativar_modelo(cls):
         modelo_busca = input('Qual o modelo do carro que você quer ativar?: ')
         encontrado = False

         for carro in cls.estoque:
             if carro._modelo.lower() == modelo_busca.lower():
                 carro._status = True
                 print(f"\n O veículo {carro._modelo} foi encontrado com sucesso!")
                 print(f"\n O {carro._modelo} foi ativado com sucesso!")
                 encontrado = True
                 break
             if  not encontrado:
                 print(f"\n O veículo {modelo_busca} não foi encontrado no estoque!")






def menu_principal():
    while True:

        Carro.limpar_tela()


        print("\n=== ESTOQUE DOS VEÍCULOS ===    ")
        print(" 1 - Cadastrar veículo")
        print(" 2 - Listar estoque")
        print(" 3 - Ativar veículo")
        print(" 4 - Sair")

        opcao = input("\nEsccolha o opção desejada: ")

        if opcao == '1':
            Carro.adicionar_modelos()

        elif opcao == '2':
            Carro.Listar_modelos()            

        elif opcao == '3':
            Carro.ativar_modelo()

        elif opcao == '4':
            print("Saindo do programa, até logo!!")
            break

        else:
            print("Opção invalida! Digite a opção novamente. ")                          

menu_principal()