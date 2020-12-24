class Node: 
      
    def __init__(self, info, size): 
        self.info = info 
        self.next = None
        self.size = size
  
class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    def enQueue(self, element): 
        temp = Node(element) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    def deQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
  
 
