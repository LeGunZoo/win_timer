import os
print("--------------------------\nTERMINAL VERSION 0.1\n--------------------------\nProgram: shutdown computer\nAuthor: A.D.")
print("\nChoose language (ru/en)")
lang=input()
def shut_en():
    print("\nВыключить или отменить выключение? 1/2")
    oper= input()
    if oper == "1":
        print("Через сколько выключить компьютер?(минуты)")
        time = input()
        time_min = int(time) * 60
        os.system("shutdown /s /t "+str(time_min))
        print("Выполнить еще одну операцию? Y/N")
        answer=input()
        if str(answer).upper() == ("N").upper:
            exit()
        elif str(answer).upper() == ("Y").upper():
             shut_en()
        elif str(answer).upper() != ("N").upper() or str(answer).upper() != ("Y").upper():
            print("Неверный вариант ответа")
    elif oper == "2":
        os.system("shutdown /a")
        print("Выполнить еще одну операцию? Y/N")
        answer = input()
        if str(answer).upper() == ("N").upper:
            exit()
        elif str(answer).upper() == ("Y").upper():
            shut_en()
        elif str(answer).upper() != ("N").upper() or str(answer).upper() != ("Y").upper():
            print("Неверный вариант ответа")
    elif str(oper) != "1" or str(oper) != "2":
        print("Неверно введена операция")
        shut_en()

def shut_ru():
    print("\nВыключить или отменить выключение? 1/2")
    oper= input()
    if oper == "1":
        print("Через сколько выключить компьютер?(минуты)")
        time = input()
        time_min = int(time) * 60
        os.system("shutdown /s /t "+str(time_min))
        print("Выполнить еще одну операцию? Y/N")
        answer=input()
        if str(answer).upper() == ("N").upper:
            exit()
        elif str(answer).upper() == ("Y").upper():
             shut_ru()
        elif str(answer).upper() != ("N").upper() or str(answer).upper() != ("Y").upper():
            print("Неверный вариант ответа")
    elif oper == "2":
        os.system("shutdown /a")
        print("Выполнить еще одну операцию? Y/N")
        answer = input()
        if str(answer).upper() == ("N").upper:
            exit()
        elif str(answer).upper() == ("Y").upper():
            shut_ru()
        elif str(answer).upper() != ("N").upper() or str(answer).upper() != ("Y").upper():
            print("Неверный вариант ответа")
    elif str(oper) != "1" or str(oper) != "2":
        print("Неверно введена операция")
        shut_ru()

if lang.upper() ==  ("ru").upper():
    shut_ru()
elif lang.upper() == ("en").upper():
    shut_en()
elif lang.upper()!=("ru") or lang.upper()!= ("en"):
    print("Invalid value selected")

