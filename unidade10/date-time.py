import datetime

tempo = datetime.time(13,20,32)
print(tempo)
print(tempo.hour)
print(tempo.minute)
print(tempo.second)

dia = datetime.date(2018,11,23)
print(dia)
hoje = datetime.date.today()
print(hoje)
print(hoje.ctime())
print(hoje.isoweekday())

d1 = datetime.date(2018, 4, 2)
d2 = datetime.date(2018, 10, 23)
print(d2-d1)

string_d1 = d1.strftime('%Y-%m-%d')
print(string_d1)
