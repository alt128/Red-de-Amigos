import json
import random
import string
import secrets

nombres = ["Juan", "Maria", "Pedro", "Luis", "Ana", "Carlos", "Laura", "Diego", "Sofia", "Marta",
           "Alejandro", "Lucia", "Javier", "Elena", "Manuel", "Isabel", "David", "Claudia", "Antonio", "Paula",
           "Francisco", "Carmen", "Jorge", "Patricia", "Miguel", "Andrea", "Jose", "Beatriz", "Fernando", "Natalia"]
apellidos = ["Garcia", "Rodriguez", "Martinez", "Fernandez", "Lopez", "Perez", "Gonzalez", "Hernandez", "Sanchez", "Diaz",
             "Torres", "Ruiz", "Jimenez", "Moreno", "Alvarez", "Romero", "Navarro", "Molina", "Dominguez", "Gutierrez",
             "Ortega", "Vazquez", "Ramos", "Blanco", "Castro", "Suarez", "Ortiz", "Serrano", "Marin", "Iglesias"]

comida = ["Pizza", "Sushi", "Hamburguesa", "Ensalada", "Pasta", "Tacos", "Sandwich", "Parrillada", "Mariscos", "Helado"]
pelicula = ["El Padrino", "Titanic", "El Senor de los Anillos", "Avatar", "Harry Potter", "Star Wars", "Matrix", "Jurassic Park", "Indiana Jones", "Forrest Gump"]
lugar = ["Playa", "Montana", "Ciudad", "Campo", "Parque", "Bosque", "Desierto", "Lago", "Rio", "Pueblo"]
hobby = ["Deportes", "Leer", "Viajar", "Pintar", "Cocinar", "Bailar", "Fotografia", "Jardineria", "Musica", "Videojuegos"]
fobia = ["Aranas", "Alturas", "Espacios cerrados", "Multitudes", "Insectos", "Serpientes", "Oscuridad", "Agujas", "Perros", "Volar"]
carrera = ["Medicina", "Ingenieria", "Arquitectura", "Derecho", "Psicologia", "Administracion", "Biologia", "Economia", "Diseno", "Educacion"]
ciclo = ["Primer ciclo", "Segundo ciclo", "Tercer ciclo", "Cuarto ciclo", "Quinto ciclo", "Sexto ciclo", "Septimo ciclo", "Octavo ciclo", "Noveno ciclo", "Decimo ciclo"]
vive = ["Ciudad", "Pueblo", "Suburbio", "Campo", "Costa", "Montana", "Interior", "Extranjero", "Otro"]
novia = ["Si", "No"]

def generar_contrasena(longitud=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

usuarios = []
for i in range(1, 1501): # Generar usuarios
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    nombre_completo = f"{nombre} {apellido}"
    comida_fav = random.choice(comida)
    pelicula_fav = random.choice(pelicula)
    lugar_fav = random.choice(lugar)
    hobby_usr = random.choice(hobby)
    fobia_usr = random.choice(fobia)
    carrera_usr = random.choice(carrera)
    num_hermanos = random.randint(0, 5)
    ciclo_usr = random.choice(ciclo)
    vive_usr = random.choice(vive)
    tiene_novia = random.choice(novia)
    contrasenia = generar_contrasena()
    
    usuario = {
        "id": i,
        "nombre": nombre_completo,
        "amigos": [],
        "contrasenia": contrasenia,
        "comida_favorita": comida_fav,
        "pelicula_favorita": pelicula_fav,
        "lugar_favorito": lugar_fav,
        "hobby": hobby_usr,
        "fobia": fobia_usr,
        "carrera": carrera_usr,
        "numero_hermanos": num_hermanos,
        "ciclo": ciclo_usr,
        "donde_vive": vive_usr,
        "tiene_novia": tiene_novia,
        "solicitudes_amistad": []
    }
    usuarios.append(usuario)

usuarios_dict = {usuario["id"]: usuario for usuario in usuarios}

# Generar amigos y solicitudes de amistad
for usuario in usuarios:
    num_amigos = random.randint(1, 2)
    
    amigos_disponibles = [u["id"] for u in usuarios if u["id"] != usuario["id"]]
    random.shuffle(amigos_disponibles)
    
    for _ in range(min(num_amigos, len(amigos_disponibles))):
        amigo_id = amigos_disponibles.pop()
        relacion = random.randint(1, 10)
        
        # Añadir la amistad en ambos sentidos
        usuario["amigos"].append({"id": amigo_id, "relacion": relacion})
        usuarios_dict[amigo_id]["amigos"].append({"id": usuario["id"], "relacion": relacion})
    
    # Generar solicitudes de amistad
    num_solicitudes = random.randint(0, 3)
    for _ in range(num_solicitudes):
        solicitud_id = random.choice(amigos_disponibles)
        nombre_usuario_solicitud = usuarios_dict[solicitud_id]["nombre"]
        resultado_cuestionario = random.randint(1, 10)
        usuario["solicitudes_amistad"].append({
            "id": solicitud_id,
            "nombre_usuario": nombre_usuario_solicitud,
            "resultado_cuestionario": resultado_cuestionario
        })

data = {"usuarios": usuarios}

with open("usuariosPrueba.json", "w") as file:
    json.dump(data, file, indent=4)

print("Se ha generado el archivo usuariosPrueba.json con 1500 usuarios.")
