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
