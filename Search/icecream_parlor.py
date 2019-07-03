
# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for i in range(len(arr)):
        diff = m - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == diff:
                return i+1, j+1


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(' '.join(map(str, result)))
        print('\n')

