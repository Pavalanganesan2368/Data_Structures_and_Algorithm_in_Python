def merge_sort (arr) :
  if len(arr) == 1 :
    return arr
  
  mid = int(len(arr) / 2)
   
  left = merge_sort(list(arr[0:mid]))
  right = merge_sort(list(arr[mid:len(arr)]))
  
  return merge(left, right)

def merge_sort_in_place (arr, start, end) :
  if end - start == 1 :
    return arr
  
  mid = int ((end + start) / 2)
   
  merge_sort_in_place(arr, start, mid)
  merge_sort_in_place(arr, mid, end)
  
  return mergeInPlace(arr, start, mid, end)
  
def mergeInPlace (arr, start, mid, end) :  
  joined = [0] * (end - start)
  i = start
  j = mid 
  k = 0
     
  while (i < mid and j < end) :
    if (arr[i] < arr[j]) :
      joined[k] = arr[i]
      k += 1
      i += 1
    else :
      joined[k] = arr[j]
      k += 1
      j += 1
        
    while (i < mid) :
      joined[k] = arr[i]
      k += 1
      i += 1
      
    while (j < end) :
      joined[k] = arr[j]
      k += 1
      j += 1
      
    for r in range (0, k) :
      arr[start+r] = joined[r]
  
def merge (first, second) :
  joined = [0] * (len(first) + len(second))
  i = j = k = 0
   
  while (i < len(first) and j < len(second)) :
    if (first[i] < second[j]) :
      joined[k] = first[i]
      k += 1
      i += 1
    else :
      joined[k] = second[j]
      k += 1
      j += 1
      
  while (i < len(first)) :
    joined[k] = first[i]
    k += 1
    i += 1
    
  while (j < len(second)) :
    joined[k] = second[j]
    k += 1
    j += 1
    
  return joined

arr = [5, 4, 7, 1, 2, 8, 6, 9]
print(merge_sort_in_place(arr, 3, 7))