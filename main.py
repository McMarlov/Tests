a = 'loh1vfdmv1234dgfd5551f'
b = []
c = []
chislo = ''

for i in a:
    try:
        c.append(int(i))
    except:
        c.append(i)
c.append(None)
c.append(None)


def chisl(b, num1, num2, list1:list, znach = ''):
    if znach == '':
        print('скобки прошли')
        if type(list1[num1]) is int and type(list1[num2]) is int:
            print(list1[num1], list1[num2])
            print('1=2')
            znach = str(list1[num1]) + str(list1[num2])
            print(znach)
            chisl(b, num1 + 1, num2 + 1, list1, znach)
        elif type(list1[num1]) is int:
            b.append(list1[num1])
            return znach, b
        else:
            print('1!=2')
            print(znach)
            return znach, b
    else:
        if type(list1[num2]) is int and (list1[num2]) != None:
            print('скобки не прошли, num2 число')
            print(list1[num2])
            znach += str(list1[num2])
            chisl(num1 + 1, num2 + 1, list1, znach)
        else:
            print('скобки не прошли, num2 не число')
            print(znach)
            b.append(int(znach))
            znach = ''
            return znach, b


print(c)

for i in range(len(c)):
    if c[i] != None:
        print(c[i])
        znach, b = chisl(b, i, i + 1, c, '')



print(b)
print(c)
