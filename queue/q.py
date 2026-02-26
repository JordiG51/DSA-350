class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self._size = 0  

    def isEmpty(self): 
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def pop_left(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = self.head.next
        self._size -= 1
        return current_head.data

    def size(self): 
        return self._size

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self): 
        return_str = "Queue object: "
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return return_str + " -> ".join(nodes)
