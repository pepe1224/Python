from ingredientes.ingrediente import Ingrediente

class Queso(Ingrediente):
    def __init__(self, nombre="Queso"):
        super().__init__(nombre, "🧀")
