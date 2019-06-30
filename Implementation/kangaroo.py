# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    for i in range(x2 - x1 + 1):
        if x1 == x2:
            return "YES"
        x1 += v1
        x2 += v2
    return "NO"


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')
