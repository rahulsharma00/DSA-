def binary_search(list,target):
    first = 0
    last = len(list)-1
    while first<=last:
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1

list = [1,2,3,4,5,6,7]
target = 2

result = binary_search(list,target)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")



