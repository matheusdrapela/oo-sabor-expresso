from modelos.restaurantes import Restaurante

restaurante_praza = Restaurante("plaza", "gourmet")
restaurante_praza.receber_avaliacao("Rubinho", 5)
restaurante_praza.receber_avaliacao("Ana", 4)
restaurante_praza.receber_avaliacao("Bia", 3)


def main():
    Restaurante.lista_restaurante()

if __name__ == "__main__":
    main()