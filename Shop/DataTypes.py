import random
import math


def ex1():
    # int and float
    #
    # Wylosuj 6 liczb typu float z przedziału od -20 do 20 oraz 3 liczby całkowite z przedziału od 1 do 10.
    #
    # Następnie na pierwszych trzech liczbach typu float zastosuj zaokrąglanie (kolejno round, ceil oraz floor).
    #
    # Kolejne trzy liczby typu float podnieś do potęgi o wartości odpowiednio pierwszej, drugiej i trzeciej wylosowanej liczby całkowitej.
    rnd_int = []
    rnd_float = []

    for i in range(6):
        if i % 2 == 0:
            rnd_int.append(random.randint(1, 10))
        rnd_float.append(random.uniform(-20, 20))

    print(rnd_int)
    print(rnd_float)

    rnd_float[0] = round(rnd_float[0])
    rnd_float[1] = math.ceil(rnd_float[1])
    rnd_float[2] = math.floor(rnd_float[2])

    rnd_float[3] = math.pow(rnd_float[3], random.randint(1, 10))
    rnd_float[4] = math.pow(rnd_float[4], random.randint(1, 10))
    rnd_float[5] = math.pow(rnd_float[5], random.randint(1, 10))

    print(rnd_int)
    print(rnd_float)


def ex2():
    # Zadanie nr 1 Napisz funkcję, która wczyta od użytkownika jej/jego imię i nazwisko, “wyczyści je” z białych
    # znaków na początku i końcu tekstu, a następnie wypisze jakieś zdanie z tymi danymi np. “Nazywasz się {
    # first_name} {last_name} - jak miło Cię poznać :)”

    first_name = input("Enter first name\n>").lstrip().rstrip()
    last_name = input("Enter last name\n>").lstrip().rstrip()
    print(f"You are {first_name} {last_name}")

    # Zadanie nr 2 Napisz funkcję generującą losowy identyfikator. Identyfikator powinien być w formacie 00001,
    # tzn. zawsze o długości pięciu znaków, dopełniony z lewej strony odpowiednią liczbą zer.

    # number = str(random.randint(1, 99999)).zfill(5)
    # print(number)

    # Zadanie nr 3
    # Wczytaj od użytkownika jej/jego ulubione kolory (jako jeden napis, np. rozdzielony przecinkiem).
    #
    # Sprawdź, czy znajduje się wśród nich niebieski, a następnie wypisz odpowiedni komunikat.

    # colors = input("Enter your favourite colours (format: color1, color2...)\n>")
    # if colors.find("blue") != -1:
    #     print("You like blue")
    # else:
    #     print("You don't like blue")

    # Zadanie nr 4
    # Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać metodę format.

    # first_name = input("Enter first name\n>").lstrip().rstrip()
    # last_name = input("Enter last name\n>").lstrip().rstrip()
    # print("You are {} {}".format(first_name, last_name))

def ex3():

    list1 = [number for number in range(30) if number % 3 == 0]
    print(list1)
    list2 = [number for number in range(30) if number % 5 == 0]
    print(list2)

    userInput = input("Enter your favourite sports. (sport1 sport2 sport3)")
    userSoprts = userInput.split(" ")
    print([sport for index, sport in enumerate(userSoprts) if index % 2 == 0])

def ex4():
    pass