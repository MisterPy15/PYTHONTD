class LIFOStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "La pile est vide"
        return self.stack.pop()

    def size(self):
        return len(self.stack)


# Exemple d'utilisation de la pile LIFO
lifo = LIFOStack()

lifo.push("A")
lifo.push("B")
lifo.push("C")

print(lifo.pop())  # Sortie: "C"
print(lifo.pop())  # Sortie: "B"

lifo.push("D")

print(lifo.pop())  # Sortie: "D"
print(lifo.pop())  # Sortie: "A"
print(lifo.pop())  # Sortie: "La pile est vide"


