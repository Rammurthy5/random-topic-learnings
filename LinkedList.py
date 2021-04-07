class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head=None
        self.counter=0
        self.tail=None


    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        if self.head is None:
            return "[]"
        nodes = [str(node.data) for node in self]
        return f"[{', '.join(nodes)}]"

    def insert(self, data):
        node = Node(data)
        self.counter+=1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
