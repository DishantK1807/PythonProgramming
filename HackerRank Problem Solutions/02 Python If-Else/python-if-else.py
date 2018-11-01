if __name__ == "__main__":
    N = int(input())
    if (N <= 100 and N >= 1):
        if N % 2 != 0:
            print("Weird")
        elif N >= 2 and N <= 5:
            print("Not Weird")
        elif N >= 6 and N <=20:
            print("Weird")
        else:
            print("Not Weird")