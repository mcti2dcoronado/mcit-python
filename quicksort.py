
list = [5,3,8,9,6,7,2,3,0,1,4,2]

# Quicksort algorithm
def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = []
        right = []
        for i in range(1,len(array)):
            if array[i] < pivot:
                left.append(array[i])
            else:
                right.append(array[i])
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(list))
