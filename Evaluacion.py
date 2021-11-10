class Persona:
    def __init__(self, nombre, edad,altura):
        self.__nombre=nombre
        self.__edad=edad
        self.__altura=altura

    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getAltura(self):
        return self.__altura

    def setEdad(self, nuevaEdad):
        self.__edad=nuevaEdad
    def setAltura(self, nuevaAltura):
        self.__altura=nuevaAltura

class Empleado(Persona):
    def __init__(self, nombre, edad,altura, cargo):
        super().__init__(nombre, edad,altura)
        self.__cargo =cargo

    def getCargo(self):
        return self.__cargo

    def setCargo(self, nuevoCargo):
        self.__cargo=nuevoCargo

class Gerente(Empleado):
    def __init__(self,nombre, edad,altura, cargo):
        super().__init__(nombre, edad,altura, cargo)

    def vestimenta(self):
        print("El gerente esta tiene puesto un saco con 3 botones")