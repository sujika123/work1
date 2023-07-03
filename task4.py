def checkunique(word):
    a = len(word)
    b =len(set(word))
    if a == b:
        return True

    return False

word = "mobile"
word1 = "calculator"
print(checkunique(word))
print(checkunique(word1))