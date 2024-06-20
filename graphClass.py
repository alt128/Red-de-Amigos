import json
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from usuarioClass import Usuario
from amigoClass import Amigo
import heapq #en dijkstra

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
        self.Gnx.add_node(usuario.nombre) #etiqueta vertice grafo networkx

    def nodos(self, etiquetas):
        for etiqueta in etiquetas:
            self.nodo(etiqueta, etiqueta)  # Crear nodos con etiquetas iguales a los nombres

    def arista(self, u, v, peso):
        u_idx = self.label2v[u]
        v_idx = self.label2v[v]
        if (u_idx, v_idx) not in self.edges_set and (v_idx, u_idx) not in self.edges_set:
            self.G[u_idx].append((v_idx, peso))
            self.G[v_idx].append((u_idx, peso))  # Agregar la arista en ambos sentidos
            self.edges_set.add((u_idx, v_idx))  # Registrar la arista
            self.Gnx.add_edge(self.Vertices[u_idx].nombre, self.Vertices[v_idx].nombre, weight=peso) #se solicita el atributo nombre de la clase Usuario

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
            if isinstance(usuario, Usuario) and getattr(usuario, criterio, None) == valor:
                resultados.append(usuario)  # Agregar el usuario a la lista de resultados

            # Agregar todos los vecinos no visitados del usuario actual a la cola y marcarlos como visitados
            for v_idx, _ in self.G[u]:
                if not visited[v_idx]:
                    visited[v_idx] = True
                    queue.append(v_idx)

        return resultados
    
    def camino_minimo_Dijkstra(self, usuario_logueado, criterio, valor, frame):
        # Utilizar bfs_por_criterio_de_busqueda para obtener la lista de usuarios que cumplen con el criterio
        usuarios_destino = self.bfs_por_criterio_de_busqueda(criterio, valor)

        # Nodo inicial para Dijkstra es el usuario logueado
        nodo_inicial = usuario_logueado

        # Inicialización para Dijkstra
        distancias = {usuario: float('inf') for usuario in self.Vertices}
        distancias[nodo_inicial] = 0
        cola_prioridad = [(0, nodo_inicial)]  # Tuplas de (distancia_acumulada, nodo)

        # Estructuras para guardar los caminos mínimos
        caminos_minimos = {usuario: [] for usuario in self.Vertices}
        caminos_minimos[nodo_inicial] = [nodo_inicial]

        # Algoritmo de Dijkstra
        while cola_prioridad:
            distancia_actual, u = heapq.heappop(cola_prioridad)

            for v_idx, peso in self.G[self.label2v[u]]:
                v = self.Vertices[v_idx]
                distancia_nueva = distancia_actual + peso

                if distancia_nueva < distancias[v]:
                    distancias[v] = distancia_nueva
                    heapq.heappush(cola_prioridad, (distancia_nueva, v))
                    caminos_minimos[v] = caminos_minimos[u] + [v]

        grafo_caminos_minimos = Graph()
    
    def dibujar(self, frame):
        # Generate the graph layout and draw it using Matplotlib
        pos = nx.spring_layout(self.Gnx)
        plt.figure(figsize=(150, 130))
        nx.draw(self.Gnx, pos, with_labels=True, node_size=700, font_size=10)
        edge_labels = nx.get_edge_attributes(self.Gnx, 'weight')
        nx.draw_networkx_edge_labels(self.Gnx, pos, edge_labels=edge_labels)

        # Save the plot to a BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        buf.seek(0)
        plt.close()

        # Load the image with QPixmap directly from BytesIO
        pixmap = QPixmap()
        pixmap.loadFromData(buf.getvalue())

        # Create a QGraphicsScene and add the image
        escena = QGraphicsScene()
        vista = QGraphicsView(escena, frame)
        vista.setGeometry(frame.rect())
        vista.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        vista.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        item = QGraphicsPixmapItem(pixmap)
        escena.addItem(item)
        vista.show()

#funcion para crear un grafo a partir del archivo json
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
