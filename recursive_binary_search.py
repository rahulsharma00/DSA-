# In this instead of returning the index position of the element it will return True if the value is
# present and False if the value is absent 

def recursive_binary_search(list,target):
    if len(list)==0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else:
                return recursive_binary_search(list[:midpoint],target)

def verify(result):
    print('target found:',result)

list = [1,2,3,4,5,6,7,8]

result = recursive_binary_search(list,4)
verify(result)


def verify(result):
    print('target found:',result)

result = recursive_binary_search(list,412)
verify(result)
