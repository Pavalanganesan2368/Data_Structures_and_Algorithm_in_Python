class Node :
  def __init__ (self, data) :
    self.data = data
    self.next = None
    
class LinkedList :
  def __init__ (self) :
    self.front = None
    self.rear = None
    
  def enqueue (self, data) :
    new_node = Node (data)
    if (self.front == None) :
      self.front = new_node
    else :
      self.rear = new_node
      
    
  def dequeue (self) :
    if self.front == None :
      print("Dequeue is Empty")
      return
    self.front.next = self.front.next.next
    
  def display (self) :
    temp = self.front
    while temp :
      print(temp.data, end=" => ")
      temp = temp.next
    print("Null")
    
linked_list = LinkedList ()
linked_list.enqueue(10)
linked_list.enqueue(20)
linked_list.enqueue(30)

# linked_list.dequeue()
# linked_list.dequeue()
# linked_list.dequeue()

linked_list.display()