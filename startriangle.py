from __future__ import print_function
class Startrai():
    def traistar(self,num):
        for i in range (0,num):
            for j in range(0,i+1):
                print("*", end=" ")
            print("\r")
        for i in range(0, num):
            for j in range(0,num-i):
                print("*", end=" ")
            print("\r")
if __name__ == "__main__":
    starcl = Startrai()
    num = int(input("Enter star number"))
    resultstat = starcl.traistar(num)
