import json
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
        self.G = []  #Lista de adyacencia
        self.edges_set = set()#Para evitar aristas duplicadas, puesto que si Pablo tiene registrado de amigo a Lucia, Lucia tambien tiene registrado a Pablo

    def nodo(self, etiqueta, usuario):
        self.label2v[etiqueta] = len(self.Vertices)
        self.Vertices.append(usuario)
        self.G.append([]) 

    def arista(self, u, v, peso):
        u_idx = self.label2v[u]
        v_idx = self.label2v[v]
        if (u_idx, v_idx) not in self.edges_set and (v_idx, u_idx) not in self.edges_set:
            #Agregar la arista en ambos sentidos
            self.G[u_idx].append((v_idx, peso))
            self.G[v_idx].append((u_idx, peso))  
            self.edges_set.add((u_idx, v_idx))  #se registra la arista

    def aristas(self, u, vs):
        for v, peso in vs:
            self.arista(u, v, peso)

    def buscar_usuario_bfs(self, nombre, contrasenia=None): #sirve para validar inicio sesion
        n = len(self.G)
        visited = [False] * n
        queue = []
        for i, usuario in enumerate(self.Vertices): #nodo para iniciar busqueda
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
        visited = [False] * n 
        queue = []
        resultados = []  #Lista para almacenar los usuarios que coincidan con el criterio de búsqueda
        #sirve para buscar primer Usuario en el grafo y agregar su índice a la cola, y marcarlo como visitado
        for i, usuario in enumerate(self.Vertices):
            queue.append(i)
            visited[i] = True
            break
        while queue:
            u = queue.pop(0)  # Extraer el nodo de la cola
            usuario = self.Vertices[u]  # Obtener el usuario correspondiente al nodo

            #Se verifica si el usuario cumple con el criterio de búsqueda
            if criterio != 'numero_hermanos':
                if getattr(usuario, criterio, None) == valor:
                    resultados.append(usuario)
            else: 
                if getattr(usuario, criterio, None) == int(valor):
                    resultados.append(usuario)

            #Se agrega todos los vecinos no visitados del usuario actual a la cola y marcamos como visitados
            for v_idx, _ in self.G[u]:
                if not visited[v_idx]:
                    visited[v_idx] = True
                    queue.append(v_idx)

        return resultados
        

    def camino_minimo_Dijkstra(self, usuario_logueado, criterio, valor):
        usuarios_destino = self.bfs_por_criterio_de_busqueda(criterio, valor)

        usuario_inicio = None
        for i, usuario in enumerate(self.Vertices):
            if isinstance(usuario, Usuario) and usuario.nombre == usuario_logueado.nombre:
                usuario_inicio = i
                break
        if usuario_inicio is None:
            return "Usuario logueado no encontrado en el grafo."
        #variables para hacer el dijkstra
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
        subgrafo = Graph()

        subgrafo.nodo(self.Vertices[usuario_inicio].id, self.Vertices[usuario_inicio])

        for destino in usuarios_destino:
            if destino.id in self.label2v:
                destino_idx = self.label2v[destino.id]
                if costo[destino_idx] < math.inf:
                    path = []
                    actual = destino_idx
                    while actual is not None:
                        path.append(actual)
                        actual = camino[actual]
                    path.reverse()

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

    def dibujar(self, frame, usuario_logueado_nombre, usuarios_destino=None):
        # Crear lista de nodos para D3.js
        nodos = [{'id': idx, 'nombre': usuario.nombre} for idx, usuario in enumerate(self.Vertices)]

        usuario_logueado_idx = -1 #identificar al usuario logueado
        for idx, usuario in enumerate(self.Vertices):
            if usuario.nombre == usuario_logueado_nombre:
                usuario_logueado_idx = idx
                break

        # lista de enlaces para D3.js
        enlaces = []
        for u_idx, vecinos in enumerate(self.G):
            for v_idx, peso in vecinos:
                enlace = {'source': u_idx, 'target': v_idx, 'peso': peso}
                enlaces.append(enlace)

        # Color nodos correspondientes a usuarios_destino de naranja
        if usuarios_destino: 
            for usuario in usuarios_destino:
                for nodo in nodos:
                    if nodo['nombre'] == usuario.nombre:
                        nodo['color'] = "orange"

        #HTML con el código D3.js y los datos
        contenido_html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Visualización de Grafo con D3.js</title>
            <script src="https://d3js.org/d3.v6.min.js"></script>
            <style>
                .link {{
                    stroke: #999;
                    stroke-opacity: 0.6;
                }}
                .node {{
                    stroke: #fff;
                    stroke-width: 1.5px;
                }}
                text {{
                    font: 10px sans-serif;
                }}
                svg {{
                    border: 1px solid black;
                }}
            </style>
        </head>
        <body>
            <div id="graph"></div>
            <script>
                var nodos = {json.dumps(nodos)};
                var enlaces = {json.dumps(enlaces)};
                var usuarioLogueadoIdx = {usuario_logueado_idx};

                var width = 800;
                var height = 600;

                var svg = d3.select("#graph")
                    .append("svg")
                    .attr("width", width)
                    .attr("height", height)
                    .call(d3.zoom().on("zoom", function (event) {{
                        svg.attr("transform", event.transform)
                    }}))
                    .append("g");

                var simulation = d3.forceSimulation(nodos)
                    .force("link", d3.forceLink(enlaces).id(d => d.id).distance(d => d.peso * 10))
                    .force("charge", d3.forceManyBody().strength(-400))
                    .force("center", d3.forceCenter(width / 2, height / 2));

                var link = svg.append("g")
                    .attr("class", "links")
                    .selectAll("line")
                    .data(enlaces)
                    .enter().append("line")
                    .attr("class", "link")
                    .attr("stroke-width", d => Math.sqrt(d.peso));

                var node = svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("circle")
                    .data(nodos)
                    .enter().append("circle")
                    .attr("class", "node")
                    .attr("r", d => d.id === usuarioLogueadoIdx ? 30 : 10)  // Cambiar radio según el nodo de inicio
                    .attr("fill", d => d.color ? d.color : (d.id === usuarioLogueadoIdx ? "red" : "#69b3a2"))  // Colores diferentes para nodo de inicio y usuario logueado
                    .call(d3.drag()
                        .on("start", dragstarted)
                        .on("drag", dragged)
                        .on("end", dragended));

                var label = svg.append("g")
                    .attr("class", "labels")
                    .selectAll("text")
                    .data(nodos)
                    .enter().append("text")
                    .attr("dy", -3)
                    .text(d => d.nombre);

                var edgeLabel = svg.append("g")
                    .attr("class", "edge-labels")
                    .selectAll("text")
                    .data(enlaces)
                    .enter().append("text")
                    .attr("class", "edge-label")
                    .attr("fill", "#000")
                    .attr("font-size", "10px")
                    .text(d => d.peso);

                simulation
                    .nodes(nodos)
                    .on("tick", ticked);

                simulation.force("link")
                    .links(enlaces);

                function ticked() {{
                    link
                        .attr("x1", d => d.source.x)
                        .attr("y1", d => d.source.y)
                        .attr("x2", d => d.target.x)
                        .attr("y2", d => d.target.y);

                    node
                        .attr("cx", d => d.x)
                        .attr("cy", d => d.y);

                    label
                        .attr("x", d => d.x)
                        .attr("y", d => d.y);

                    edgeLabel
                        .attr("x", d => (d.source.x + d.target.x) / 2)
                        .attr("y", d => (d.source.y + d.target.y) / 2);
                }}

                function dragstarted(event, d) {{
                    if (!event.active) simulation.alphaTarget(0.3).restart();
                    d.fx = d.x;
                    d.fy = d.y;
                }}

                function dragged(event, d) {{
                    d.fx = event.x;
                    d.fy = event.y;
                }}

                function dragended(event, d) {{
                    if (!event.active) simulation.alphaTarget(0);
                    d.fx = null;
                    d.fy = null;
                }}
            </script>
        </body>
        </html>
        """

        # vista de QWebEngineView y carga del HTML
        vista = QWebEngineView(frame)
        vista.setHtml(contenido_html)
        vista.setGeometry(frame.rect())
        vista.show()

def cargar_usuarios_desde_archivo(filename): # Función para crear un grafo a partir del archivo JSON
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    grafo = Graph()
    # nodos para cada usuario
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
    # aristas basadas en las relaciones de amistad
    for usuario_data in json_data['usuarios']:
        user_id = usuario_data['id']
        amigos = [(amigo['id'], amigo['relacion']) for amigo in usuario_data['amigos']]
        grafo.aristas(user_id, amigos)
    return grafo
