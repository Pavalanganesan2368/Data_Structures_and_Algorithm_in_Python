class Node :
  def __init__ (self, data) :
    self.data = data
    self.next = None
    
class CircularLinkedList :
  def __init__ (self) :
    self.tail = None
    
  def insert_beginning (self, data) :
    new_node = Node(data) 
    if (self.tail is None) :
      new_node.next = new_node
      self.tail = new_node
    else :
      new_node.next = self.tail.next
      self.tail.next = new_node
      
  def insert_end (self, data) :
    new_node = Node(data) 
    if (self.tail is None) :
      new_node.next = new_node
      self.tail = new_node
    else :
      new_node.next = self.tail.next
      self.tail.next = new_node
      self.tail = new_node
      
  def delete_beginning (self) :
    if self.tail is None :
      print("Can't Delete the Beginning")
      return
    
    if self.tail.next == self.tail :
      self.tail = None
    else :
      self.tail.next = self.tail.next.next
      
  def delete_end (self) :
    if self.tail is None :
      print("Can't Delete the Beginning")
          return
        
    if self.tail.next == self.tail :
      self.tail = None
      
  def display_node (self) :
    temp = self.tail.next
    if temp is None :
      print("List is Empty")
      return
    
    while True :
      print(temp.data, end=" => ")
      temp = temp.next
      
      if temp == self.tail.next :
        break
    print("Null")
    
circular_linked_list = CircularLinkedList()

circular_linked_list.insert_beginning(10)
circular_linked_list.insert_beginning(20)
circular_linked_list.insert_beginning(30)

circular_linked_list.insert_end(40)
circular_linked_list.delete_beginning()

circular_linked_list.display_node()