nums_convertation = [5, '65', '5f8', '-1', ['6'], [0], [6, 7], 'fgdg']  # Входные данные


def convert(spisok1: list) -> :
    itog: list = []
    for param1 in spisok1:
        if isinstance(param1, list):  # Проверяем списки
            try:
                itog.append(int(param1[0] if len(param1) < 2 else None))
            except:
                itog.append(None)
        elif type(param1) is str:  # Проверяем строки
            try:
                itog.append(int(param1))
            except:
                bufer: str = ''
                for param2 in param1:
                    try:
                        bufer += str(int(param2))
                    except:
                        pass
                try:
                    itog.append(int(bufer))
                except:
                    itog.append(None)
        elif type(param1) is int:  # Проверяем числа
            itog.append(int(param1))
        else:
            itog.append(None)  # Записываем остальные элементы

    return itog


print(convert(nums_convertation))
# Итог для сравнения 5, 65, 58, -1, 6, 0, None, None
