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

        # Python Program - Pattern Program 3

        k = 8
        for i in range(0, 5):
            for j in range(0, k):
                print(end=" ")
            k = k - 2
            for j in range(0, i + 1):
                print("* ", end="")
            print()

        # Python Program - Pattern Program 3
        n = 1
        for i in range(0, 5):
            for j in range(0, i + 1):
                print(n, end=" ")
                n = n + 1
            print()
        # Python Program - Pattern Program 3

        n = 1
        for i in range(0, 5):
            for j in range(0, 5-i):
                print(n, end=" ")
                n = n + 1
            print()
if __name__ == "__main__":
    starcl = Startrai()
    num = int(input("Enter star number"))
    resultstat = starcl.traistar(num)
