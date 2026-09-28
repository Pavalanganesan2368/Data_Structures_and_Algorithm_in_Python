# class Array :
#   def __init__ (self, capacity) :
#     self.capacity = capacity
#     self.size = 0
#     self.data = [0] * self.capacity
  
#   def get (self, index) :
#     return self.capacity[index]
  
#   def set (self, index, element) :
#     self.data[index] = element
  
#   def insert (self, index, element) :
#     if (element < 0 or self.size >= self.capacity or index > self.size) :
#       print(f"Can't Insert {element} element.")
#       return
#     for i in range (self.size, index, -1) :
#       self.data[i] = self.data[i - 1]
#     self.data[index] = element
#     self.size += 1
    
#   def delete (self, index) :
#     if (index < 0) :
#       print(f"Can't Delete the Element.")
#       return 
    
#     for i in range (index, self.size - 1) :
#       self.data[i] = self.data[i + 1]
#     self.data[self.size - 1] = 0
#     self.size -= 1
          
#   def display (self) :
#     for i in range (self.size) :
#       print(self.data[i], end=" ")
#     print(" ")
    
# arrays = Array(5)
# arrays.insert(0, 1)
# arrays.insert(1, 2)
# arrays.insert(2, 3)
# arrays.insert(3, 4)
# arrays.insert(4, 5)

# arrays.display()

# arrays.delete(3)
# arrays.delete(2)
# arrays.delete(1)

# arrays.set(0, 10)
# arrays.set(3, 20)

# arrays.display()

def fibonacci (num) :
  fib = [0, 1]
  if (num == 0) :
    return 0
  elif (num == 1) :
    return 1
  else :
    for i in range (2, num) :
      nums = fib[i - 1] + fib[i - 2]
      fib.append(nums)
      
  return fib

print(fibonacci (10))