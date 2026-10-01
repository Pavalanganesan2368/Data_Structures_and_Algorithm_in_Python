class Queue :
  def __init__ (self, capacity) :
    self.capacity = [0] * capacity
    self.front = -1
    self.rear = -1
  
  def enqueue (self, data) :
    try :
      if self.rear == len(self.capacity) - 1 :
        print("Enqueue is Full")
        return

      if self.front == -1 : 
        self.front += 1

      self.rear += 1
      self.capacity[self.rear] = data  
    except :
      return IndexError ("Enqueue is Full")
    
  def dequeue (self) :
    try :
      if (self.front == -1 or self.front > self.rear) :
        print("Dequeue is Empty")
        return
      self.front += 1
      return self.capacity[self.front]
    except :
        return IndexError("Dequeue is Empty")
      
  
  def display (self) :
    for i in range (0, self.rear) :
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
