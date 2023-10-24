

#Operadores y operando
#Ejemplos: 
# Operando operador operando
#    1        +          1      
#
print("Suma de dos numeros: ")
num1 = int(input("Ingrese num1: "))
num2 = int(input("Ingrese num2: "))

res = num1 + num2

print(f"El resultado es: {res}")

#Logica True or False
marcaTelefono = "Google pixel"
colorTelefono = "Negro"

            #Negro == Azul? FALSE
resultado = colorTelefono == "Azul"
#resultado = "Negro" == "Azul"
print(resultado)

#En programacion podemos hacerlo con cosas matematicas
#False
print(1+1 == 3)
#True
print(1+1 == 2)

#operadores relacionales
#Igualdad operando1 == operando2 -> se lee operando1 es igual a operando2?
#Tener cuidado con la asignacion de variable
#diferente operando1 != operando2 -> se lee operando1 es diferente a operando2?
#Menor que operando1 < operando2 -> se lee operando1 es menor que operando2?
#Menor o igual que operando1 <= operando2 -> se lee operando1 es menor o igual que operando2?
#mayor que operando1 > operando2 -> se lee operando1 es mayor que operando2?
#mayor o igual que operando1 >= operando2 -> se lee operando1 es mayor o igual que operando2?

num1 = int(input("Ingrese num1: "))
num2 = int(input("Ingrese num2: "))
print(num1 == num2)
#Caso gracioso xD
print(True + 2)

#Ejemplos Expresiones dentro de una lista correlo en python y ve el comportamiento
expresiones = [
False == True,
10 >= 2*4,
33/3 == 11,
True > False,
True*5 == 2.5*2
]
print(expresiones)

#Negacion
print(not True == False)

expresiones = [not False,not 3 == 5,33/3 == 11 and 5 > 2,
True or False,
True*5 == 2.5*2 or 123 >= 23,
12 > 7 and True < False
]
print(expresiones)


#Como se descompone la logica
#a = 15
#b = 12 
#a ** b / 3**a / a * b >= 15 and not (a%b**2) != 0
#15 ** 12 / 3**15 / 15 * 12 >= 15 and not (15%12**2) != 0
#129746337890625 / 14348907 / 15 * 12 >= 15 and not (15) != 0
#129746337890625 / 14348907 / 180 >= 15 and not (15) != 0
#50234.70 >= 15 and not 15 != 0
#True and not True
#True and False
#False

#DESAFIO

nombre = input("Ingresar Nombre: ")
edad = int(input("Ingresar edad: "))

print(f"Su nombre({nombre}) es diferente a **** {nombre != '****'}")
print(f"Su edad({edad}) es mayor que 10 y a su vez menor que 18 {edad > 10 and edad < 18}")
print(f"La longuitud de su nombre ({nombre}) es >= 3 pero tambien <  10 {len(nombre) >= 3 and len(nombre) < 10 }")
print(f"La edad ({edad}) multiplicada por 4 es mayor a 40 {edad*4 > 40}")












#Flujo continuo
nombre = input("Ingresar nombre: ")
edad = int(input("Su edad es: "))
print(f"Hola {nombre} su edad es {edad}")


if True:
  print(1)
if True:
  print(2)

print('XXXXXXX')

if True:
  print(3)
elif True:
  print(4)

#Flujo aplicando condiciones
edad = int(input("Su edad es: "))
if (edad > 18):#Si se cumple entro aqui
    print(f"Hola {nombre} eres un adulto mayor de edad")
print("Esto se ejecutara siempre porque esta fuera del if")

edad = int(input("Su edad es: "))
if (edad > 18): #Si se cumple entro aqui
    print(f"Hola {nombre} eres un adulto mayor de edad")
else:#Si lo anterior no se cumple entro aqui
    print(f"Hola {nombre} eres un menor de edad")
print("Esto se ejecutara siempre porque esta fuera del if y el else")

#ALERTA ESTE ES UN CASO DE LOGICA MALA CON RESULTADO NO DESEADO SE PUEDE ANALIZAR
#En el siguiente codigo se muestra una posible solucion
#Flujo aplicando condiciones AGREGANDO VARIOS CASOS ALTERNOS (SI) (SINO,SI) (SINO) caso malo
edad = float(input("Edad: "))

if edad <= 1: 
    print("Eres un bebe")
elif edad <= 12: # edad>1 and edad<=12
    print("Eres un niño")
elif edad <= 18:
    print("Eres un adolecente")
    if edad == 13:
        print(3*9)
elif edad <= 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

#DESAFIO

nombre = input("¿Cómo te llamas? ")
print("Presiona M si prefieres MARVEL y presiona C si prefieres C")
preferencia = input("¿Cuál es tu preferencia (M o C)? ")

if(preferencia == "M" or preferencia == "C"):
    if (inicial > "M" or inicial < "C" ):    
        grupo = "A"
    else:
        grupo = "B"
else:
    grupo = ""
    print("USUUUUARRRIOOOOO DIJE M O C >:/")

print(f"{nombre} perteneces al grupo {grupo}")

num1 = float(input("Num1: "))
num2 = float(input("Num2: "))
res = 0
ban = 0

operacion = input("Operacion: ")

if operacion == "+":
    res = num1 + num2
elif operacion == "-":
    res = num1 - num2
elif operacion == "*":
    res = num1 * num2
elif operacion == "/":
    if num2 == 0:
        print("Division entre cero no se puede")
    else:
        res = num1/num2
else:
    print("Operacion no valida")
    ban = 1

if ban == 1 and res == 0:
    print("Sucedio un error")
else:
    print(f"El resultado es: {res}")