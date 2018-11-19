if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #print(list(set(arr))[len(list(set(arr)))-2])
    new_arr = list(set(arr))
    new_arr.sort()
    print(new_arr[len(new_arr)-2])