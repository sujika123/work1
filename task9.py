def checkWrongOrWrite(a):
    vowels = 'aeiou'
    vowel_count = 0

    for char in a.lower():
        if char in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                print("False")
                break
    else:
        print("True")

a = "sdagdibo"
checkWrongOrWrite(a)
a = "Hello"
checkWrongOrWrite(a)