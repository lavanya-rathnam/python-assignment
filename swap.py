class Swap():
    def swapthenumbers(self,first,second):
        first = first+second
        second = first-second
        first = first-second
        return(first,second)
if __name__ == "__main__":
    swapob = Swap()
    a = input("Enter a first number")
    b = input("Enter a second number")
    result= swapob.swapthenumbers(a,b)
    print(result)

