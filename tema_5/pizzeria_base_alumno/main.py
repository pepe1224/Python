from pizzeria import Pizzeria
from pedido import Pedido
from pizza import Pizza
from ingredientes.queso import Queso
from ingredientes.carne import Carne
from ingredientes.vegetal import Vegetal

def main():
    pizzeria = Pizzeria()
    pedido = Pedido()

    while True:
        pizzeria.mostrar_menu()
        opcion = input("Opción: ")

        # crear pizza
        if opcion == "1":
            pizza = Pizza("Personalizada")
        

            # TODO: añadir ingredientes
            # muestra al usuario opciones para que elija qué ingredientes quiere añadir a su pizza, 
            # hasta que elija la opción de terminar pizza
            # Por ejemplo, así añadiría Queso y después terminaría la pizza.
            
            while True:
                pizzeria.mostrar_menu_ingredientes()
                opcion_ingredientes = int(input("Elige ingrediente: "))
                if opcion_ingredientes == 0:
                    break
                elif opcion_ingredientes == 1:
                    queso = Queso("🧀")
                    pizza.add_ingrediente(queso)
                elif opcion_ingredientes == 2:
                    carne = Carne("🥩")
                    pizza.add_ingrediente(carne)
                elif opcion_ingredientes == 3:
                    vegetal = Vegetal("🥬")
                    pizza.add_ingrediente(vegetal)
                else:
                    print("Preparando tu pizza...")
            """
                Ingredientes:
                1. Queso
                2. Carne
                3. Vegetal
                0. Terminar pizza

                Ingredientes:
                1. Queso
                2. Carne
                3. Vegetal
                0. Terminar pizza
            """
            pedido.add_pizza(pizza)
        elif opcion == "2":
            pedido.mostrar_pedido()
        elif opcion == "3":
            break

if __name__ == "__main__":
    main()
