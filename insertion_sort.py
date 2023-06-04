def insertion_sort(array):
    
    n = len(array)
    
    for i in range(1, n):
        
        j = i
        
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array   
    
    

print(insertion_sort([12, 11, 13, 5, 6]))
# [12, 11, 13, 5, 6]
# [11, 12, 13, 5, 6]