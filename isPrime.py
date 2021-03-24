while True:
    try:
        a = int(input("Введите число: "))
        if a<=0:
            raise Exception
        break
    except ValueError:
        print("Ввод некорректный. Введите целое положительное число!")
    except Exception:
        print("Введите целое положительное число!")

print("Вы ввели: ", a)
counter=0

if a>2 and a<10:
    for i in range (2, a):
        counter=0
        if(a%i==0):
            print(f"Число {a} не является простым!")
            break
        else:
            counter=1

if counter==1 or a==1 or a==2:
    print(f"Число {a} простое!")

if a >= 10:
    if (a%2==0) or (a%3==0) or (a%4==0) or (a%5==0) or (a%6==0) or (a%7==0) or (a%8==0) or (a%9==0):
        print(f"Число {a} не является простым!")
    else:
        print(f"Число {a} простое!")
