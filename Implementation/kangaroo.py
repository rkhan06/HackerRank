# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v2 >= v1:
        return "NO"
    j = abs(x1 - x2) // abs(v2 - v1)
    if x1 + (v1 * j) == x2 + (v2 * j):
        return "YES"

    return "NO"


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')
