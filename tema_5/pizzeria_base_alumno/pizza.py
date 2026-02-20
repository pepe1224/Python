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
            lista_ingredientes = [aux_ingredientes[0], aux_ingredientes[1], aux_ingredientes[1]]
        if (len(aux_ingredientes) == 3):
            lista_ingredientes = [aux_ingredientes[0], aux_ingredientes[1], aux_ingredientes[2]]

        return f"""
                  🍞🍞🍞🍞🍞🍞🍞🍞🍞
                🍞🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍞
               🍞🍅🍅{lista_ingredientes[0]*2}🍅🍅🍅{lista_ingredientes[2]*2}🍞
              🍞🍅{lista_ingredientes[1]*2}🍅🍅🍅{lista_ingredientes[0]*2}🍞
             🍞🍅{lista_ingredientes[2]*2}🍅🍅{lista_ingredientes[1]*2}🍅🍞
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
            #        🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞
            #     🍞🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍞
            #    🍞🍅🍅{lista_ingredientes}🍅🍞
            #   🍞🍅                        🍅🍞
            #  🍞🍅                          🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            # 🍞🍅                           🍅🍞
            #  🍞🍅                         🍅🍞
            #   🍞🍅                       🍅🍞
            #    🍞🍅                     🍅🍞
            #      🍞🍅🍅🍅🍅🍅🍅🍅🍅🍅🍞
            #        🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