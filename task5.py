def search(array, number):
    for search, num in enumerate(array):
        if num == number:
            return search
    return "not found"

number = 4
array = (10,20,4,2,12,5)
number1 = 9
print(search(array,number))
print(search(array,number1))



def search(a, number):
    for i in range(len(a)):
        if a[i] == number:
            return i
    return "not found"


arr = [2, 5, 8, 10, 15, 20]
num_to_find = 10
index = search(arr, num_to_find)
print(index)

num_not_found = 25
index_not_found = search(arr, num_not_found)
print(index_not_found)