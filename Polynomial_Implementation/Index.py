class Node :
  def __init__ (self, coef, expo) :
    self.coef = coef
    self.expo = expo
    self.next = None

class Polynomial : 
  def __init__ (self) :
    self.head = None
    
  def insert_last (self, coef, expo) :
    new_node = Node (coef, expo)
    if (not self.head) :
      self.head = new_node
      return
    
    temp = self.head
    while temp.next :
      temp = temp.next
    temp.next = new_node
         
  def display (self) :
    temp = self.head
    
    while temp :
      print(f"{temp.coef}x^{temp.expo} + ", end="")
      temp = temp.next
    print("NULL")
    
def add_polynomial (polynomial1, polynomial2) :
    result = Polynomial()
    while polynomial1 and polynomial2 :
      if polynomial1.expo == polynomial2.expo :
        result.insert_last(polynomial1.coef + polynomial2.coef, polynomial1.expo)
        polynomial1 = polynomial1.next
        polynomial2 = polynomial2.next
        
      elif polynomial1.expo > polynomial2.expo : 
        result.insert_last(polynomial1.coef, polynomial1.expo)
        polynomial1 = polynomial1.next
      
      else : 
        result.insert_last(polynomial2.coef, polynomial2.expo)
        polynomial2 = polynomial2.next
        
    while polynomial1 :
      result.insert_last (polynomial1.coef, polynomial1.expo)
      polynomial1 = polynomial1.next
      
    while polynomial2 :
      result.insert_last (polynomial2.coef, polynomial2.expo)
      polynomial2 = polynomial2.next
      
    return result
    
if "__main__" == __name__ :
  polynomial1 = Polynomial()
  polynomial1.insert_last(3, 2)
  polynomial1.insert_last(4, 1)
  polynomial1.insert_last(1, 0)

  polynomial2 = Polynomial()
  polynomial2.insert_last(4, 2)
  polynomial2.insert_last(4, 0)
  
  result = add_polynomial (polynomial1.head, polynomial2.head)

  polynomial1.display()
  polynomial2.display()
  
  result.display()