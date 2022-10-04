#PRIMERA FORMA DE CREAR UNA CLASE

"""class Coche():
    largoChasis=250
    anchoChase=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True
    
    def estado(Self):
        if(Self.enmarcha):
            return "El estado del coche es en marcha..."
        else:
            return "El estado del coche es parado..."

miCoche=Coche()

print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas,"ruedas")

miCoche.arrancar()
print(miCoche.estado())

print("-------------------------------------------------")

"""
#SEGUNDA FORMA DE CREAR UNA CLASE


class Coche():

#Un CONNSTRUCTOR es un metodo que le da estado inicial a los objetos

#Encapsulacion de Atributos y Metods de una clase --> Embolver, proteger una propiedad para que no sea modificado suv valor desde fuera de  la clase
#Lo podemos hacer precediendo el nombre de la propiedad con dos guiones de piso

    def __init__(self):
        
        self.__largoChasis=250
        self.__anchoChase=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo==True):
            return "El estado del coche es en marcha..."

        elif(self.__enmarcha and chequeo==False):
            return "Algo  ha salido mal en el chequeo, no pudemos arrancar"
        
        else:
            return "El estado del coche es parado..."
    
    def estado(Self):
        print("El largo del coche es: ", Self.__largoChasis)
        print("El coche tiene: ", Self.__ruedas,"ruedas")

    #Metodo chequeo interno para uso  justo antes de arrancar el coche
    #Para encapsular un metodo colocamos dos guiones bajos al inicio del nombre
    #Como esta encapsuladosolo se podra llamas desde la miasma clase, no es accesible desde fuera
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-------------------------------------------------")

#CREAMOS UN SEGUNDO OBJETO INSTANCIA DE COCHE
 
miCoche2=Coche()

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

print("commit al archivo")