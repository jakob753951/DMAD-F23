from dataclasses import dataclass, field

@dataclass
class Vertex:
	name: str = field(hash=True)
	neighbors: set['Vertex'] = field(default_factory=set) # default = []

	def __str__(self):
		return self.name

	def __repr__(self) -> str:
		return self.__str__()

	def __eq__(self, o: object) -> bool:
		return isinstance(o, Vertex) and self.name == o.name

	def __hash__(self) -> int:
		return hash(self.name)

def get_all_connected_vertices(vertex: Vertex, connected_vertices: set | None = None) -> set[Vertex]:
	if connected_vertices is None:
		connected_vertices = set()
	connected_vertices.add(vertex)
	for neighbor in vertex.neighbors:
		if neighbor not in connected_vertices:
			connected_vertices |= get_all_connected_vertices(neighbor, connected_vertices)
	return connected_vertices

# get all vertices reachable from vertex
def get_connections(graph: set[Vertex]) -> dict[Vertex, set[Vertex]]:
	connections = {}
	for vertex in graph:
		connections[vertex] = get_all_connected_vertices(vertex)
	return connections

# get all strongly connected components in graph
def get_strongly_connected_components(graph: set[Vertex]) -> list[set[Vertex]]:
	connections = get_connections(graph)

	components = []
	for vertex in graph:
		component = {vertex}
		for other_vertex in graph:
			if vertex is other_vertex:
				continue

			if vertex in connections[other_vertex] and other_vertex in connections[vertex]:
				component.add(other_vertex)
		components.append(component)
	# remove duplicates
	components = [component for i, component in enumerate(components) if component not in components[:i]]
	return components

if (__name__ == "__main__"):
	a = Vertex('a')
	b = Vertex('b')
	c = Vertex('c')
	d = Vertex('d')
	e = Vertex('e')
	f = Vertex('f')
	g = Vertex('g')
	h = Vertex('h')
	i = Vertex('i')

	a.neighbors = {e, d, g}
	b.neighbors = {c}
	c.neighbors = {b}
	d.neighbors = {e}
	e.neighbors = set()
	f.neighbors = {c, b, g}
	g.neighbors = {d, h, i, b}
	h.neighbors = {d, f, g}
	i.neighbors = {a, b}

	graph = {a, b, c, d, e, f, g, h, i}

	components = get_strongly_connected_components(graph)

	print('strongly connected components:')
	for component in components:
		print(component)
