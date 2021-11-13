class Persona:
    def __init__(self, nombre,apellidoP,apellidoM, edad,altura,noTelefono):
        self.__nombre=nombre
        self.__apellidoP=apellidoP
        self.__apellidoM=apellidoM
        self.__edad=edad
        self.__altura=altura
        self.__noTelefono=noTelefono
#Getters y setters
    def __getNombre(self):
        return self.__nombre
    def __getApellidoP(self):
        return self.__apellidoP
    def __getApellidoM(self):
        return self.__apellidoM
    def __getEdad(self):
        return self.__edad
    def __getAltura(self):
        return self.__altura
    def __getTelefono
        return self.__noTelefono

    def setEdad(self, nuevaEdad):
        self.__edad=nuevaEdad
    def setAltura(self, nuevaAltura):
        self.__altura=nuevaAltura
    def setTelefono(self,nuevoTelefono):
        self.__noTelefono=nuevoTelefono

    def presentacion(self):
        pass

class Empleado(Persona):
    def __init__(self,nombre,apellidoP,apellidoM, edad,altura,noTelefono, cargo):
        super().__init__(nombre,apellidoP,apellidoM, edad,altura,noTelefono)
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