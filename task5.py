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