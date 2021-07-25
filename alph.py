chislo = 'XXII'
# Вместо этих двух строк можно: 
# spisoc = list(spisoc).append(None)
spisok = [i for i in chislo]
spisok.append(None)
itog = 0
slovar = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}
def rim(numb:int):
    # Можно было не создавать переменную arab
    arab = slovar[spisok[numb]]
    return arab

for i in range(len(spisok)-1):
    # Если сравниваешь с None нужно писать spisoc is not None
    # Но в этом случае тебе и это не нужно, достаточно просто
    # if spisok[i+1]: 
    if spisok[i+1]!= None:
        if rim(i) < rim(i+1):            
            itog-=rim(i)
        else:
            itog+=rim(i)
    else:
        itog+=rim(i)
print(itog)
