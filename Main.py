import Evaluacion as Ev
#Primero se intancia la empresa
IMA=Ev.Empresa("Ideas Mecatronicas Avanzadas", "Calle Revolucion #10, Colonia Industrial Puebla Mexico")
#Se da la bienvenida a la empresa
IMA.Bienvenida()
#Se comienza el dia laboral
IMA.trabajar()
#Se insancia al gerente de la empresa
Luis=Ev.Gerente("Luis","Perez","Lopez",30,"1.80 m",2311405012,"Ingenieria en Gestion de empresas","IMA",
                "Gerente",30000,"de vestir color negros","de vestir","Blanca","Cafe con 3 botones")
#Se muestra la informacion de presentacion
Luis.presentacion()

#se instancian persona desempladas
Jose=Ev.Persona("Jose Maria","Suarez","Arroyo",26,"1.68 m",2311201650,"Ing Industrial","Zapatillas","falda","blanca de manga corta","sueter")
