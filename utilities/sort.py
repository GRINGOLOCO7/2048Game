def bubble(list1):
    swapped = True
    while swapped:
        swapped = False
        
        for i in range(len(list1)-1):
            
            if list1[i] < list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                swapped = True

    print(list1)
    return list1
#bubble([1, 5, 3, 2, 4])