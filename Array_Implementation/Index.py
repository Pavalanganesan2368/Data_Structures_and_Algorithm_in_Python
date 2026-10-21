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

class Node :
  def __init__ (self, data) :
    self.data = data
    self.next = None
    
class LinkedList :
  def __init__ (self) :
    self.head = None
    
  def insert_beginning (self, data) :
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
  def insert_position (self, index, data) :
    if (index == 0) :
      self.insert_beginning(data)
      return
    
    if (index < 0) :
      return
    
    temp = self.head
    new_node = Node(data)
    
    for _ in range (index - 1) :
      temp = temp.next
      
    new_node.next = temp.next
    temp.next = new_node
    
  def delete_beginning (self) :
    temp = self.head
    if temp is None :
      return
    temp = temp.next.next
    
  def delete_position (self, index) :
    temp = self.head
    
    if (temp is None) or (index >= temp.data)  :
      return
    
    if index < 0 :
      return
    
    for _ in range (index - 1) :
      temp = temp.next
    temp.next = temp.next.next
    
  def display (self) :
    temp = self.head
    
    while temp is not None:
      print(temp.data, end=" => ")
      temp = temp.next
    
    print("Null")
    
linked_list = LinkedList ()

linked_list.insert_beginning(10)
linked_list.insert_beginning(20)
linked_list.insert_beginning(30)

linked_list.insert_position(1, 25)

linked_list.delete_position(2)
linked_list.delete_position(1)
linked_list.delete_position(0)

linked_list.display()