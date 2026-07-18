from modelos.restaurante import Restaurante

Restaurante_Gui = Restaurante('Guigas','gourmet')
Restaurante_Gui.receber_avalicao('Gui', 10)
Restaurante_Gui.receber_avalicao('Lu', 7)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()