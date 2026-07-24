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

                 'placa' : carro._placa,
                'modelo': carro._modelo,
                'cor': carro._cor,
                'ano': carro._ano,
                'status': carro._status,
                'data de cadastro' : carro._data_cadastro

             })

         with open('carros.json', 'w', encoding='utf-8') as arquivo:
             json.dump(dados, arquivo, indent=4, ensure_ascii=False)



     @classmethod
     def carregar_json(cls):
         if os.path.exists('carros.json'):
             with open('carros.json', 'r', encoding='utf-8') as arquivo:
                 dados = json.load(arquivo)
                 cls.estoque = []
                 for item in dados:
                     Carro(
                         placa=item.get('placa', 'N/A'),
                         modelo=item['modelo'],
                         cor=item['cor'],
                         ano=item['ano'],
                         status=item.get('status', False),
                         data_cadastro=item.get('data de cadastro')
                     )


     estoque = []

     def __init__(self, placa, modelo, cor, ano, data_cadastro=None):
         self._placa = placa
         self._modelo = modelo
         self._cor = cor
         self._ano = ano
         self._status = False
         self._data_cadastro = data_cadastro or datetime.now().strftime('%d/%m/%Y %H:%m')
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
            print(f"{carro._placa.ljust(20)} | {carro._modelo.ljust(20)} | {carro._cor.ljust(20)} | {str(carro._ano).ljust(20)} | {str(status).ljust(20)}")



     @classmethod
     def adicionar_modelos(cls):

        while True:

            placa = input(str('Qual a placa do carro? (7 caracteres): ')).strip().upper()

            if len(placa) == 7:
                break
            else:
                print("❌ Placa inválida! A placa deve ter exatamente 7 caracteres (Ex: ABC1D23 ou ABC1234).\n")




        modelo = input(str('Qual o modelo?: '))
        cor = input(str('Qual o Cor?: '))
        ano = input(str('Qual o Ano?: '))
        Carro(placa, modelo, cor, ano)
        cls.salvar_json()

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

     @classmethod
     def excluir(cls):
         placa_busca = input('Digite a placa do veículo que você deseja EXCLUIR: ').strip().upper()
         encontrado = False

         for carro in cls.estoque:
                 if carro._placa.strip().upper() == placa_busca:
                     cls.estoque.remove(carro) 
                     cls.salvar_json()         
                     print(f"\n O veículo com a placa {placa_busca} foi excluído com sucesso!")
                     encontrado = True
                     break
                 if not encontrado:
                     input(f"\n O veículo {placa_busca}, não foi encontrado em nosso banco de dados! Pressione enter")





def menu_principal():
    while True:

        


        print("\n=== ESTOQUE DOS VEÍCULOS ===    ")
        print(" 1 - Cadastrar veículo")
        print(" 2 - Listar estoque")
        print(" 3 - Ativar veículo")
        print(" 4 - !!EXCLUIR!!")
        print(" 5 - Sair")

        opcao = input("\nEscolha o opção desejada: ")

        if opcao == '1':
            Carro.limpar_tela()
            Carro.adicionar_modelos()

        elif opcao == '2':
            Carro.limpar_tela()
            Carro.Listar_modelos()
            input("\nPressione ENTER para voltar ao menu...")            

        elif opcao == '3':
            Carro.limpar_tela()
            Carro.ativar_modelo()

        elif opcao == '4':
            Carro.limpar_tela()
            Carro.excluir()


        elif opcao == '5':
            Carro.limpar_tela()
            print("Saindo do programa, até logo!!")
            break


        else:
            Carro.limpar_tela()
            print("Opção invalida! Digite a opção novamente. ")                          

menu_principal()