
from collections import Counter
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    c = Counter(arr)
    mx = max([c.get(i) for i in c])
    return min([key for key in c if c[key] == mx])


if __name__ == '__main__':


    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')

