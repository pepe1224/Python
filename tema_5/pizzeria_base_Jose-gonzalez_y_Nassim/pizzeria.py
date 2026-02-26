class Pizzeria:
    def mostrar_menu(self):
        print("1. Crear pizza")
        print("2. Ver pedido")
        print("3. Salir")

    def mostrar_menu_ingredientes(self):
        print("""
            Ingredientes:
            1. Queso
            2. Carne
            3. Vegetal
            0. Terminar pizza
        """)
