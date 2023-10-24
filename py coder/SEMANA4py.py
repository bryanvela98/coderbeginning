numeros= [1, 2,3,4,5]

for numero in numeros:
    print(numero)

# mensaje= ["Hola", "chau", "blanco", "negro","Hola", "chau", "blanco", "negro","Hola", "chau", "blanco", "negro"]
# for palabra in range(1,20,2):
#     print(palabra)

# # for i in range ( ):
# #     print(i)

# persona= {"nombre":"Gaston", "edad:" :30 }
# for clave in persona.items():
#     print (f"{clave}")


# frutas = ["manzana", "banana", "cereza"]
# for indice, fruta in enumerate (frutas):
#     print (f"Indice {indice}:{fruta} ")



# CICLO INFINITO!!!!!!!!!!!!!!!!
# # contador = 1
# # while contador <=5:
# #     print(contador)
# #     contador=+1

# contador = 1
# while contador <=5:
#     print(contador)
#     contador+=1

# contador= 1
# while contador<=5:
#     if contador==3:
#         break
#     print(contador)
#     contador+=1



# contador= 1
# while contador<=5:
#     if contador==3:
        
#         pass
#         print("Esto siempre se ejecuta")




       
# i=0
# while (i%2==0):
#     i=int(input("escribe un numero impar"))
#     if i==True:
#         break
#     i+i
# else:
#     print("este numero es impar")    
    




##ejemplo basico de funcionamiento
# num = 5
# while num > 0:
#     print(f"{num}")
#     num -= 1
# # print("Terminó el conteo!")
# #Declaramos una variable num y le asignamos el valor int 5.
# #Usamos la sentencia while para indicar que mientras que num sea mayor a 0 entremos al bloque de código.
# #Al evaluar num contra 0 nos indica que es True
# #Ingresamos al bloque de código, imprimimos num y le restamos 1 a num
# #Volvemos a repetir desde el paso 2 hasta que num deje de ser mayor a 0
# #Cuando la operación relacional de False saldremos del bucle 
# #Imprimimos por pantalla Terminó el conteo! 
# #Termina nuestro programa

# #Cuidado caemos en un bucle infinito
# num = 5
# while num > 0:
#     print(f"{num}")
#     num += 1 #Si en ves de restar suma simpre sera mayor que 0 y jamas saldra
# print("Terminó el conteo!")

# # i = 0
# # while i < 6:
# #     i += 1
# #     if i == 3:
# #         break
# #         #continue
# #         #pass
# #     print(i)

# # print("fin")

# # #AUMENTO DIFICULTA
# # chance  = 1
# # while chance <= 3:
# #     txt = input("Escribe SI: ")
# #     if txt == "SI":
# #         print("Ok, lo conseguiste en el intento", chance)
# #         break
# #     chance += 1
# # else:
# #     print("Has agotado tus tres intentos")

# # #Desafio Generico 1
# # numero = int(input("Numero: "))
# # suma = 0
# # while numero != 0:
# #     suma += numero
# #     numero = int(input("Numero: "))
# # else:
# #     print(f"La suma fue: {suma}")

# # ###NIVEL REAL while Un login
# # correoCorrecto = "developer@gmail.com"
# # contraCorrecta = "asd.456" 
# # estadoCuenta = "Activo"
# # n = 3 #intentos

# # correo = input("Correo: ")
# # pwd = input("Contraseña: ")

# # while (correo != correoCorrecto or pwd != contraCorrecta):
# #     print("Correo o contraseña INCORRECTA!!!")
# #     print(f"Le quedan {n} intentos")
# #     if( n != 0 ):
# #         correo = input("Correo: ")
# #         pwd = input("Contraseña: ")
# #     else:
# #         print("Usuario bloqueado")
# #         break
# #     n -= 1
# # else:
# #     print(f"Bienvenido {correo}!!!")

# # #DESAFIO
# # paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']

# # for numero, pais in enumerate(paises):
# #     print(f"{numero+1}.- {pais}")

# # suma = 0
# # #No toma el fin por eso mas 1
# # for numero in range(0,101):
# #     par = numero % 2
# #     if par == 0:
# #         suma += numero
# # print(f"La suma de los numeros impares es: {suma}")
# # #Con ayuda de las funciones del for
# # suma = 0
# # for numero in range(0,101,2):
# #     suma += numero
# # print(f"La suma de los numeros impares es: {suma}")

# # #USO porque el -1 no toma en cuenta el fin
# # for numero in range(10,0,-1):
# #     print(numero)

# # numero = input("Numero: ")
# # n = 0
# # for item in numero:
# #     n += 1
# # print(f"El numero {numero} tiene {n} digitos")

# # #SUPER BONUS EJERCICIO NUEVO QUE PODEMOS ANALISAR UNA AFTER pero veanlo antes

# # #Usando Continue and pass en un caso real
# # #Supongamos que matriculamos solo estudiantes Argentinos
# # #Con la excepcion de Colombianos los cuales seran extra al numero permitido
# # #uso del upper es para hacer las letras mayusculas
# # persona = 1
# # alumnos = []

# # while persona <= 3:
# #     print(f"Persona {persona}")
# #     pais = input("De que pais eres?\n")
# #     if (pais.upper() == "COLOMBIA"):
# #         pass
# #     elif (pais.upper == "NARNIA"):
# #         print("Chau")
# #         break
# #     elif (pais.upper() != "ARGENTINA"): #Uso de Upper para hacer todo siempre mayuscula
# #         print("Lo sentimos solo permitimos personal de Argentina!")
# #         continue
# #     else:
# #         persona += 1
# #     nombre = input("Nombre: ")
# #     alumnos.append(nombre)
# # else:
# #     print("Se acabaron las inscripciones!")
# #     print(alumnos)

