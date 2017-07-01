""" 
zapraszam na https://github.com/sledziu32/python_nauka
"""
import re
Str1 = "Ale dzisiaj wieje."

Str2 = Str1[0:7]    #znaki od pierwszego (indeks 0) do siódmego
                    #(indeks 6 - znak o ineksie 7 będzie już 'wyciętym')
Str3 = Str1[5:]     #znaki od szóstego (indeks 5) do końca
Str4 = Str1[-5:-1]  #znaki od piątego od końca do ostatniego
Str5 = Str1[11]     #pojedynczy dzisiąty znak (indeks 11)

print(Str1)
print(Str2)
print(Str3)
print(Str4)
print(Str5)

ciag1 = "#%9147876DFBBGFdfgSDFGjhnmy  .sdfgijirtj"

ciag2 = re.sub('[^0-9]', '§', ciag1)    #znaki niebędące cyframi zamienia na paragraf §
ciag3 = re.sub('[" "%#.]', '§', ciag1)   #spacja, kropka % i # zamienia na paragraf §


print(ciag2)
print(ciag3)
