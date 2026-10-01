class Queue :
  def __init__ (self, capacity) :
    self.capacity = [0] * capacity
    self.rear = -1
  
  def enqueue (self, data) :
    try :
      self.rear += 1
      self.capacity[self.rear] = data  
    except :
      return IndexError ("Enqueue is Full")
    
  def dequeue (self) :
    try :
      if self.rear == -1 :
        print("Dequeue is Empty")
        return
      
      temp = self.capacity[0]
      for i in range (1, self.rear) :
        self.capacity[i - 1] = self.capacity[i]
        
      self.rear -= 1
      return temp
    except :
        return IndexError("Dequeue is Empty")
      
  
  def display (self) :
    for i in range (0, self.rear + 1) :
      print(self.capacity[i], end=" ")
    print("")
    
queue = Queue(3)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
