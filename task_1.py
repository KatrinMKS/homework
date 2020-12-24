class Node: 
      
    def __init__(self, info): 
        self.info = info 
        self.next = None
  
class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
    
    def size(self, size):
        self.size = size
            
    def sizenum(self, size)
        for i in Queue:
            size++
            return
            
    def sizeclear(self, size)
        for i in Queue:
            size--
            return
            
    def enQueue(self, element): 
        temp = Node(element) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
        self.size = size + 1
  
    def deQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
        self.size = size - 1
  
 
