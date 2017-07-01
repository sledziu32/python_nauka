import datetime

d1 = datetime.date(1988, 10, 26)

print("rok: ", d1.year)
print("miesiac: ", d1.month)
print("dzień: ", d1.day)

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)

print(mill+dt)

print("podaj datę aby dowiedzieć się jaki to był dzień tygodnia")
y = input("Podaj rok ")
m = input("podaj miesiąc ")
d = input("podaj dzień ")

d2 = datetime.date(int(y), int(m), int(d))
print(d2.strftime("%A"))

wiadomosc = "urodziłem się {:%d - %m - %Y}"
print(wiadomosc.format(d1))