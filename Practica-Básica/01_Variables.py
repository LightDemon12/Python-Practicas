#Variables son los tipos de datos que se pueden almacenar en un programa 

MyVariable = 5
print(MyVariable)

#Buena practica escribir las variables con la primera letra en mayuscula y las siguientes en minuscula volviendo a mayuscula en la siguiente palabra

MyVariableTypeString = "variable de tipo string"
print(MyVariableTypeString)

#otra manera de nombrar una variable es usando todo minusculas con guiones bajos para separar las palabras

my_variable_type_boolean = True
print(my_variable_type_boolean)

#una forma de usar las varibles es en un print con varios argumentos (concatenarlos) con comas entre cada uno

edad = 20
nombre = "Juan"
print ("holame llamo", nombre, "y tengo ", edad, "Años de edad")


#una funcion interesante por dar un ejemplo es str() que convierte un numero en un string

edad = 20
print("convietiendo la edad en un string",str(edad), type(str(edad)))

"""
hay varios tipos de funciones que se pueden usar en python para convertir un tipo de dato en otro por ejemplo:
int() convierte un string en un entero
float() convierte un string en un flotante
bool() convierte un string en un booleano
str() convierte un entero, flotante o booleano en un string
"""

# funciones del sistema

print(len(nombre)) #devuelve la longitud de un string
print(nombre.upper()) #devuelve el string en mayusculas

#variables en una sola linea
#aun que se puede hacer en una sola linea no es recomendable ya que se puede volver confuso, es mejor hacerlo en varias lineas
nombreA, edada, ciudada = "Angel", 23, "Guateamala"

print("Mi nombre es",nombreA,"y tengo" ,edada, "años de edad", "Ademas vivo en",ciudada)


#en programas de consola se pueden usar los input para pedir datos al usuario

nombreB = input("Ingrese su nombre: ")
edadB = input("ingrese su edad: ")


#luego con ello podemos hacer un print con los datos ingresados

print ("Bienvenido", nombreB, "tu edad es de ", edadB, "años ")

#una variable puede ser reasignada con otro valor por ejemplo 

nombreB = "Juan"
print ("Bienvenido", nombreB, "tu edad es de ", edadB, "años ")

#tambien se puede reasignar con un input
nombreB = input("ingrese de nuevo su nombre: ")
print ("Bienvenido", nombreB, "tu edad es de ", edadB, "años ")

#una variable ingresada por input siempre sera de tipo string por lo que si se quiere hacer una operacion con ella se debe convertir a un tipo de dato numerico

print("Tipo al ingresar",type(edadB))

print("Tipo al convertir",type(int(edadB)))

#se puede forzar a que una variable sea de un tipo de dato especifico con la funcion de conversion

tipo = str = "tipo 01"
tipo = 32
print(type(tipo))# se convirtio a un entero

