def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    copiedArray = list(arr)
    for i in range(len(copiedArray)):
        smallest = findSmallest(copiedArray)
        newArr.append(copiedArray.pop(smallest))
    return newArr
    
if __name__ == "__main__":
    print(selection_sort([3, 2, 6, 4, 9]))


