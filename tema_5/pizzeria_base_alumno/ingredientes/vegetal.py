from ingredientes.ingrediente import Ingrediente

class Vegetal(Ingrediente):
    def __init__(self, nombre="Vegetal"):
        super(). __init__(nombre, "🥬")
