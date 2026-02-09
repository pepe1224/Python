#cadena = 'cadenas'
#print(cadena[0:4])
# a = 'hola'
# b = 9
# print(a + str(b))

# texto = 'sosad; cola; espuma'
# cols = texto.split(',')
# for col in cols:
#     print(col)


# color = [1, 3, 2]
# #color.remove('azul')
# color.pop(1)
# print(color)

# a = "Hola"
# b = "Mundo"
# print(a + " " + b) 


class Hucha:
    def __init__(self):
        self.__dinero = 0

    def meter_dinero(self, cantidad):
        if cantidad > 0:
            self.__dinero += cantidad
    
    def ver_dinero(self):
        return self.__dinero
    
hucha = Hucha
hucha.meter_dinero(10)
print(hucha.ver_dinero())
assert hucha.ver_dinero()