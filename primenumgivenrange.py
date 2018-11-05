a = []
for num in range(2,101):
    if all(num%i!=0 for i in range(2,num)):
        a.append(num)
print a