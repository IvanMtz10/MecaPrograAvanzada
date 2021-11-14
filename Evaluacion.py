class vestimenta:
    def __init__(self, tipoZapatos, tipoPantalon, tipoCamisa, saco):
        self.__tipoZapatos = tipoZapatos
        self.__tipoPantalon = tipoPantalon
        self.__saco = saco
        self.__tipoCamisa = tipoCamisa

#Getters y setters
    def getZapatos(self):
        return self.__tipoZapatos
    def getPantalon(self):
        return self.__tipoPantalon
    def getCamisa(self):
        return self.__tipoCamisa
    def getSaco(self):
        return self.__saco

    def setZapatos(self, nuevosZapatos):
        self.__tipoZapatos=nuevosZapatos
    def setPantalon(self, nuevoPantalon):
        self.__tipoPantalon=nuevoPantalon
    def setCamisa(self, nuevaCamisa):
        self.__tipoCamisa=nuevaCamisa
    def setSaco(self,nuevoSaco):
        self.__saco=nuevoSaco


    def vestirse(self):
        print("La vestimenta que estoy usando actualmente es:")
        print("Zapatos: ", self.getZapatos())
        print("Tipo de pantalon: ", self.getPantalon())
        print("Un saco: ", self.getSaco())
        print("Una camisa: ", self.getCamisa())


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
    def getCarrera(self):
        return self.__carrera

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
    def setCarrra(self, nuevaCarrera):
        self.__carrera=nuevaCarrera

    def presentacion(self):
        print("Hola mi nombre es: ",self.getNombre(), self.getApellidoP(), self.getApellidoM())
        print("Tengo ",self.getEdad(),"años de edad")
        print("Mi altura es: ",self.getAltura())
        print("Mi numero de telefono es: ",self.getTelefono())
        Persona.vestirse(self)

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
        print("\n")

class Gerente(Empleado):
    def __init__(self,nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, empresa, cargo, sueldo, tipoZapatos, tipoPantalon, tipoCamisa, saco):
        super().__init__(nombre,apellidoP,apellidoM, edad,altura,noTelefono,carrera, empresa, cargo, sueldo, tipoZapatos, tipoPantalon, tipoCamisa, saco)

class Empresa:
    def __init__(self, nombre,ubicacion,):
        self.__nombre=nombre
        self.__ubicacion=ubicacion

    def trabajar(self):
        print("El dia laboral ha comenzado")
        print("Como se esta contratando nuevo personal para la empresa el gerente realizara entrevistas a canditados")
        print("\n")

    def Bienvenida(self):
        print("Buen dia la empresa",self.__nombre, "le da la bienvenida")
        print("Ubicada en ",self.__ubicacion)
        print("Con innovacion alcanzamos el mañana")
        print("\n")

    def entrevistar(self,gerente, persona):
        if (gerente.getCargo() == "Gerente"):
            print(gerente.getNombre(), "esta entrevistando a :", persona.getNombre())
            print("Buen dia, le pido contestar una entrevista rapida")
            print("Para comenzar la entrevista seran datos personales")
            print("¿Cual es su nombre? ")
            print("Mi nombre es: ", persona.getNombre())
            print("¿Cual es su primer apellido? ")
            print("Mi apellido paterno es: ",persona.getApellidoP())
            print("¿Cual es su segundo apellido? ")
            print("Mi apellido materno es: ", persona.getApellidoM())
            print("¿Cual es su edad? ")
            print("Mi edad es: ",persona.getEdad())
            print("¿Cual es su altura? ")
            print("Mi altura es: ",persona.getAltura())
            print("¿Cual es su numero de telefono? ")
            print("Mi numero de telefono es: ", persona.getTelefono())
            print("¿Cual es su carrera? ")
            print("Mi carrera es:", persona.getCarrera())
            print("***************************************************")
            cont=5
            print("Ahora pasaremos a preguntas laborales, solo conteste 0 para NO y 1 para SI")
            while True:
                a = (input("¿Tiene experiencia mayor a 6 meses en alguna empresa? "))
                try:
                    n1 = float(a)
                    if n1<2 :
                        cont=cont+n1
                        break
                    else:
                        print("numero equivocado")
                except ValueError:
                    print("Por favor ingrese solo numeros")
            while True:
                b = (input("¿Esta dispuesta a rotar turnos de trabajo?"))
                try:
                    n2 = float(b)
                    if n2<2 :
                        cont=cont+n2
                        break
                    else:
                        print("numero equivocado")
                except ValueError:
                    print("Por favor ingrese solo numeros")
            while True:
                c = (input("¿Tiene disponibilidad de horario? "))
                try:
                    n3 = float(c)
                    if n3<2 :
                        cont=cont+n3
                        break
                    else:
                        print("numero equivocado")
                except ValueError:
                    print("Por favor ingrese solo numeros")
            while True:
                d = (input("¿Tiene disponibilidad para viajar?"))
                try:
                    n4 = float(d)
                    if n4<2 :
                        cont=cont+n4
                        break
                    else:
                        print("numero equivocado")
                except ValueError:
                    print("Por favor ingrese solo numeros")
            while True:
                e = input("¿Puede trabajar bajo presion?")
                try:
                    n5 = float(e)
                    if n5<2 :
                        cont=cont+n5
                        break
                    else:
                        print("numero equivocado")
                except ValueError:
                    print("Por favor ingrese solo numeros")
            if cont>=8:
                print("Felicidades su contratacion es inmediata")
            else:
                print("Muy bien hemos terminado, gracias por presentarse, nosotros le llamammos")
        else:
            print("ACCESO DENEGADO")