import json
from usuarioClass import Usuario
from amigoClass import Amigo

class Graph:
  def __init__(self):
      self.Vertices = []
      self.label2v = dict()
      self.G = []
      self.edges_set = set()  # Para evitar aristas duplicadas
  def node(self, label, name):
      self.label2v[label] = len(self.Vertices)
      self.Vertices.append(name)
      self.G.append([])
  def nodes(self, labels):
      for label in labels:
          self.node(label)
  def edge(self, u, v, weight):
      u_idx = self.label2v[u]
      v_idx = self.label2v[v]
      if (u_idx, v_idx) not in self.edges_set and (v_idx, u_idx) not in self.edges_set:
          self.G[u_idx].append((v_idx, weight))
          self.G[v_idx].append((u_idx, weight))  # Agregar la arista en ambos sentidos
          self.edges_set.add((u_idx, v_idx))  # Registrar la arista
  def edges(self, u, vs):
      for v, weight in vs:
          self.edge(u, v, weight)
  
  def buscar_usuario_bfs(self, nombre, contrasenia):
      n = len(self.G)
      visited = [False] * n
      queue = []
      for i, usuario in enumerate(self.Vertices):
          if isinstance(usuario, Usuario):
              queue.append(i)
              visited[i] = True
              break
      while queue:
          u = queue.pop(0)
          usuario = self.Vertices[u]
          if isinstance(usuario, Usuario) and usuario.nombre == nombre and usuario.contrasenia == contrasenia:
              return True
          for v, _ in self.G[u]:
              if not visited[v]:
                  visited[v] = True
                  queue.append(v)
      return False
  
#funcion para crear un grafo a partir del archivo json
def cargar_usuarios_desde_archivo(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    grafo = Graph()
    # Crear nodos para cada usuario
    for usuario_data in json_data['usuarios']:
        amigos = [Amigo(amigo['id'], amigo['relacion']) for amigo in usuario_data['amigos']]
        usuario = Usuario(
            usuario_data['id'], usuario_data['nombre'], amigos,
            usuario_data['contrasenia'], usuario_data['comida_favorita'],
            usuario_data['pelicula_favorita'], usuario_data['lugar_favorito'],
            usuario_data['hobby'], usuario_data['fobia'], usuario_data['carrera'],
            usuario_data['numero_hermanos'], usuario_data['ciclo'],
            usuario_data['donde_vive'], usuario_data['tiene_novia']
        )
        grafo.node(usuario_data['id'], usuario)
    # Crear aristas basadas en las relaciones de amistad
    for usuario_data in json_data['usuarios']:
        user_id = usuario_data['id']
        amigos = [(amigo['id'], amigo['relacion']) for amigo in usuario_data['amigos']]
        grafo.edges(user_id, amigos)
    return grafo
