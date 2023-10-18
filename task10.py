string="welcome"
p=""
for char in string:
    if char not in p:
        p=p+char
print(p)
# k=list("welcome")

def removeDuplicate(a):
    unique_chars = []

    for char in a:
        if char not in unique_chars:
            unique_chars.append(char)

    return ''.join(unique_chars)


a = "calculator"
result = removeDuplicate(a)
print(result)