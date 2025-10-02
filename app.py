class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} e {self.categoria}'
    
    def lista_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} e {restaurante.categoria} e {restaurante.ativo}")
    

restaurante_praza = Restaurante("plaza", "gourmet")
restaurante_pizza = Restaurante("pizzaria", "italiana")

Restaurante.lista_restaurante()

