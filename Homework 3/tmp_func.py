def task(array):
    if len(array) == 0:
        return array
    
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > current: 
            array[j + 1] = array[j]
            j -= 1
            
        array[j + 1] = current
        
    return array
