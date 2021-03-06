nums_convertation = [5, '65', '5f8', '-1', ['6'], [0], [6, 7], 'fgdg']  # Входные данные


def convert(spisok1: list) -> list:
    itog: list = []
    for param1 in spisok1:
        if isinstance(param1, list):  # Проверяем списки
            try:
                itog.append(int(param1[0] if len(param1) < 2 else ''))
            except ValueError:
                itog.append(None)
        elif isinstance(param1, str):  # Проверяем строки
            try:
                itog.append(int(param1))
            except ValueError:
                buffer = ''.join([i for i in param1 if i.isdigit()])
                try:
                    buffer = int(buffer)
                except ValueError:
                    buffer = None
                itog.append(buffer)
        elif isinstance(param1, int):  # Проверяем числа
            itog.append(int(param1))
        else:
            itog.append(None)  # Записываем остальные элементы

    return itog


print(convert(nums_convertation))
# Итог для сравнения 5, 65, 58, -1, 6, 0, None, None
