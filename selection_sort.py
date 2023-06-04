def selection_sort(array):
    
    n = len(array)
    
    for i in range(n):
        
        min_idx = i
        
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array
        


print(selection_sort([64, 25, 12, 22, 11]))
        