# # #INDICE
# # #   0            1        2  
# # #['Martin', 'CAROLINA', 'RAUL']
# # for codigoEstudiante, nombre in enumerate(alumnos):
# #     print(f"Hola {nombre}, su codigo unico como estudiante es {codigoEstudiante}")

# # #indice     0         1        2        3            4            5       6
# # paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']
# # #       0    canada   #  0       ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']
# # for num, pais in enumerate(paises):
# #     print(f"{num+1}.- {pais}")
# # #1.- Canada
# # #2.- USA

# # indice = 0
# # numeros = [0,1,2,3,4,5,6,7,8,9,10]
# # for numero in numeros:
# #     print(numero)
# #     numeros[indice] *= 5
# #     indice += 1
# #     print(numeros)	

# # lista = [0,1,2,3,4,5,6,7,8,9,10]
# # for num in lista:
# #     print('Soy un valor de la lista y valgo', num)
# #     num *= 5
# #     print('Soy un valor de la lista y ahora valgo', num)








# # -------------------------
# # -------------
# # -------------------------------
# # -----------------

# Caso de uso de la vida Real sets
# Imaginemos que vamos a una convencion internacional de programadores
# Y queremos saber que paises nos visitaron
# Senso donde el usuario escribe
# seguir = "SI"
# mySetPais = set()
# myListaPais = []

# while (seguir.upper() == "SI"):
#     pais = input("Pais: ")
#     seguir = input("Desea seguir??? Escriba SI o NO\n")
#     mySetPais.add(pais.upper())
#     myListaPais.append(pais)

# print(f"Asistieron {len(mySetPais)} paises a la convecion")
# print(f"Asistieron {len(myListaPais)} paises a la convecion")
# print("################### SET ############################")
# for indice, pais in enumerate(mySetPais):
#     print(f"{indice+1}.- {pais}")
# print("\n################## LISTA ###########################")
# for indice, pais in enumerate(myListaPais):
#     print(f"{indice+1}.- {pais}")


# Caso de uso de la vida Real dic (llenado de persona y busqueda)
# Imaginemos que vamos a la misma convencion internacional de programadores
#Y queremos saber datos de quienes nos visitaron
#Senso donde el usuario escribe
# mas = "SI"
# ListaPersonas = []
# #persona = {}

# while (mas == "SI"):
#     #persona.clear()
#     nombre = input("Nombre: ")
#     apellido = input("Apellido: ")
#     pais = input("Pais: ")
#     edad = int(input("Edad: "))
#     correo = input("Correo: ")
#     #persona.update({"nombre": nombre, "apellido":apellido,"pais":pais,"edad":edad,"correo":correo})
#     ListaPersonas.append({"nombre": nombre, "apellido":apellido,"pais":pais,"edad":edad,"correo":correo})
#     print(ListaPersonas)
#     mas = input("Otro usuario (SI o NO): ").upper() #lower

# for persona in ListaPersonas:
#     print(persona)

# buscar = input("Buscar persona por nombre: ")

# for persona in ListaPersonas:
#     if (persona["nombre"].upper() == buscar.upper()):
#         print("Persona encontrada!!!")
#         print(persona)
#         break
# else:
#     print("Persona no encontrada!!!")



# ------------
# --------------------

# EJERCICIOS EJEMPLO DIAPOSITIVAS
# CALCULADORA
# while True:
    
#         num1 = float(input("Introduzca el primer número: "))
#         num2 = float(input("Introduzca el segundo número: "))

#         print("Menu:")
#         print("1. Mostrar la suma de los dos números")
#         print("2. Mostrar la resta de los dos números (el primero menos el segundo)")
#         print("3. Mostrar la multiplicación de los dos números")
#         print("4. Salir")

#         opcion = input("Elija una opción (1/2/3/4): ")

#         if opcion == '1':
#             print(f"La suma de {num1} y {num2} es: {num1 + num2}")
#         elif opcion == '2':
#             print(f"La resta de {num1} y {num2} es: {num1 - num2}")
#         elif opcion == '3':
#             print(f"La multiplicación de {num1} y {num2} es: {num1 * num2}")
#         elif opcion == '4':
#             print("Saliendo del programa.")
#             break
#         else:
#             print("Opción no válida. Por favor, elija una opción válida (1/2/3/4).")
   

# Usamos la función sum() con un rango que va desde 1 hasta 100 con un salto de 2 ya que siempre es par, impar, tambien se podria usar 
# validaciones
# resultado = sum(range(1, 101, 2))

# # Imprimimos
# print("La suma de todos los números enteros impares desde 0 hasta 100 es:", resultado)

# La media
# Escribe un programa que pida al usuario cuantos números quiere introducir. Luego, lee todos los números, guardándolos en una lista, y realiza una media aritmética de todos los valores.

# 🖐 Ayuda: Puedes utilizar la funciones sum() entre paréntesis se le pasa un iterable (lista, tupla, range) y devuelve la suma de todos sus elementos (sirve solo con valores numéricos)

# # Solicitar al usuario cuántos números desea introducir
# num_elementos = int(input("¿Cuántos números desea introducir?: "))

# # Inicializar una lista para almacenar los números
# numeros = []

# # Leer los números y guardarlos en la lista
# for i in range(num_elementos):
#     numero = float(input(f"Ingrese el número {i + 1}: "))
#     numeros.append(numero)

# # Calcular la media aritmética
# media = sum(numeros) / num_elementos

# # Mostrar la media aritmética
# print(f"La media aritmética de los números ingresados es: {media}")
