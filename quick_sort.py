# Quicksort
# O - notation depends on pivot (start) element
# but on average O(n log n)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    

print(quicksort([1,5,3,345,7,77,23,99,99,245,2,5,9]))