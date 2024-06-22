import json
import networkx as nx
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
from usuarioClass import Usuario
from amigoClass import Amigo
import heapq
import math

class Graph:
    def __init__(self):
        self.Vertices = []
        self.label2v = dict()
        self.G = []  # Lista de listas de adyacencia
        self.Gnx = nx.Graph()
        self.edges_set = set()  # Para evitar aristas duplicadas

    def nodo(self, etiqueta, usuario):
        self.label2v[etiqueta] = len(self.Vertices)
        self.Vertices.append(usuario)
        self.G.append([])  # Inicializar lista de adyacencia vacía para el nuevo nodo
        self.Gnx.add_node(len(self.Vertices) - 1)  # Usar el índice del nodo como identificador

    def arista(self, u, v, peso):
        u_idx = self.label2v[u]
        v_idx = self.label2v[v]
        if (u_idx, v_idx) not in self.edges_set and (v_idx, u_idx) not in self.edges_set:
            self.G[u_idx].append((v_idx, peso))
            self.G[v_idx].append((u_idx, peso))  # Agregar la arista en ambos sentidos
            self.edges_set.add((u_idx, v_idx))  # Registrar la arista
            self.Gnx.add_edge(u_idx, v_idx, weight=peso)

    def nodos(self, etiquetas):
        for etiqueta in etiquetas:
            self.nodo(etiqueta, etiqueta)  # Crear nodos con etiquetas iguales a los nombres

    def aristas(self, u, vs):
        for v, peso in vs:
            self.arista(u, v, peso)

    def buscar_usuario_bfs(self, nombre, contrasenia=None):
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
            if isinstance(usuario, Usuario) and usuario.nombre == nombre:
                if contrasenia is None or usuario.contrasenia == contrasenia:
                    return usuario
            for v, _ in self.G[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return False
    
    def bfs_por_criterio_de_busqueda(self, criterio, valor):
        n = len(self.Vertices)
        visited = [False] * n  # Lista booleana para marcar los nodos visitados
        queue = []  # Cola para manejar los nodos en el orden de BFS
        resultados = []  # Lista para almacenar los usuarios que coincidan con el criterio de búsqueda
        # Buscar el primer Usuario en el grafo y agregar su índice a la cola, marcándolo como visitado
        for i, usuario in enumerate(self.Vertices):
            if isinstance(usuario, Usuario):
                queue.append(i)
                visited[i] = True
                break
            
        # Procesar cada nodo en la cola
        while queue:
            u = queue.pop(0)  # Extraer el nodo de la cola
            usuario = self.Vertices[u]  # Obtener el usuario correspondiente al nodo

            # Verificar si el usuario cumple con el criterio de búsqueda
            if criterio != 'numero_hermanos':
                if getattr(usuario, criterio, None) == valor:
                    resultados.append(usuario)  # Agregar el usuario a la lista de resultados
            else: 
                if getattr(usuario, criterio, None) == int(valor):
                    resultados.append(usuario)

            # Agregar todos los vecinos no visitados del usuario actual a la cola y marcarlos como visitados
            for v_idx, _ in self.G[u]:
                if not visited[v_idx]:
                    visited[v_idx] = True
                    queue.append(v_idx)

        return resultados
        




    def camino_minimo_Dijkstra(self, usuario_logueado, criterio, valor):
        # Step 1: Perform Dijkstra's algorithm to find shortest paths
        usuarios_destino = self.bfs_por_criterio_de_busqueda(criterio, valor)
        usuario_inicio = None
        for i, usuario in enumerate(self.Vertices):
            if isinstance(usuario, Usuario) and usuario.nombre == usuario_logueado.nombre:
                usuario_inicio = i
                break
        if usuario_inicio is None:
            return "Usuario logueado no encontrado en el grafo."

        n = len(self.G)
        visitado = [False] * n
        camino = [None] * n
        costo = [math.inf] * n
        costo[usuario_inicio] = 0
        cola_prioridad = [(0, usuario_inicio)]

        while cola_prioridad:
            g_u, u = heapq.heappop(cola_prioridad)
            if not visitado[u]:
                visitado[u] = True
                for v, w in self.G[u]:
                    f = g_u + w
                    if f < costo[v]:
                        costo[v] = f
                        camino[v] = u
                        heapq.heappush(cola_prioridad, (f, v))

        # Step 2: Create a subgraph containing all nodes involved in shortest paths
        subgrafo = Graph()

        # Add starting node to the subgraph
        subgrafo.nodo(self.Vertices[usuario_inicio].id, self.Vertices[usuario_inicio])


        # Add destination nodes and reconstruct shortest paths
        for destino in usuarios_destino:
            if destino.id in self.label2v:
                destino_idx = self.label2v[destino.id]
                if costo[destino_idx] < math.inf:
                    # Reconstruct the path from destino_idx to usuario_inicio
                    path = []
                    actual = destino_idx
                    while actual is not None:
                        path.append(actual)
                        actual = camino[actual]
                    path.reverse()

                    # Add nodes and edges to the subgraph based on the reconstructed path
                    for i in range(len(path) - 1):
                        nodo_actual = self.Vertices[path[i]].id
                        nodo_siguiente = self.Vertices[path[i + 1]].id
                        peso_arista = costo[path[i + 1]] - costo[path[i]]
                        if nodo_actual not in subgrafo.label2v:
                            subgrafo.nodo(nodo_actual, self.Vertices[path[i]])
                        if nodo_siguiente not in subgrafo.label2v:
                            subgrafo.nodo(nodo_siguiente, self.Vertices[path[i + 1]])
                        subgrafo.arista(nodo_actual, nodo_siguiente, peso_arista)

        return usuarios_destino, subgrafo



    # Función para crear un grafo a partir del archivo JSON
def cargar_usuarios_desde_archivo(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    grafo = Graph()
    # Crear nodos para cada usuario
    for usuario_data in json_data['usuarios']:
        amigos = list()
        for amigo in usuario_data['amigos']:
            amigos.append(amigo)
        usuario = Usuario(
            usuario_data['id'], usuario_data['nombre'], amigos,
            usuario_data['contrasenia'], usuario_data['comida_favorita'],
            usuario_data['pelicula_favorita'], usuario_data['lugar_favorito'],
            usuario_data['hobby'], usuario_data['fobia'], usuario_data['carrera'],
            usuario_data['numero_hermanos'], usuario_data['ciclo'],
            usuario_data['donde_vive'], usuario_data['tiene_novia'], usuario_data['solicitudes_amistad']
        )
        grafo.nodo(usuario_data['id'], usuario)
    # Crear aristas basadas en las relaciones de amistad
    for usuario_data in json_data['usuarios']:
        user_id = usuario_data['id']
        amigos = [(amigo['id'], amigo['relacion']) for amigo in usuario_data['amigos']]
        grafo.aristas(user_id, amigos)
    return grafo

def cargar_usuarios_desde_archivo_Graficar(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    grafo = Graph()

    # Crear nodos para cada usuario
    for usuario_data in json_data['usuarios']:
        grafo.nodo(usuario_data['id'], usuario_data['nombre'])

    # Crear aristas basadas en las relaciones de amistad
    for usuario_data in json_data['usuarios']:
        user_id = usuario_data['id']
        amigos = [(amigo['id'], amigo['relacion']) for amigo in usuario_data['amigos']]
        grafo.aristas(user_id, amigos)

    return grafo
