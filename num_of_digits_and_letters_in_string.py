def count_of_num_string(inp):
    count_num= 0
    count_str = 0
    for i in inp:
        if(i.isdigit()):
            count_num+=1
        count_str+=1
    print("count of number in the given number is:", count_num)
    print("count of number in the given string is:", count_str)

if __name__ == "__main__":
    user_input = raw_input("Enter the nubmer or string")
    count_of_num_string(user_input)
