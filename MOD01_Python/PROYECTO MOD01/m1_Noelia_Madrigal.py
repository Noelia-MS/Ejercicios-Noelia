# %%
class Usuario:
    
    def __init__(self, nombre, apellido, CCAA, email, edad, altura, estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.CCAA = CCAA
        self.email = (f"{nombre.lower()}.{apellido.lower()}@{CCAA.lower()}.com")
        self.edad = edad
        self.altura = altura
        self.estudiante = estudiante
    
    def __str__(self):
        es_estudiante = "Si" if self.estudiante else "No"
        return f"Usuario: {self.nombre}, {self.apellido}, email {self.email}, edad {self.edad} años, altura {self.altura} m, estudiante {es_estudiante}"

# %%
Usuario1 = Usuario("Lola", "Flores", "Andalucia", "email", 51, 1.55, False)
Usuario2 = Usuario("Rocio", "Durcal", "Madrid", "email", 66, 1.60, False)
Usuario3 = Usuario("Manuel", "Serrat", "Catalunya", "email", 80, 1.81, True)

usuarios = [Usuario1, Usuario2, Usuario3]

# %%
menu = """Bienvenid@, selecciona una opcion: 
1 - Ver todos los usuarios
2 - Ordenar los usuarios por edad
3 - Ver un usuario por email
4 - Crear nuevo usuario
5 - Actualizar usuario existente
6 - Borrar usuario por email
7 - Borrar todos los usuarios
8 - Salir """


# %%
# Funciones

def ver_todos(): #1 Ver todos los usuarios
    if not usuarios:
        print("No hay usuarios")
    else:
        for usuario in usuarios:
            print(usuario)       
    print("\n")
    
def ver_ordenados(): #2 Ordenar los usuarios edad ascendente o descendente
    while True: 
        orden = int(input("Elige el orden: 1-ascendente o 2-descendente"))
        if orden == 1:
            reverse = False
            break
        elif orden == 2:
            reverse = True
            break
        else:
            print ("Opción incorrecta, selecciona 1 o 2")
         
    usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario.edad, reverse=reverse)
    for usuario in usuarios_ordenados:
        print(usuario) 
    
def ver_correo(): #3 Ver un usuario por email
    email = input("Escribe el email del usuario")
    for usuario in usuarios:
        if email == usuario.email:
            print(usuario)
            break   
    else:
        print("No existe usuario o email incorrecto")
    
    
def crear_usuario(): #4 Crear un usuario
    print("Vas a crear un nuevo usuario")
    nombre = input("Escribe el nombre")
    apellido = input ("Escribe el apellido")
    CCAA = input ("Comunidad autonóma de nacimiento")
    email = (f"{nombre.lower()}.{apellido.lower()}@{CCAA.lower()}.com")
    edad = int(input ("Escribe la edad"))
    altura = float(input ("Altura en metros"))
    estudiante = bool(input("¿Es estudiante? (True/False)"))
    nuevo_usuario = Usuario(nombre, apellido, CCAA, email, edad, altura, estudiante)
    usuarios.append(nuevo_usuario)
    print("Usuario creado correctamente")


def actualizar_usuario(): #5 Actualizar un usuario existente
    email = input("Escribe el email del usuario a modificar")
    actualizado = False
    
    for usuario in usuarios:
        if email.lower() == usuario.email.lower():
            print("Elige que atributo quieres actualizar: 1. Nombre 2. Apellido 3.Email 4. Edad 5. Altura 6. Estudiante")
            opcion = input("Selecciona 1/2/3/4/5/6")
            if opcion == "1":
                nuevo_nombre = input("Escribe el nuevo nombre")
                usuario.nombre = nuevo_nombre
                actualizado = True
            elif opcion == "2":
                nuevo_apellido = input("Escribe el nuevo apellido")
                usuario.apellido = nuevo_apellido
                actualizado = True
            elif opcion == "3":
                nuevo_email = (input("Escribe el nuevo email"))
                usuario.email = nuevo_email
                actualizado = True            
            elif opcion == "4":
                nueva_edad = int(input("Escribe la nueva edad"))
                usuario.edad = nueva_edad
                actualizado = True
            elif opcion == "5":
                nueva_altura = int(input("Escribe la nueva altura"))
                usuario.edad = nueva_altura
                actualizado = True
            elif opcion == "6":
                estudiante_actualizado = bool(input("¿Es estudiante? (True/False): "))
                usuario.estudiante = estudiante_actualizado
                actualizado = True   
            else:
                print("Opción no válida.")    
            break
    
    if actualizado:
        print("Usuario actualizado correctamente")
    else: 
        print("No existe usuario o email incorrecto")        
            
        
def borrar_usuario(): #6 Borrar un usuario
    email = input("Escribe el email del usuario a borrar")
    for usuario in usuarios: 
        if email.lower() == usuario.email.lower():
            usuarios.remove(usuario)
            print ("Usuario eliminado correctamente")
            break            
    else:
        print("No existe usuario o email incorrecto") 

def borrar_todos(): #7 Borrar todos los usuarios
    print("Vas a borrar la lista de usuarios")
    borrar_usuarios = input("Escribe BORRAR para confirmar")
    if borrar_usuarios == "BORRAR":
        usuarios.clear()
        print("Usuarios eliminados correctamente")
    else: 
        print("Saliendo al menú")           
                
    

# %%
while True:
    option = int(input(menu))
    match option:
        case 1: 
            ver_todos()        
        case 2: 
            ver_ordenados()                
        case 3: 
            ver_correo()            
        case 4:
            crear_usuario()        
        case 5: 
            actualizar_usuario()        
        case 6: 
            borrar_usuario()                    
        case 7:
            borrar_todos()        
        case 8:
            print ("Hasta luego")
            break
        case _: 
            print ("Opción incorrecta")


