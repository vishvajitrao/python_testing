x = "a1rb2c3"
output = "arbbccc"
x1 = []

for i in x:
    if i.isalpha():
        x1.append(i)
    else:
        val = x1.pop(len(x1) - 1)
        x1.append(val * int(i))

print(''.join(x1))




