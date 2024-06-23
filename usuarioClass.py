import json
from amigoClass import Amigo

class Usuario:
    def _init_(self, id, nombre, amigos, contrasenia, comida_favorita, pelicula_favorita, lugar_favorito, hobby, fobia, carrera, numero_hermanos, ciclo, donde_vive, tiene_novia,solicitudes_amistad):
        self.id = id
        self.nombre = nombre
        self.amigos = amigos
        self.contrasenia = contrasenia
        self.comida_favorita = comida_favorita
        self.pelicula_favorita = pelicula_favorita
        self.lugar_favorito = lugar_favorito
        self.hobby = hobby
        self.fobia = fobia
        self.carrera = carrera
        self.numero_hermanos = numero_hermanos
        self.ciclo = ciclo
        self.donde_vive = donde_vive
        self.tiene_novia = tiene_novia
        self.solicitudes_amistad = solicitudes_amistad

    def _repr_(self):
        return (f"Usuario(id={self.id}, nombre='{self.nombre}', amigos={self.amigos}, "
                f"contrasenia='{self.contrasenia}', comida_favorita='{self.comida_favorita}', "
                f"pelicula_favorita='{self.pelicula_favorita}', lugar_favorito='{self.lugar_favorito}', "
                f"hobby='{self.hobby}', fobia='{self.fobia}', carrera='{self.carrera}', "
                f"numero_hermanos={self.numero_hermanos}, ciclo='{self.ciclo}', donde_vive='{self.donde_vive}', "
                f"tiene_novia='{self.tiene_novia}', solicitudes_amistad={self.solicitudes_amistad})")
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'amigos': self.amigos,
            'contrasenia': self.contrasenia,
            'comida_favorita': self.comida_favorita,
            'pelicula_favorita': self.pelicula_favorita,
            'lugar_favorito': self.lugar_favorito,
            'hobby': self.hobby,
            'fobia': self.fobia,
            'carrera': self.carrera,
            'numero_hermanos': self.numero_hermanos,
            'ciclo': self.ciclo,
            'donde_vive': self.donde_vive,
            'tiene_novia': self.tiene_novia,
            'solicitudes_amistad': self.solicitudes_amistad
        }

    def getNombre(self):
        return self.nombre
    
    def agregar_solicitud_amistad(self, id, nombre_usuario, resultado_cuestionario, filename):
        solicitud = {
            'id': int(id),
            'nombre_usuario': str(nombre_usuario),
            'resultado_cuestionario': int(resultado_cuestionario)
        }
        self.solicitudes_amistad.append(solicitud)
        self.actualizar_solicitudes_amistad_json(filename)
    
    def eliminar_solicitud_amistad(self, id, nombre_usuario=None, resultado_cuestionario=None, valor_relacion=None, filename=None):
        if resultado_cuestionario != None:
            solicitud = {
                'id': int(id),
                'nombre_usuario': str(nombre_usuario),
                'resultado_cuestionario': int(resultado_cuestionario)
            }
        amigo = {
            "id": id,
            "relacion": valor_relacion,
        }
        for soli in self.solicitudes_amistad:
            if solicitud == soli:
                self.solicitudes_amistad.remove(solicitud)
                self.actualizar_solicitudes_amistad_json(filename)
                self.amigos.append(amigo)
                self.actualizar_amigos_json(filename)
        if resultado_cuestionario == None: #sirve para agregar al usuario logueado como amigo del usuario que envio la solicitud 
            self.amigos.append(amigo)
            self.actualizar_amigos_json(filename)



    def actualizar_amigos_json(self, filename): #actualizar amigos
        with open(filename, 'r+', encoding='utf-8') as file:
            json_data = json.load(file)
            for usuario in json_data['usuarios']:
                if usuario['id'] == self.id:
                    usuario['amigos'] = self.amigos
                    break
            file.seek(0)
            json.dump(json_data, file, ensure_ascii=False, indent=4)
            file.truncate()

    def actualizar_solicitudes_amistad_json(self, filename): #actualiza solicitudes_amistad
        with open(filename, 'r+', encoding='utf-8') as file:
            json_data = json.load(file)
            for usuario in json_data['usuarios']:
                if usuario['id'] == self.id:
                    usuario['solicitudes_amistad'] = self.solicitudes_amistad
                    break
            file.seek(0)
            json.dump(json_data, file, ensure_ascii=False, indent=4)
            file.truncate()
    
def agregar_usuario_a_json(usuario, filename):
    with open(filename, 'r+', encoding='utf-8') as file:
        # Cargar los datos existentes
        json_data = json.load(file)
        
        # Convertir el usuario a un diccionario y agregarlo a la lista de usuarios
        nuevo_usuario = usuario.to_dict()
        json_data['usuarios'].append(nuevo_usuario)
        
        # Volver al inicio del archivo y escribir los datos actualizados
        file.seek(0)
        json.dump(json_data, file, ensure_ascii=False, indent=4)
        file.truncate()
