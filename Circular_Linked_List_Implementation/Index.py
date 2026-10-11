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

#class Node :
#  def __init__ (self, data) :
#    self.data = data
#    self.next = None
#    
#class CircularLinkedList :
#  def __init__ (self) :
#    self.last = None
#    
#  def insert_at_the_beginning (self, data) :
#    new_node = Node(data)
#    if self.last == None :
#      new_node.next = new_node
#      self.last = new_node
#    else :
#      new_node.next = self.last.next
#      self.last.next = new_node
#      
#  def insert_at_the_position (self, data, position) :
#    new_node = Node(data)
#    if position == 0 :
#      self.insert_at_the_beginning(data)
#      return
#    
#    temp = self.last
#    if temp == self.last :
#      self.insert_at_the_end(data)
#      return
#    
#    for _ in range (position - 1) :
#      temp = temp.next
#      if temp is not None :
#        print("Array Out of bound ")
#        return
#      temp.next = new_node.next
#      new_node = temp
#  
#  def insert_at_the_end (self, data) :
#    new_node = Node(data)
#    if self.last == None :
#      new_node.next = new_node
#      self.last = new_node
#    else :
#      new_node.next = self.last.next
#      self.last.next = new_node
#      self.last = new_node
#      
#  def delete_at_the_beginning (self) :
#    if (self.last == None) :
#      print("Delete The Linked list is the last")
#      return
#
#    temp = self.last.data
#    if (self.last.next == self.last) :
#      self.last = None
#    else :
#      self.last.next = self.last.next.next
#    
#    return temp
#  
#  def delete_at_the_end  (self) :
#    if self.last == None :
#      print("Delete Linked list is the last")
#      return
#    
#    if (self.last.next == self.last) :
#      self.last = None
#    else :
#      temp = self.last
#      while temp.next is not self.last :
#        temp = temp.next
#      temp.next = self.last.next
#      self.last = temp
#      
#  def delete_at_the_position (self, position) :
#    if self.last == None :
#      print("Delete Linked list is the Not Contained")
#      return
#    
#    if position == 0 :
#      self.delete_at_the_beginning()
#      return
#    
#    temp = self.last
#    
#    if temp == self.last :
#      self.delete_at_the_end()
#      return
#      
#    for _ in range (position - 1) :
#      temp = temp.next
#      if temp == self.last :
#        print("Position is out of range")
#        return
#    temp.next = temp.next.next
#      
#  def display_node (self) :
#    if self.last == None :
#      return
#    temp = self.last.next
#    while temp != self.last :
#      print(f"{temp.data}", end=" <=> ")
#      temp = temp.next
#    print(f"{self.last.data}")
#    
#circular_linked_list = CircularLinkedList()
#
#circular_linked_list.insert_at_the_beginning("Jailer 2")
#circular_linked_list.insert_at_the_beginning("Meiyalagan")
#circular_linked_list.insert_at_the_beginning("Toxic")
#circular_linked_list.insert_at_the_beginning("Jailer 1")
#
#circular_linked_list.insert_at_the_position("Raya", 2)
#circular_linked_list.insert_at_the_position("Marco", 3)
#
#circular_linked_list.display_node()