from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):   # (self) é como se fosse para falar de um "restaurante" de cada vez!! ---- E não necessariamente precisa ser self! Podemos usar no python qualquer palavra!!!
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False  # quando coloco o self._ativo deixa essa propriedade protegida, que ele nem deve ser mexido! no caso, não mostra ela de primeira
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    #é usado para indicar que um método pertence à classe em si, e não a uma instância específica dessa classe. Pense nele como uma ferramenta que diz: "Este método é para a classe Restaurante como um todo, e não para um restaurante_praca ou restaurante_pizza individualmente."
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(20)} | {'Categoria do restaurante'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'.ljust(20)}")
        for restaurante in cls.restaurantes: 
            # VEJA AQUI: Fechamos o str() logo após a propriedade, e o .ljust(20) fica fora dele!
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo.ljust(20)}')

    #@property é para mudar a propriedade de ativo
    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'

    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avalicao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacao(self):
        # Corrigido aqui: checa se a lista de avaliações está vazia
        if not self._avaliacao:
            return 'Esse restaurante ainda não tem avaliação' 
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        resultado = round(media / 2, 1)
        return resultado



#Restaurante.listar_restaurantes()


# print(vars(Restaurante_001)) -- > Usa o vars para definir as variaveis e atributos

# print(dir(Restaurante_001)) -- > Usa o dir para ver tudo que nasce com a palavra