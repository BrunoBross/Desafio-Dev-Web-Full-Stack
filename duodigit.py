
def Duodigito(number):
    value = str(number)
    repeated = []
    distinct = 0

    for num in value:
        if num not in repeated:
            distinct += 1
        repeated.append(num)

    if 2 >= distinct:
        return f'{value} é duodigito'
    else:
        return f'{value} não é duodigito'


print(Duodigito(101))
print(Duodigito(322))
print(Duodigito(888))
print(Duodigito(123))
print(Duodigito(1102))
