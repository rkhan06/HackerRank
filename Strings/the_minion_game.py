
def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    k = 0
    s = 0
    l = len(string)
    for i in range(l):
        if string[i] in vowels:
            k += l - i
        else:
            s += l - i
    if k > s:
        return print("Kevin" + " " + str(k))
    if s > k:
        return print("Stuart" + " " + str(s))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)