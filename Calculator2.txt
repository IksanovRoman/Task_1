i=0

while True:
    try:
        a = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Введите число!")

print("Введите математическую операцию и число(через пробел)")

while True:
    if (i >= 1):
        print("Для выхода наберите =\nДля продолжения наберите математическую операцию и число: ")

    while True:
        try:
            b = input()

            if b == "=":
                print("Итоговый результат: ", a)
                break

            c, d = b.split(" ")
            d = float(d)
            if c != "+" and c != "-" and c != "*" and c != "/" and c != "**":
                raise Exception
            break
        except Exception:
            print("Некорректный ввод!\nПовторите результат: ")

    if b == "=":
        break

    try:
        if c == "+" or c == "-" or c == "*" or c == "/" or c == "**":
            if c == "+":
                a += d
            elif c == "-":
                a -= d
            elif c == "*":
                a *= d
            elif c == "/":
                a /= d
            elif c == "**":
                a **= d
    except ZeroDivisionError:
        print("Вы поделили на ноль! Ошибка!")

    i+=1