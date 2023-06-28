from dataclasses import dataclass, field
from typing import Self

@dataclass
class Vertex:
	name: str
	neighbors: list[Self | None] = field(default_factory=list) # default = []

	def __str__(self):
		return self.name

	def __repr__(self) -> str:
		return self.__str__()


def is_topological_sorting(vertices: list[Vertex]) -> bool:
	for i in range(1, len(vertices)):
		vertex = vertices[i]
		for neighbor in vertex.neighbors:
			if neighbor in vertices[:i]:
				return False
	return True

if (__name__ == "__main__"):
	a = Vertex('a')
	b = Vertex('b')
	c = Vertex('c')
	d = Vertex('d')
	e = Vertex('e')
	f = Vertex('f')

	a.neighbors = []
	b.neighbors = [a, c, d, e]
	c.neighbors = [e]
	d.neighbors = [a, e]
	e.neighbors = []
	f.neighbors = [c, e]

	sortings = [
		[a, b, c, d, e, f],
		[b, d, f, c, e, a],
		[f, e, d, c, b, a],
		[b, f, e, d, c, a],
		[f, b, c, d, a, e]
	]

	for sorting in sortings:
		print(f'is_topological_sorting({sorting}) = {is_topological_sorting(sorting)}')