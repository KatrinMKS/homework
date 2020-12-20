import collections

class QueueContainer:

    def __init__ (self):
        self.queue = collections.deque()

    def my_append(self, element):
        self.element = element
        self.queue.append(self.element)

    def my_popleft(self):
        if not self.queue:
            print ("queue is empty")
        else:
            print(self.queue.popleft())

queue = QueueContainer()
#queue.my_append(10)
#queue.my_append(20)
#queue.my_append(30)
#queue.my_append("hello")
#queue.my_append("world")
#print(queue.queue)
#queue.my_popleft()
#queue.my_popleft()
#queue.my_popleft()
#queue.my_popleft()
#queue.my_popleft()
#queue.my_popleft()
