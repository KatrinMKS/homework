class Node: 
      
    def __init__(self, info): 
        self.info = info 
        self.next = None
  
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
  
 
if __name__== '__main__': 
    q = Queue() 
    q.EnQueue(15) 
    q.EnQueue(23) 
    q.DeQueue() 
    q.DeQueue() 
    q.EnQueue(38) 
    q.EnQueue(42) 
    q.EnQueue(56)  
    q.DeQueue()    
    print("Queue Front: " + str(q.front.info)) 
    print("Queue End: " + str(q.rear.info)) 
