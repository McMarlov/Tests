a = 'loh1vfdmv1234dgfd5551f'
b = ''
c = []

for i in a:
    try:
        b+=str(int(i))
    except:
        if b != '':
            c.append(b)
        b = ''

print(c)
