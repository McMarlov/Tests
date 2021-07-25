chislo = 'XXII'
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
    arab = slovar[spisok[numb]]
    return arab

for i in range(len(spisok)-1):
    if spisok[i+1]!= None:
        if rim(i) < rim(i+1):            
            itog-=rim(i)
        else:
            itog+=rim(i)
    else:
        itog+=rim(i)
print(itog)