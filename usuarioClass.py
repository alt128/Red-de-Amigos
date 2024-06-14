import json
from amigoClass import Amigo

class Usuario:
    def __init__(self, id, nombre, amigos, contrasenia, comida_favorita, pelicula_favorita, lugar_favorito, hobby, fobia, carrera, numero_hermanos, ciclo, donde_vive, tiene_novia):
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

    def __repr__(self):
        return (f"Usuario(id={self.id}, nombre='{self.nombre}', amigos={self.amigos}, "
                f"contrasenia='{self.contrasenia}', comida_favorita='{self.comida_favorita}', "
                f"pelicula_favorita='{self.pelicula_favorita}', lugar_favorito='{self.lugar_favorito}', "
                f"hobby='{self.hobby}', fobia='{self.fobia}', carrera='{self.carrera}', "
                f"numero_hermanos={self.numero_hermanos}, ciclo='{self.ciclo}', donde_vive='{self.donde_vive}', "
                f"tiene_novia='{self.tiene_novia}')")
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'amigos': [amigo.to_dict() for amigo in self.amigos],
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
            'tiene_novia': self.tiene_novia
        }