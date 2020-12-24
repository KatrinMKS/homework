class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def size(self, size):
        self.size = size

    def enQueue(self, element):
        temp = Node(element)
        if self.rear is None:
                self.front = self.rear = temp
                return
        self.rear.next = temp
        self.rear = temp

        def size_num(self, size):
            for i in Queue:
                    size += 1
                    return size

    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if(self.front is None):
            self.rear = None

        def size_clear(self, size):
            size -= 1
            return size
