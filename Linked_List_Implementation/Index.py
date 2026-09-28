import sys 
class Node :
  def __init__ (self, data) :
    self.data = data 
    self.next = None
    
class LinkedList :
  def __init__ (self) :
    self.head = None
    # self.prev = None
    # self.current = None
    # self.next = None
    
  def insert_at_the_beginning (self, data) :
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
  def insert_at_the_position(self, index, data) :
    if index < 0 :
      return
    
    if index == 0 :
      return self.insert_at_the_beginning(data)
    
    new_node = Node(data)
    temp = self.head 
    
    for _ in range (index - 1) :
      if temp == None :
        return
      temp = temp.next
      
    new_node.next = temp.next
    temp.next = new_node
  
  def delete_at_the_beginning (self) :
      temp = self.head
      self.head = temp
  
  def delete_at_the_particular (self, data) :
    if self.head is None:
      return 
    
    if self.head.data == data :
      self.head = self.head.next
      return
    
    temp = self.head
    
    while temp.next is not None :
      if temp.next.data == data :
        temp.next = temp.next.next
        return
      temp = temp.next
      
  def reversed (self) :
    prev = None
    current = self.head
    next = self.head.next
    
    while next is not None :
      next = current.next
      current.next = prev
      prev = current
      current = next
      
    self.head = prev
      
    
  def display (self) :
    temp = self.head
    while temp is not None :
      print(f"{temp.data}", end=" => ")
      temp = temp.next
    print("NULL")

node = LinkedList()
starts = True
while starts :
  print("---Linked List---")

  print("--Choose any option--")
  print("1.Insert at the beginning")
  print("2.Insert at the position")
  print("3.Display the node")
  print("4.Reverse the node")
  print("5.Type Exit")
  userInput = input("").lower()

  match userInput :
    case "1" :
      size = int(input("Enter the Linked List Size : "))
      for i in range (size) :
        inputs = int(input(f"Enter the number {i}: "))
        node.insert_at_the_beginning(inputs)
        
    case "2" :
      data = int(input("Enter the Linked List Data : "))
      index = int(input("Enter the Linked List Index : "))
      node.insert_at_the_position(index, data)
      
    case "3" :
      node.display()
      
    case "4" :
      node.reversed()
      node.display()
      
    case "exit" :
      starts = False
      sys.exit("Linked List is Exited") 