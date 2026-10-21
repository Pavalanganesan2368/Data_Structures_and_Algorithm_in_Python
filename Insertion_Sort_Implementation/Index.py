# def insertion_sort (arr) :
  
#   for i in range (1, len(arr) - 1) :
#     for j in range (i, 0, -1) :
#       if (arr[j - 1] > arr[j]) :
#         arr[j - 1], arr[j] = arr[j], arr[j - 1]
        
#   return arr

# arr = [5, 1, 3, 2, 4]
# result = insertion_sort(arr)

# print(f"Insertion Sort: {result}")

class Node :
  def __init__ (self, data) :
    self.data = data
    self.next = None
    
class LinkedList :
  def __init__  (self) :
    self.head = None
    
  def insert_beginning (self, data) :
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
  def display (self) :
    temp = self.head
    while temp :
      print(temp.data, end=" => ")
      temp = temp.next
    print("NULL")
    
linked_list = LinkedList ()

linked_list.insert_beginning(10)
linked_list.insert_beginning(20)
linked_list.insert_beginning(30)

linked_list.display()