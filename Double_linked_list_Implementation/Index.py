class Node :
  def __init__ (self, data) :
    self.prev = None
    self.data = data
    self.next = None
    
class DoubleLinkedList :
  def __init__ (self) :
    self.head = None
  
  def insert_beginning (self, data) :
    new_node = Node(data)
    new_node.next = self.head
    if self.head is not None :
      self.head.prev = new_node
    self.head = new_node
    
  def insert_end (self, data) :
    end_node = Node(data)
    temp = self.head
    
    if temp.next is None :
      self.insert_beginning(data)
    
    while temp.next is not None :
      temp = temp.next
      
    temp.next = end_node
    end_node.prev = temp
    
  def insert_at_the_index (self, index, data) :
    index_node = Node(data)
    temp = self.head
    
    if (index == 0) :
      self.insert_beginning(data)
    
    if (index < 0) :
      return
    
    for _ in range (index - 1) :
      temp = temp.next
      
    index_node.next = temp.next
    temp.next = index_node 
    index_node.prev = temp
    temp.next = index_node
    
  def delete_node (self, index) :
    temp = self.head
    
    if index < 0 :
      return
    
    for _ in range (index) :
      temp = temp.next
      
    if temp.prev :
      temp.prev.next = temp.next
    else :
      self.head = temp.next
    if temp.next :
      temp.next.prev = temp.prev
  
  def search_node (self, data) :
    temp = self.head
    counter = 0
    
    if temp is None :
      return
    
    while temp.next is not None :
      if (temp.data == data) :
        print(f"Data: {data}\nIndex: {counter}")
      temp = temp.next  
      counter += 1
    
    return -1
    
  def display_node (self) :
    temp = self.head
    
    while temp is not None :
      print(f"{temp.data}", end=" => ")
      temp = temp.next
    print("Null")
    
  def display_node_reverse (self) :
    current = self.head
    
    while current is not None :
      current.prev, current.next  = current.next, current.prev
      current = current.prev
    if self.head is not None :
      self.head = self.head.prev
      
  def reversed_display (self) :
    if self.head is None :
      return
    temp = self.head
    # prev = temp.prev
    
    while temp.next is not None :
      temp = temp.next
      
    while temp is not None :
      print(f"{temp.data}", end=" => ")
      temp = temp.prev
    print("NULL")
      
    
double_linked_list = DoubleLinkedList()

double_linked_list.insert_beginning(10)
double_linked_list.insert_beginning(20)
double_linked_list.insert_beginning(30)

double_linked_list.insert_at_the_index(2, 80)
double_linked_list.insert_at_the_index(0, 20)
double_linked_list.insert_at_the_index(3, 70)

# double_linked_list.delete_node(1)
# double_linked_list.delete_node(2)
# double_linked_list.delete_node(3)

# double_linked_list.insert_end(50)
# double_linked_list.insert_end(60)

# double_linked_list.search_node(80)
double_linked_list.display_node()
  
double_linked_list.reversed_display()  
# double_linked_list.reversed_display()       