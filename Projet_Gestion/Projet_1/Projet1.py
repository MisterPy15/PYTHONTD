
class FIFOQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "La file d'attente est vide"
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


# Exemple d'utilisation de la file FIFO
fifo = FIFOQueue()

fifo.enqueue(int(input("Entrez la valeur : ")))
fifo.enqueue("B")
fifo.enqueue("C")

print(fifo.dequeue())  # Sortie: "A"
print(fifo.dequeue())  # Sortie: "B"

fifo.enqueue("D")

print(fifo.dequeue())  # Sortie: "C"
print(fifo.dequeue())  # Sortie: "D"
print(fifo.dequeue())  # Sortie: "La file d'attente est vide"


