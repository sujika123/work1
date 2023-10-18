def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array = [10, 5, 8,22,35,11,40, 1, 4]

bubble_sort(array)
print("sortedlist :",array)

print("__________________")

def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                # here we are not using temp variable
                list1[j],list1[j+1] = list1[j+1], list1[j]
    return list1

list1 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list1)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list1))
