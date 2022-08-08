def linear_search(lst,target):
    for i in range(0,len(lst)):
        if lst[i] == target:
            return i    
            # we need to terminate the statement from the for loop or else it won't exist 
    return -1
    
lst = [1,3,5,6,14,7]
target = 3

result = linear_search(lst,target)
if result != -1:
    print('Element found at index',str(result))
else:
    print('Element not found')
    


 