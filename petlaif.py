""" 
zapraszam na https://github.com/sledziu32/python_nauka
"""

"""
porównanie liczb czy są takie same
"""
x = int(5)
#y = "5"    nie można porównać ciągu z liczbą
y = float(5)    #float może być równy intigerowi jeżeli nie ma części ułamkowych
if x == y:
    print("super! ")
else:
    print("niestety")
    
a = 5
b = 5
if a != b:
    print("wartości są różne")
else:
    print("wartości są równe")

q = 6 < 4
if q:
    print(q)    #wypisze True
else:
    print(q)    #wypisze False