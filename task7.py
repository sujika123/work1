def find_mismatch(a,b):
    new = []

    for number in a:
        if number not in b:
            new.append(number)

    print("Numbers present in array a but not in b:", new)

a =[1,2,4,32,12,6,8]
b = [2,6,10,12,14,17]
find_mismatch(a,b)

print("_______________________")
# Method 2

def search_number(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Example Usage
a = [5, 8, 3, 2, 9, 7, 1, 6, 4]
target_number = 7

result = search_number(a, target_number)

if result != -1:
    print(f"The number {target_number} was found at index {result}.")
else:
    print(f"The number {target_number} was not found in the array.")
