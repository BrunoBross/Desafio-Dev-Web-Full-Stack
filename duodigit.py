
def SmallDuodigit(digit):
    for num in range(2, 101):
        multiple = int(digit) * num
        if Duodigit(multiple):
            return multiple


def Duodigit(number):
    value = str(number)
    repeated = []
    distinct = 0

    for num in value:
        if num not in repeated:
            distinct += 1
        repeated.append(num)

    if 2 >= distinct:
        return True
    else:
        return False


print(SmallDuodigit(999))
