'''
n=int(input("Enter the number of elements to be inserted"))
Mylist = []
for i in range(0,n):
    ele = int(input("Enter the number"))
    Mylist.append(ele)
avgnum = sum(Mylist)/n
print("average of the numbers is ",round(avgnum,2))
'''

class Avg_num():
    def findavg(self,num):
        list_num=[]
        for i in range(0,num):
            numele = input("enter the number")
            list_num.append(numele)
        avg = sum(list_num)/num
        return avg

if __name__ == '__main__':
    numavf= Avg_num();
    entnum = int(input("Enter the number"))
    resultavg = numavf.findavg(entnum)
    print(resultavg)
