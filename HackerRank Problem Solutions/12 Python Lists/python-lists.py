if __name__ == '__main__':
    N = int(input())
    int_list = []
    for i in range(N):
        statement = input().split()
        command = statement[0]
        numbers = statement[1:]
        if command != "print":
            actual_command = "int_list."+command+"("+",".join(numbers)+")"
            eval(actual_command)
        else:
            print(int_list)