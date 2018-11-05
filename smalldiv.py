n = input("Enter the number")
a = []
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("the smallest one is",a[0])