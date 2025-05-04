class BinarySearch():

    def binary_search_iterative(self, list, item):
        # low and high keep track of whichpart of the list you'l search in
        low = 0
        high = len(list) - 1

        # while you haven't narrowed down to one element
        while low <= high:
            # Check the middle element
            mid = (low + high) // 2
            guess = list[mid]
            # Found the item
            if guess == item:
                return mid
            # The guess was too high 
            elif guess > item:
                high = mid - 1
            # The guess was too low
            else:
                low = mid + 1
        # The item does not exist
        return None
    
if __name__ == "__main__":
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]
    print(bs.binary_search_iterative(my_list, 5))
