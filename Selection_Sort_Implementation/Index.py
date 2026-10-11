def selection_sort (arr) :
  for i in range (0, len(arr) - 1) :
    for j in range (0, len(arr) - 1) :
      if (arr[j] >= arr[j + 1]) :
        arr[j + 1], arr[j] = arr[j], arr[j + 1]
  
  return arr

def selection_sort (arr) :
  for i in range (0, len(arr) - 1) :
    mininum = arr[i]
    min_index = i
    
    for j in range (i, len(arr) - 1) :
      if (arr[j] < mininum) :
        mininum = arr[j]
        min_index = j
        
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp
    
  print(arr)
    

arr = [5, 2, 9, 1, 7, 10, 6, 3, 8, 4, 5]
selection_sort(arr)