import random

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.sid = random.randint(1000,9999)

    def __str__(self):
        return f"{self.first} {self.last} ID: {self.sid}"

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

        print(f"{current_head.data}  has been moved off the waitlist.")
        return current_head.data

    def size(self):
        return self._size

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self): 
        if self.isEmpty():
            return "Waitlist Status: Empty"

        status_line = "Waitlist Status:  "
        names = [f"{node.data.first} {node.data.last}" for node in self]
        return status_line + " -- ".join(names)

if __name__ == '__main__':
    s1 = Student("Amy", "Mathers")
    s2 = Student("Beth", "Chambers")
    s3 = Student("Carlos", "Ruiz")  

    waitlist = Queue()
    waitlist.add(s1)
    waitlist.add(s2)
    waitlist.add(s3)

    print(waitlist)
    print(f"size is:  {waitlist.size()}")

    waitlist.pop_left()
    print(waitlist)
    print(f"size is:  {waitlist.size()}")

    waitlist.pop_left()
    print(waitlist)

    waitlist.pop_left()
    print(waitlist)
