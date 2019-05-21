# Get The Current Date Or Time
# Назначение новой функции и присваивание ей имени getdatetime


def GetDateTime(Format='complete'):
    from datetime import datetime
    Format = Format.lower()
    if Format == 'day':
        return ((str(datetime.now())).split(' ')[0]).split('-')[2]
    elif Format == 'month':
        return ((str(datetime.now())).split(' ')[0]).split('-')[1]
    elif Format == 'year':
        return ((str(datetime.now())).split(' ')[0]).split('-')[0]
    elif Format == 'hour':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
    elif Format == 'minute':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1]
    elif Format == 'second':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2]
    elif Format == 'millisecond':
        return (str(datetime.now())).split('.')[1]
    elif Format == 'year_month_day':
        return (str(datetime.now())).split(' ')[0]
    elif Format == 'day_month_year':
        return ((str(datetime.now())).split(' ')[0]).split('-')[2] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[1] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[0]
    elif Format == 'hour_minute_second':
        return ((str(datetime.now())).split(' ')[1]).split('.')[0]
    elif Format == 'second_minute_hour':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
    elif Format == 'complete':
        return str(datetime.now())
    elif Format == 'datetime':
        return (str(datetime.now())).split('.')[0]
    elif Format == 'timedate':
        return ((str(datetime.now())).split('.')[0]).split(' ')[1] + ' ' + ((str(datetime.now())).split('.')[0]).split(' ')[0]


print(int(GetDateTime('day')) + 2, '.', end='')
print(GetDateTime('month'), '.', end='')
print(GetDateTime('year'))
print(GetDateTime('hour'))
print(GetDateTime('minute'))
print(GetDateTime('second'))
print(GetDateTime('millisecond'))
print(GetDateTime('year_month_day'))
print(GetDateTime('day_month_year'))
print(GetDateTime('hour_minute_second'))
print(GetDateTime('second_minute_hour'))
print(GetDateTime('complete'))
print(GetDateTime('datetime'))
print(GetDateTime('timedate'))
print(end='')
Format = input('Введите желаемый формат вывода даты = \n')
print(GetDateTime(Format), end='')

input()
