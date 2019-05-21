import datetime
import time

a = datetime.datetime.today().strftime("%Y")
a = int(a)-1
print(a, '\n')  # '20170405'

# from datetime import date, timedelta

delta = int(input('Введите разницу во времени:\ndelta='))
date_now = datetime.datetime.today()
year_now = date_now.strftime('%Y')
print(year_now, 'Год текущий')
print(int(year_now)-delta, 'Год ранее текущего на число лет, равное "delta"')
print(datetime.date.today() - datetime.timedelta(days=delta), 'Дата меньшая на число дней, равное "delta"')

print(datetime.datetime.now(tz=None))

#    Запрос имени: присваивание переменной name введенного имени
#    и вывод приветсвия
name = input('\nКак тебя зовут? \n')
print ('\nПривет','', name,'\n')

#    Запрос фамилии
family = input ('А как твоя фамилия? \n')
print ('\nОчень приятно,', name, family, '!' '\nТеперь мы знакомы!\n')

age = input('А сколько тебе лет?\n')  # Запрос возраста и вычисление года рождения

data_now = datetime.datetime.now()
year_now = int(data_now.strftime('%Y'))
year = year_now - int(age)
print('\nЗначит ты родился в', year, 'году?\n')

#    Проверка года рождения
ans = input('Да или нет?\n')

time.sleep(1)
if ans == 'Нет' or ans == 'нет':
    print('\nТогда твой год рождения -', str(year - 1), '!',
          '\nУра, наконец я угадал!!!\n\n\n')
elif ans == 'Да' or ans == 'да':
    print('\nЗначит я правильно угадал!!!\n\n')
else:
    print('\nНе понял ответа, ответьте еще раз, пожалуйста!\n')
time.sleep(2)

#    Не дать закрыться консоли после выполнения программы
input('Нажми на клавишу "Enter" чтобы закрыть окно')

'''Не рекомендуется использовать такой синтаксис импорта, программа будет путать переменные с переменными в модуле'''
#    from time import *
#    Задержка перед закрытием окна на время sleep(x)
time.sleep(1)
