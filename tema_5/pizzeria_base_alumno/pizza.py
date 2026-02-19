class Pizza:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__ingredientes = []

    def get_nombre(self):
        return self.__nombre

    def add_ingrediente(self, ingrediente):
        self.__ingredientes.append(ingrediente)
            

    def imprimir_ascii(self):
        aux_ingredientes = []

        for ingredientes in self.__ingredientes:
            if ingredientes.get_simbolo() not in aux_ingredientes:
                aux_ingredientes.append(ingredientes.get_simbolo())

        lista_ingredientes = []
        if(len(aux_ingredientes) == 1):
            lista_ingredientes = [aux_ingredientes[0], aux_ingredientes[0], aux_ingredientes[0]]
        if(len(aux_ingredientes) == 2):
            lista_ingredientes = [aux_ingredientes[1], aux_ingredientes[1], aux_ingredientes[0]]
        if (len(aux_ingredientes) == 3):
            lista_ingredientes = [aux_ingredientes[2], aux_ingredientes[2], aux_ingredientes[0]]

            pipsa = f"""
                  🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞
                🍞🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍞
               🍞🍅{lista_ingredientes[0]}🍅🍅{self.__ingredientes[0].get_simbolo()}🍅🍅🍅{self.__ingredientes[1].get_simbolo()}🍅🍅{self.__ingredientes[2].get_simbolo()}🍅🍞
              🍞🍅                        🍅🍞
             🍞🍅                          🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
            🍞🍅                           🍅🍞
             🍞🍅                         🍅🍞
              🍞🍅                       🍅🍞
               🍞🍅                     🍅🍞
                 🍞🍅🍅🍅🍅🍅🍅🍅🍅🍅🍞
                    🍞🍞🍞🍞🍞🍞🍞🍞🍞
        """
            print(pipsa)
            return pipsa
