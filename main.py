
try:
 Str1 = (input("Введите дату вашего рождения первого человека в формате 00.00.0000: "))
 Str2 = (input("Введите дату вашего рождения второго человека в формате 00.00.0000: "))
except:
    print("Введены не коректные данные")
try:
    reh = int(str(Str1)[3:5:]) == 4 or int(str(Str1)[3:5:]) == 6 or int(str(Str1)[3:5:]) == 9 or int(str(Str1)[3:5:]) == 11  # 30 дней
    reh0 = int(str(Str2)[3:5:]) == 4 or int(str(Str2)[3:5:]) == 6 or int(str(Str2)[3:5:]) == 9 or int(str(Str2)[3:5:]) == 11
    reh11 = int(str(Str1)[3:5:]) == 1 or int(str(Str1)[3:5:]) == 3 or int(str(Str1)[3:5:]) == 5 or int(str(Str1)[3:5:]) == 7 or int(str(Str1)[3:5:]) == 8 or int(str(Str1)[3:5:]) == 10 or int(str(Str1)[3:5:]) == 12  # 31 день
    reh12 = int(str(Str2)[3:5:]) == 1 or int(str(Str2)[3:5:]) == 3 or int(str(Str2)[3:5:]) == 5 or int(str(Str2)[3:5:]) == 7 or int(str(Str2)[3:5:]) == 8 or int(str(Str2)[3:5:]) == 10 or int(str(Str2)[3:5:]) == 12
    reh1 = int(str(Str1)[3:5:])  == 2 or int(str(Str2)[3:5:]) == 2 # 28 дней
    reh2 = int(str(Str1)[3:5:]) > 12 or int(str(Str2)[3:5:]) > 12  # ограничение на количество месяцев
    day1 = int(str(Str1)[0:2:]) <= 28 and int(str(Str2)[0:2:]) <= 28 # ограничение по дням
    day2 = int(str(Str1)[0:2:]) <= 30 and int(str(Str2)[0:2:]) <= 30
    day3 = int(str(Str1)[0:2:]) <= 31 and int(str(Str2)[0:2:]) <= 31
    year1 = int(str(Str1)[6::]) >= 1900 and int(str(Str2)[6::]) >= 1900  # ограничение по годам
    yaer2 = int(str(Str1)[6::]) <= 2023 and int(str(Str2)[6::]) <= 2023
    if (reh2 == False):
        pass
    else:
        print("неверно указан месяц")
    if (reh == True and day2 == True or reh1 == True and day1 == True or reh11 == True and day3 == True):
        pass
    else:
        print("неверно указан день")
    if (reh0 == True and day2 == True or reh12 == True and day3 == True):
        pass
    else:
        print("неверно указан день")
    if (year1 == True and yaer2 == True):
        pass
    else:
        print("неверно указан год")
    d = int(str(Str2)[3:5:]) - int(str(Str1)[3:5:])
    g = int(str(Str1)[3:5:]) - int(str(Str2)[3:5:])
    if (d < 0 or g < 0):
        d1 = -1
    else:
        d1 = 0
    f = int(str(Str1)[6::]) - int(str(Str2)[6::]) + d1
    f1 = int(str(Str2)[6::]) - int(str(Str1)[6::]) + d1
    if (f<0):
        s = f'Первый человек старше на {f1} '
    elif (f1<0):
        s = f'Второй человек старше на {f} '
    else:
        pass
    by = f or f1 == 1,11,21,31,41,51,61,71,81,91
    by1 = 2<=f1 or f>=4 or 22<=f1 or f>=24 or 32<=f1 or f>=34 or 42<=f1 or f>=44  or 52<=f1 or f>=54 or 62<=f1 or f>=64 or 72<=f1 or f>=74 or 82<=f1 or f>=84 or 92<=f1 or f>=94
    if by == True:
        v = ("год")
    elif by1 == True:
        v = ("года")
    else:
        v = ("лет")
    x = f'{s}{v}'
    print (x)
except:
    print("Ошибка обработки")