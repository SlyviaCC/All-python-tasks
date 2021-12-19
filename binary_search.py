def binary_search(data_list, target):
    low = 0  
    high = len(data_list) - 1  
    index = 1 
 
    while low <= high:
        mid = (low + high) // 2 
 
        if data_list[mid] == target:
            return "find %d times,This number is undermark in the list :%d" % (index, mid)
        elif data_list[mid] > target:
            high = mid - 1  
        else:
            low = mid + 1  
 
        index += 1
    return "find %d times, not find!" % index
 
 
