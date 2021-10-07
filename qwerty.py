# Zadanie 1
def kropka(imie, nazwisko):
    print(f'{imie}.{nazwisko}')


kropka("Konrad", "Kisiel")

# Zadanie 2
def skrot(imie, nazwisko):
    print(imie[0].title() + "." + nazwisko.title())


skrot("konrad", "kisiel")

# Zadanie 3
def rok(fst, lst, age):
    curr = fst + lst
    birth = int(curr) - int(age)
    print(birth)



rok("20","21","20")

# Zadanie 4

def fun(imie, nazwisko, zad2):
    zad2(imie, nazwisko)


fun("konrad", "kisiel", skrot)

# Zadanie 5

def dzielenie(l1, l2):
    if l1 >= 0 and l2 > 0:
        print(l1/l2)

dzielenie(24,8)

# Zadanie 6
# suma = 0
# while suma < 100:
#     i = int(input("Suma wciąż mniejsza od stu, podaj kolejną liczbę: "))
#     suma += i
#
#
# print(f'Suma przekroczyłą 100 i wynosi: {suma}')

# Zadanie 7

def krotka(lista):
    tup = tuple(lista)
    print(tup)

lista1 = [1, 2, 5]
krotka(lista1)

# Zadanie 8

lista2 = []
while True:
    answer = input("Chcesz dodać element do listy? t/n")
    if answer == "t":
        lista2.append(input("element do dodania: "))
    elif answer == "n":
        print(lista2)
        break

# zadanie 9








