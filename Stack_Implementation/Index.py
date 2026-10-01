class Array :
  def __init__ (self, capacity) :
    self.stack = [0] * capacity
    self.top = -1
    
  def push (self, data) :
    self.top += 1
    if (self.top == len(self.stack) - 1) :
      print("Stack is Overflow")
      return
    self.stack[self.top] = data
    
  def pop (self) :
    self.top -= 1
    if self.top == -1 :
      print("Stack is Empty")
      return
    return self.stack[self.top]
    
  def peek (self) :
    return self.stack[self.top]
  
  def display (self) :
    for i in range (self.top + 1) :
      print(f"{self.stack[i]}", end=" ")
    print()
    
  def isEmpty (self) :
    if self.top == -1 :
      return True
    return False
    
stackStarts = True
while stackStarts :
  array = Array(10)
  array.push(10)
  array.push(20)
  array.push(30)
  array.push(40)
  array.display()