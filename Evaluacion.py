class Persona:
    def __init__(self, nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera):
        self.__nombre=nombre
        self.__apellidoP=apellidoP
        self.__apellidoM=apellidoM
        self.__edad=edad
        self.__altura=altura
        self.__noTelefono=noTelefono
        self.__carrera=carrera
#Getters y setters
    def getNombre(self):
        return self.__nombre
    def getApellidoP(self):
        return self.__apellidoP
    def getApellidoM(self):
        return self.__apellidoM
    def getEdad(self):
        return self.__edad
    def getAltura(self):
        return self.__altura
    def getTelefono(self):
        return self.__noTelefono

    def setNombre(self, nombreCorrecto):
        self.__nombre=nombreCorrecto
    def setApellidoP(self,apellidoPCorrecto):
        self.__apellidoP=apellidoPCorrecto
    def setApellidoM(self,apellidoMCorrecto):
        self.__apellidoM=apellidoMCorrecto
    def setEdad(self, nuevaEdad):
        self.__edad=nuevaEdad
    def setAltura(self, nuevaAltura):
        self.__altura=nuevaAltura
    def setTelefono(self,nuevoTelefono):
        self.__noTelefono=nuevoTelefono

    def presentacion(self):
        print("Hola mi nombre es: ",self.getNombre(), self.getApellidoP(), self.getApellidoM())
        print("Tengo ",self.getEdad(),"años de edad")
        print("Mi altura es: ",self.getAltura())
        print("Mi numero de telefono es: ",self.getTelefono())

class Empleado(Persona):
    def __init__(self,nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, empresa, cargo, sueldo):
        super().__init__(nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera)
        self.__cargo =cargo
        self.__empresa=empresa
        self.__sueldo=sueldo

#setters y getters
    def getEmpresa(self):
        return self.__empresa
    def getCargo(self):
        return self.__cargo
    def getSueldo(self):
        return self.__sueldo

    def setEmpresa(self, nuevaEmpresa):
        self.__empresa=nuevaEmpresa
    def setCargo(self, nuevoCargo):
        self.__cargo=nuevoCargo

    def presetacion(self):
        Persona.presentacion(self)
        print(OCup)


class Gerente(Empleado):
    def __init__(self,nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, empresa, cargo, sueldo):
        super().__init__(nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, empresa, cargo, sueldo)

    def vestimenta(self):
        print("El gerente esta tiene puesto un saco con 3 botones")