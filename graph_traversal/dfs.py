from dataclasses import dataclass, field
from typing import Self

time = 0

@dataclass
class Vertex:
	name: str
	neighbors: list[Self] = field(default_factory=list) # default = []
	color: str = 'white'
	discovery_time: int = 0
	discoverer: Self | None = None
	finish_time: float = float('inf')

	def __str__(self):
		return self.name

	def __repr__(self) -> str:
		return self.__str__()

def visit_vertex(vertex: Vertex) -> None:
	global time

	time += 1
	vertex.discovery_time = time
	vertex.color = "gray"
	for neighbor in sorted(vertex.neighbors, key=lambda x: x.name):
		if neighbor.color == "white":
			neighbor.discoverer = vertex
			visit_vertex(neighbor)

	vertex.color = "black"
	time += 1
	vertex.finish_time = time


def depth_first_search(graph: list[Vertex]) -> None:
	global time

	for vertex in graph:
		vertex.color = "white"
		vertex.discoverer = None
	time = 0
	for vertex in graph:
		if vertex.color == "white":
			visit_vertex(vertex)


def get_edges(graph: list[Vertex]) -> tuple[list[tuple[str, str]], list[tuple[str, str]], list[tuple[str, str]], list[tuple[str, str]]]:
	global time

	tree_edges = []
	back_edges = []
	forward_edges = []
	cross_edges = []

	for vertex in graph:
		for neighbor in sorted(vertex.neighbors, key=lambda x: x.name):
			if neighbor.discoverer == vertex:  # Note that tree edges are the edges that are explored by the parent
				tree_edges.append((vertex.name, neighbor.name))

			# elif are needed to avoid double counting since we no longer have the time variable to help us
			elif neighbor.discovery_time <= vertex.discovery_time < vertex.finish_time <= neighbor.finish_time:
				back_edges.append((vertex.name, neighbor.name))

			elif vertex.discovery_time < neighbor.discovery_time < neighbor.finish_time < vertex.finish_time:
				forward_edges.append((vertex.name, neighbor.name))

			elif neighbor.discovery_time < neighbor.finish_time < vertex.discovery_time < vertex.finish_time:
				cross_edges.append((vertex.name, neighbor.name))

			else:
				print(f"Error on edge: ('{vertex.name}',  '{neighbor}')")

	return tree_edges, back_edges, forward_edges, cross_edges


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

	a.neighbors = [d, g]
	b.neighbors = [c]
	c.neighbors = [b, f]
	d.neighbors = [e, g]
	e.neighbors = [a, d]
	f.neighbors = [b, g]
	g.neighbors = [b, h, i]
	h.neighbors = [d, f, g]
	i.neighbors = [a, b]

	graph = [a, b, c, d, e, f, g, h, i]

	depth_first_search(graph)

	tree_edges, back_edges, forward_edges, cross_edges = get_edges(graph)

	print(f"Tree Edges ({len(tree_edges)}): {tree_edges}")
	print(f"Back Edges ({len(back_edges)}): {back_edges}")
	print(f"Forward Edges ({len(forward_edges)}): {forward_edges}")
	print(f"Cross Edges ({len(cross_edges)}): {cross_edges}")

	print()

	print('Vertices by discovery time:')
	for vertex in sorted(graph, key=lambda vertex: vertex.discovery_time):
		print(vertex.name, vertex.discovery_time, vertex.finish_time)

	print()

	print('Vertices by finish time:')
	for vertex in sorted(graph, key=lambda vertex: vertex.finish_time):
		print(vertex.name, vertex.discovery_time, vertex.finish_time)