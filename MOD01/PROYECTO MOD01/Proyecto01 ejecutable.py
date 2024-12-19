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
    
def ver_ordenados(): #2 Ordenar los usuarios edad descendiente
    usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario.edad, reverse=True)
    for usuario in usuarios_ordenados:
        print(usuario) 
    print("\n")    
    
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
    estudiante_actualizado = bool(input("¿Es estudiante? (True/False)"))
    actualizado = False
    
    for usuario in usuarios:
        if email.lower() == usuario.email.lower():
            usuario.estudiante = estudiante_actualizado
            actualizado = True
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


