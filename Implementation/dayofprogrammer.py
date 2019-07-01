
# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leapY = 0
    dayslost = 0
    if year < 1918 and year % 4 == 0:
        leapY = 1
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leapY = 1
    if year == 1918:
        dayslost = 13
    day = 256 - (5*31 + 2*30 + 28 + leapY - dayslost)
    return str(day) + ".09." + str(year)


if __name__ == '__main__':


    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')
