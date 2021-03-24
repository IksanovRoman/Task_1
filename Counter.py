import re

def inp ():
    while True:
        text = input("Введите текст на английском языке: ")
        if text.isalpha()==False:
            print("Необходимо ввести только буквы!")
        elif re.search('[^a-zA-Z]', text):
            print("Необходимо ввести текст на английском языке!")
        else:
            break
    return text

def counter(text2):
    i=[0,0,0,0,0,0]
    print("Ваш текст:", text2)

    for value in text2:
        if value == "a" or value == "A" in text2:
            i[0] += 1
        if value == "o" or value == "O" in text2:
            i[1] += 1
        if value == "u" or value == "U" in text2:
            i[2] += 1
        if value == "i" or value == "I" in text2:
            i[3] += 1
        if value == "e" or value == "E" in text2:
            i[4] += 1
        if value == "y" or value == "Y" in text2:
            i[5] += 1

    return i

text = inp()
a = counter(text)
print("A:",a[0], "\nO:",a[1], "\nU:",a[2], "\nI:",a[3], "\nE:",a[4], "\nY:",a[5])