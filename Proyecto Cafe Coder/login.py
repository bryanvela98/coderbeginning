#Pre entrega numero 1
import re  # importamos el modulo de expresiones regulares 

usuarios = {} #Se crea diccionario para almacenar usuarios

# Función para validar usuario (menor a 8 caracteres y que sea solo letras)
def validar_nombre_usuario(username):
    return len(username) <= 8 and username.isalpha()

# Función para validar una contraseña (menor a 8 caracteres y contenga al menos una mayuscula)
def validar_password(password):
    return len(password) <= 8 and any(char.isupper() for char in password)

#Se crea la funcion REGISTRAR USUARIO, verificacion y validación de usuario y contraseña, y si fue registrado con exito
def registrar_usuario(username, password):
    if validar_nombre_usuario(username) and validar_password(password):
        usuarios[username] = password
        print("Usuario registrado con éxito.")
    else:
        print("Error: El nombre de usuario debe tener menos de 8 letras y solo contener letras. La contraseña debe tener menos de 8 caracteres y contener al menos una letra mayúscula.")

#Se crea función para inicio de sesión
def iniciar_sesion(username, password):
    if username in usuarios and usuarios[username] == password: #busca los parametros en el diccionario creado previamente
        return True
    else:
        return False
    
# Función para mostrar los datos almacenados en el diccionario
def mostrar_datos():
    print("La data almacenada es:")
    for username, password in usuarios.items():
        print(f"Usuario: {username}, Contraseña: {password}")
        
#Creamos la funcion principal de nuestro sistema, basado en tres opciones de eleccion
def main():
    while True:
        print("Bienvenido al sistema de login de Bryan Vela:")    #como se muestra a continuacion se tendran las siguientes opciones
        opcion = input("1. Registrarse\n2. Iniciar sesión\n3. Salir\nElija una opción: ")

        if opcion == "1":   
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            registrar_usuario(username, password)

        elif opcion == "2":
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")

            if username in usuarios and usuarios[username] == password:
                print("Se inicio sesión con éxito.")
            else:
                print("Nombre de usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Gracias por usar nuestro sistema de login.")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

#Se utiliza para determinar si el script se está ejecutando directamente y, por lo tanto, permite que el código principal se ejecute solo en ese caso
if __name__ == "__main__":
    main()
