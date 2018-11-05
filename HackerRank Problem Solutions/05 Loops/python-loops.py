if __name__ == '__main__':
    n = int(input())
    if (n >= 0 and n <= 20):
        for i in range(n):
            if (i == 0):
                print("0")
            else:
                print(i * i)