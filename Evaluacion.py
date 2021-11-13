class vestimenta:
    def __init__(self, tipoZapatos, tipoPantalon, tipoCamisa, saco):
        self.__tipoZapatos = tipoZapatos
        self.__tipoPantalon = tipoPantalon
        self.__saco = saco
        self.__tipoCamisa = tipoCamisa

    def vestirse(self):
        print("La vestimenta que se esta usando actualmente es:")
        print("Zapatos: ", self.__tipoZapatos)
        print("Tipo de pantalon: ", self.__tipoPantalon)
        print("Un saco: ", self.__saco)
        print("Una camisa: ", self.__tipoCamisa)
        print("\n")

class Persona(vestimenta):
    def __init__(self, nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera,tipoZapatos, tipoPantalon, tipoCamisa, saco):
        super().__init__(tipoZapatos, tipoPantalon, tipoCamisa, saco)
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
    def __init__(self,nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, empresa, cargo, sueldo, tipoZapatos, tipoPantalon, tipoCamisa, saco):
        super().__init__(nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, tipoZapatos, tipoPantalon, tipoCamisa, saco)
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
    def setSueldo(self, nuevoSueldo):
        self.__sueldo=nuevoSueldo

    def presentacion(self):
        Persona.presentacion(self)
        print("La empresa donde trabajo se llama: ",self.getEmpresa())
        print("Mi cargo es: ",self.getCargo())
        print("Mi sueldo es de ",self.getSueldo(),"pesos al mes")
        print("\n")

class Gerente(Empleado):
    def __init__(self,nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, empresa, cargo, sueldo, tipoZapatos, tipoPantalon, tipoCamisa, saco):
        super().__init__(nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, empresa, cargo, sueldo, tipoZapatos, tipoPantalon, tipoCamisa, saco)

class Empresa:
    def __init__(self, nombre,ubicacion,):
        self.__nombre=nombre
        self.__ubicacion=ubicacion

    def Bienvenida(self):
        print("Buen dia la empresa",self.__nombre, "le da la bienvenida")
        print("Ubicada en ",self.__ubicacion)
        print("Con innovacion alcanzamos el mañana")
        print("\n")

class Trabajar():
    def __init__(self):
        pass

    def acciones(self):
        print("El dia laboral ha comenzado")


