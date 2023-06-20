import random

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.adjacent = {}
        self.vizinhos = []
        self.vizinhos_pesos = []

    def add_borda(self, vertice, peso):
        self.adjacent[vertice] = peso

    def incrementar_borda(self, vertice):
        self.adjacent[vertice] = self.adjacent.get(vertice, 0) + 1

    def get_probabilidade(self):
        for (vertice, peso) in self.adjacent.items():
            self.vizinhos.append(vertice)
            self.vizinhos_pesos.append(peso)

    def next_palavra(self):
        return random.choices(self.vizinhos, weights=self.vizinhos_pesos)[0]


class Grafo:
    def __init__(self):
        self.vertices = {}

    def get_vertice_valor(self):
        return set(self.vertices.keys())

    def add_vertice(self, valor):
        self.vertices[valor] = Vertice(valor)

    def get_vertice(self, valor):
        if valor not in self.vertices:
            self.add_vertice(valor)
        return self.vertices[valor]

    def get_next_palavra(self, current_vertice):
        return self.vertices[current_vertice.valor].next_palavra()

    def generate_probabilidade(self):
        for vertice in self.vertices.values():
            vertice.get_probabilidade()
