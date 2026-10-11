def linear_search (arr, target) :
  for i in range (len(arr)) :
    if arr[i] == target :
      return i
  return -1

def binary_search (arr, target) :
  arr.sort()
  
  start = 0
  end= len(arr) - 1
  
  while start <= end :
    mid = int((start + end) / 2)
    
    if (arr[mid] > target) :
      start = mid + 1
    elif (arr[mid] < target) :
      end = mid - 1
    else :
      return mid
  
  return -1
      
def agostic_binary_search (arr, target) :
  # arr.sort()
  start = 0
  end = len(arr) - 1
  
  ascending = False
  
  if (arr[start] < arr[end]) :
    ascending = True
  
  while (start <= end) :
    mid = int((start + end) / 2)
    
    if ascending :
      if (arr[mid] > target) :
        start = mid + 1
      elif (arr[mid] < target) :
        end = mid - 1
      else :
        return mid
    else : 
      if (arr[mid] > target) :
        start = start - 1
      elif (arr[mid] < target) :
        end = end + 1
      else :
        return mid
    
  return -1

#Question - 1    

def first_occurance (arr, target) :
  start = 0
  end = len(arr) - 1
  
  while start <= end :
    mid = int((start + end) / 2)
    
    if arr[mid] <= target :
      start = mid + 1
    elif arr[mid] >= target :
      end = mid - 1
    else :
      return mid
  
  return -1

arr = [0, 1, 1, 1, 3, 4, 6, 8]
target = 1
result = first_occurance (arr, target)
print(result)