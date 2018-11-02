a=float(input("Enter a first number"))
b = float(input("Enter a second number"))
c=float(input("Enter a third number"))
MyList  = []
MyList.append(a)
MyList.append(b)
MyList.append(c)
for i in range(0,3):
    for j  in range(0,3):
        for  k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(MyList[i],MyList[j],MyList[k])