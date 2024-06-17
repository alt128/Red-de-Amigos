class Amigo:
    def __init__(self, id, relacion):
        self.id = id
        self.relacion = relacion

    def __repr__(self):
        return f"Amigo(id={self.id}, relacion={self.relacion})"
    
    def to_dict(self):
        return {
            'id': self.id,
            'relacion': self.relacion
        }