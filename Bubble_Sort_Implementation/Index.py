def bubble_sort (arr) :
  for i in range (0, len(arr) - 1) :
    swapped = False
    for j in range (len(arr) - i - 1) :
      
      if arr[j] > arr[j + 1] :
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
        
    if not swapped :
      break
        
  return arr

arr = [1, 2, 3, 4, 5]
result = bubble_sort (arr)
print(result)