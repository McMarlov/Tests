spisok1 = ['Sumy', 'Kiev', 'Kharkov', 'Lviv']
spisok2 = ['viv', 'my', 'none', 'dog', 'spok', 'Kha']
spisok3 = []


for i1 in spisok2:
    for i2 in spisok1:
        if i1 in i2:
            spisok3.append(i1)


print(spisok3)
