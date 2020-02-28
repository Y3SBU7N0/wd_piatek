print('Hemlo World')

def main():
	pass
# Łańcuchy znaków
imie = "Mariusz"
print(imie)
print(type(imie))
print(type(5))
print(type(5.7))
print(type(True))
print(type(None))
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>
print(imie[2])
# imie[0] = "D" # str nie mutowalny
imie = "Dariusz"
imie = imie.lower()
print(imie)
wiek = 30
#print(imie + " ma" + wiek + " lat.")
print(imie + " ma " + wiek.__str__() + " lat.")
print(imie + " ma " + str(wiek) + " lat.")
print("{} ma {} lat.".format(imie, wiek))
# f-string
print(f"{imie} ma {wiek} lat.")
# pyformat.info
liczba = 6.213742069
print(f"{liczba:.4f}")

# typ liczby
liczba = 5
liczbaf = 5.5
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 // 2) # dzielenie bez reszty
print(1 ** 2) # potęgowanie
print(1 % 2) # modulo

tekst = "69420"
liczba_z_tekstu = int(tekst)
print(liczba_z_tekstu)
import math
pi = 3.15
import math as m
m.pow()
print(m.pi)

# listy
lista = [] # pusta lista
lista2= list() # pusta lista
lista3= [1, 2, 3] 
lista4= [1, "Ala", True, None, [1, 2]]
lista4[1] = "Zocha"

macierz = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print(macierz [1][1])
print(0.1 + 0.2 == 0.3)
# Decimal
print(f"{0.1:.32f}")

lista = lista + lista3
lista += lista3

# sŁownik
slownik = {}
slownik2 = dict()
slownik3 = {"klucz": "wartość"}
slownik3['klucz']
slownik3['klucz'] = 100
slownik3[0] = 999
print(slownik3)
slownik3.keys()
slownik3.values()
print(slownik3.items())

