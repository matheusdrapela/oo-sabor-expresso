class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} e {self.categoria}'
    
    @classmethod
    def lista_restaurante(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
        
    def alterar_status(self):
        self._ativo = not self._ativo
    

restaurante_praza = Restaurante("plaza", "gourmet")
restaurante_praza.alterar_status()
restaurante_pizza = Restaurante("pizzaria", "italiana")

Restaurante.lista_restaurante()

