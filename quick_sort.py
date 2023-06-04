def quick_sort(array, low, high):
    
    if low < high:
        pivot = partition(array, low, high)
        
        quick_sort(array, low, pivot-1)
        quick_sort(array, pivot+1, high)
    
    return array
   

def partition(array, low, high):
    
    pivot = array[high]
    
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[high] = array[high], array[i+1]
    return i+1
    

items = [10,80,30,90,40,50,70]
print(quick_sort(items,0,len(items)-1))

    