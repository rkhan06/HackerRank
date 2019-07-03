def merge_the_tools(string, k):
    s = [''] * (int(len(string) / k))
    count = 0
    index = 0
    check = [False] * 128
    for i in string:
        if check[ord(i)]:
            count += 1
        else:
            s[index] += i
            count += 1
            check[ord(i)] = True
        if count == k:
            index += 1
            count = 0
            check = [False] * 128
    for i in s:
        print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)