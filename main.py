str1 = 15
str2 = 1
str3 = 2023
try:
 Str1 = int(input("Введите день вашего рождения "))
 Str2 = int(input("Введите месяц вашего рождения "))
 Str3 = int(input("Введите год вашего рождения "))
except:
    print("Введены не коректные данные")
try:
 reh = Str2 == 4 or Str2 == 6 or Str2 == 9 or Str2 == 11 # 30 дней
 reh11 = Str2 == 1 or Str2 == 3 or Str2 == 5 or Str2 == 7 or Str2 == 8 or Str2 == 10 or Str2 == 12 # 31 день
 reh1 = Str2 == 2 # 28 дней
 reh2 = Str2 > 12 #ограничение на количество месяцев
 day1 = Str1 <= 28 # ограничение по дням
 day2 = Str1 <= 30
 day3 = Str1 <= 31
 year1 = Str3 >= 1900 # ограничение по годам
 yaer2 = Str3 <=2023
 if (reh2 == False):
    pass
 else:
    print("неверно указан месяц")
 if (reh == True and day2 == True or reh1 == True and day1 == True or reh11 == True and day3 == True):
   pass
 else:
    print("неверно указан день")
 if (year1 == True and yaer2 == True):
    pass
 else:
    print("неверно указан год")
 f1 = (str3-Str3)
 f2 = (str2-Str2)
 f3 = (str1-Str1)
 if f3 <= 0:
     c1=f2-1
 else:
     pass
 if f2 <= 0:
     c2=f1-1
 else:
    pass
 s = f"Ваш возраст {c2}"
 print(s)
except:
    print("Ошибка обработки")
