class QueueContainer:

    def __init__ (self):
        self.queue = []

    def append(self, element):
        self.element = element
        self.queue.append(self.element)

    def popleft(self):
        if not self.queue:
            print ("queue is empty")
        else:
            self.queue.reverse()
            self.queue.pop()
            self.queue.reverse()

    def showQueue(self):
        print (self.queue)

queue = QueueContainer()
queue.append(203)
queue.showQueue()

queue.append(204)
queue.showQueue()

queue.append(205)
queue.showQueue()

queue.append(206)
queue.showQueue()

queue.popleft()
queue.showQueue()
queue.popleft()
queue.showQueue()
queue.popleft()
queue.showQueue()
queue.popleft()
queue.showQueue()
queue.popleft()
