# bynary search algoritmth

def binary_search (lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return f"{item} isn't in the list"

my_list = [x*2 for x in range(100)]
print(binary_search(my_list, 6))
print(binary_search(my_list, 17))


def binary_search_recursive(lst, low, high, item):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            return binary_search_recursive(lst, low, mid - 1, item)
        else:
            return binary_search_recursive(lst, mid + 1, high, item)
    else:
        return f"{item} isn't in the list"   


# my_list = [x*2 for x in range(100)]
print(binary_search_recursive(my_list, 0, len(my_list)-1, 6))
print(binary_search_recursive(my_list, 0, len(my_list)-1, 17))