from random import choice, randint
from time import time
from os import listdir, mkdir


RusPhonk = {
    "a": "Анна",
    "b": "Борис",
    "c": "Центр",
    "d": "Дмитрий",
    "e": "Елена",
    "f": "Фёдор",
    "g": "Галина",
    "h": "Харитон",
    "i": "Иван",
    "j": "Иван-Краткий",
    "k": "Киловатт",
    "l": "Леонид",
    "m": "Мария",
    "n": "Николай",
    "o": "Ольга",
    "p": "Павел",
    "q": "Щука",
    "r": "Радио",
    "s": "Сергей",
    "t": "Татьяна",
    "u": "Ульяна",
    "v": "Жук",
    "w": "Василий",
    "x": "Знак",
    "y": "Игрек",
    "z": "Зоя"
}

EngPhonk = {
    "a": "Alfa",
    "b": "Brave",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Radio",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "X-Ray",
    "y": "Yankee",
    "z": "Zulu"
}

EngToRus = {
    "a": "а",
    "b": "б",
    "c": "ц",
    "d": "д",
    "e": "е",
    "f": "ф",
    "g": "г",
    "h": "х",
    "i": "и",
    "j": "й",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "p": "п",
    "q": "щ",
    "r": "р",
    "s": "с",
    "t": "т",
    "u": "у",
    "v": "ж",
    "w": "в",
    "x": "ь",
    "y": "ы",
    "z": "з",
}
 
Dopust = {
    "Мягкий_Знак": "Знак",
    "Семён": "Сергей",
    "Семен": "Сергей",
    "Антон": "Анна",
    "Роман": "Радио",
    "Зинаида": "Зоя",
    "Ёлка": "Елена",
    "Елка": "Елена",
    "Григорий": "Галина",
    "Йот": "Иван-Краткий",
    "America": "Alfa",
    "Florida": "Foxtrot",
    "Guatemala": "Golf",
    "Honolulu": "Hotel",
    "Italy": "India",
    "Kilowatt": "Kilo",
    "Mexico": "Mike",
    "Nency": "November",
    "Ontario": "Oscar",
    "Romeo": "Radio",
    "Rodger": "Radio",
    "Santiago": "Sierra",
    "Sugar": "Sierra",
    "Texas": "Tango",
    "United": "Uniform",
    "Washington": "Whiskey",
    "Cristmass": "X-Ray",
    "Yokohama": "Yankee",
    "Zanzibar": "Zulu",
    "Ноль": "0",
    "Zero": "0",
    "Один": "1",
    "One": "1",
    "Два": "2",
    "Two": "2",
    "Три": "3",
    "Three": "3",
    "Четыре": "4",
    "Four": "4",
    "Пять": "5",
    "Five": "5",
    "Шесть": "6",
    "Six": "6",
    "Семь": "7",
    "Seven": "7",
    "Восемь": "8",
    "Eight": "8",
    "Девять": "9",
    "Nine": "9"
}
 
 
def encode_to_RusPhonk(text):
    RusToEng = {v: k for k, v in EngToRus.items()}
    b1 = list(text.lower())
    b = []
    for i in b1:
        try:
            b.append(RusToEng[i])
        except KeyError:
            b.append(i)
    res = []
    for j in b:
        try:
            res.append(RusPhonk[j])
        except KeyError:
            res.append(j)
    return " ".join(res)


def encode_to_EngPhonk(text):
    b1 = list(text.lower())
    b = []
    for i in b1:
        try:
            b.append(EngPhonk[i])
        except KeyError:
            b.append(i)
    res = []
    for j in b:
        try:
            res.append(EngPhonk[j])
        except KeyError:
            res.append(j)
    return " ".join(res)
 
 
def encode_to_dopust(text):
    res = []
    for i in text.split():
        try:
            res.append(Dopust[i])
        except KeyError:
            res.append(i)
    return " ".join(res)


if "bases" not in listdir():
    mkdir("bases")
else:
    pass
#    print(listdir(path="bases"))

bases = listdir(path="bases")

print("Накалякал t.me/maksimushka для себя и товарищей из UG5R")
print("большими буквами необязательно писать, 0 - выход")
print()
print("Какую базу?")
print("")
print("0 - выйти")
print("1 - случайно генерируемая")
[print(i + 2, bases[i], sep=" - ") for i in range(len(bases))]
while True:
    baze = input()
    try:
        if 0 <= int(baze) - 2 <= len(bases) - 1 or baze == "1" or baze == "0":
            break
        else:
            print("Неправильный ввод")
    except:
        print("Неправильный ввод")
print()

if baze != "1" and baze != "0":
    with open("bases/" + bases[int(baze) - 2], "r") as f:
        custom = f.read().split()
        f.close()

print("Выберите режим:")
print("0 - просто перепись позывных")
print("1 - позывной -> русская фонетическая азбука")
print("2 - позывной -> международная фонетическая азбука")
print("3 - русская фонетическая азбука -> позывной")
print("4 - международная фонетическая азбука -> позывной")
while True:
    mode = input()
    if mode in "12340":
        break
    else:
        print("Неправильный ввод")

time_s = time()
true = 0
wrong = []
while True:
    time_start = time()
    if baze == "1":
        poz = "".join([choice("QWERTYUIOPASDFGHJKLZXCVBNM0123456789") for _ in range(randint(4, 6))])
    elif baze == "0":
        break
    else:
        poz = choice(custom)
    
    if mode == "0":
        poz1 = poz
    elif mode == "1":
        poz1 = encode_to_RusPhonk(poz)
    elif mode == "2":
        poz1 = encode_to_EngPhonk(poz)
    elif mode == "3":
        poz1 = poz
        poz = encode_to_RusPhonk(poz)
    elif mode == "4":
        poz1 = poz
        poz = encode_to_EngPhonk(poz)
    
    print("Введите 0 для выхода и просмотра результатов")
    print(poz)
    if mode == "0":
        answer = input().upper()
    elif mode == "1" or mode == "2":
        answer = encode_to_dopust(input().title())
    elif mode == "3" or mode == "4":
        answer = input().upper()
    
    if poz1 == answer:
        print("Правильно")
        print(round(time() - time_start, 2), "секунд")
        true += 1
    elif answer == "0":
        print()
        print("Итого:")
        if baze == "1":
            print("База из случайных")
        else:
            print(bases[int(baze) - 2])
        
        print("Прошло:", round(time() - time_s, 2), "секунд")
        print("Правильно:", true)
        print("Неправильно:", len(wrong))
        print("Правильных позывных в минуту:", round(true / ((time() - time_s) / 60), 2))
        if true != 0:
            print("В среднем на правильный позывной:", round((time() - time_s) / true, 2), "секунд")
        else:
            print("В среднем на правильный позывной: 0 секунд")
        print()
        [print(x, y, sep="\t") for x, y in wrong]
        break
    else:
        print("Неправильно")
        wrong.append((poz1, answer))
    print()

print()
input("Enter чтобы выйти")    
