def check_zeros(numberlist):
    count = 0

    for num in numberlist:
        if num == 0:
            count += 1
            if count > 1:
                return False

    return True


array1 = [1, 1, 0, 1]
array2 = [0,4,0,2,5,0]

print(check_zeros(array1))
print(check_zeros(array2))