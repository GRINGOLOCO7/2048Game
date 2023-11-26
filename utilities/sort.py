def QuickSort(arr):
    if not arr or len(arr) < 2:
        return arr   # arr in the base case is a part of the array that is sorted

    pivot_index = (len(arr)//2) - 1
    pivot = arr[pivot_index]

    # create left_arr & right_arr
    left_arr = [element for element in arr[:pivot_index] + arr[pivot_index + 1:] if element < pivot]   # list comprention
    right_arr = [element for element in arr[:pivot_index] + arr[pivot_index + 1:] if element >= pivot]

    return QuickSort(right_arr) + [pivot] + QuickSort(left_arr)

#print(QuickSort([2,8,6,4,3,6,8,5,7,4,3,2,79,9]))



# time complexity: O(n * log(n))
    # every time divide and conquer => O(log(n))
    # but every subset u compare each element => O(n)
# worst case: if array is already sorted and you pick as pivot the mid element => O(n*log(n))







def bubble(list1):
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(list1)-1):

            if list1[i] < list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                swapped = True

    #print(list1)
    return list1
#bubble([1, 5, 3, 2, 4])