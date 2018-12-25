def insertion_sort(arr, n):
    for i in range(1, n):
        cur = arr[i]
        insert = False
        for j in range(i-1, -1, -1):
            if cur < arr[j]:
                arr[j+1] = arr[j]
            else:
                insert = True
                arr[j+1] = cur
                break
        if not insert:
            arr[0] = cur


while True:
    try:
        # f = open('input.txt')
        # arr = [int(i) for i in f.readline().split()]

        arr = [int(i) for i in input().strip().split()]
        n = arr[0]
        arr = arr[1:]
        insertion_sort(arr, n)

        print(arr[0], end='')
        for i in range(1, n):
            print('', arr[i], end='')
        print()
    except EOFError:
        break
