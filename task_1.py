class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def size(self):
        return self.size

    def size_plus(self):
        self.size += 1

    def size_del(self):
        self.size -= 1

    def enQueue(self, element):
        temp = Node(element)
        self.size_plus()
        if self.rear is None:
                self.front = self.rear = temp
                return
        self.rear.next = temp
        self.rear = temp

    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if(self.front is None):
            self.rear = None
        self.size_del()

    def isEmpty(self):
        return self.front is None

    def queue_clean(self):
        while not self.isEmpty():
            self.deQueue()

