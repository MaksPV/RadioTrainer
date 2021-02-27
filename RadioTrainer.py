from random import choice, randint
from time import time
from os import listdir, mkdir
from itertools import repeat
from sys import exit
from dicti import *


attention = False
try: 
    with open("files/last_version.txt", "r") as f:
            now = f.read().splitlines()
            version = float(now[0])
except:
    version = 0.00
    attention = True


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


def generator():
    poz = choice("ABCDEFGHIJKLMNOPRSTUVWXYZ")
    for _ in range(randint(3, 5)):
        poz += choice("QWERTYUIOPASDFGHJKLZXCVBNM0123456789")
    return poz


def rus_generator():
    regions = {
        "0": "CDFEIJKLMNQZXABHOSRTUVWY",
        "1": "ABCDNOPQRSTWZ",
        "2": "FKABCDHEGILMNPOQRSUVWXYZT",
        "3": "ABCDFHEGILMNPKOQRSUVWXYZT",
        "4": "ABFHILMNPQRSTUWYZ",
        "5": "ABCDFHEGILMNPKOQRSUVWXYZ",
        "6": "ABCDILMNUYEHFGJPRQWX",
        "7": "ABCDILMNUYEHFGJPRQWX",
        "8": "XFGSTWABCDJKLQRHIMNOPUVYZ",
        "9": "XFGSTWABCDJKLQRHIMNOPUVYZ"
        }
    
    poz = choice("UR")
    if poz == "U":
        poz += choice("ABCDFGHI")
    else:
        poz += choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    poz += choice("1234567890")
    poz += choice(regions[poz[-1]])
    
    for _ in range(randint(0, 2)):
        poz += choice("QWERTYUIOPASDFGHJKLZXCVBNM")
    return poz


if "bases" not in listdir():
    mkdir("bases")
    with open("bases/База из контеста.txt", "w") as f:
        f.write(contest)
        f.close()
else:
    pass

bases = listdir(path="bases")

print("""  _               ___                   
 |_)  _.  _| o  _  | ._ _. o ._   _  ._ 
 | \ (_| (_| | (_) | | (_| | | | (/_ |  
                                        """)
print(f"""Версия: {str(version)}
Накалякал t.me/maksimushka для себя и товарищей из UG5R
Большими буквами необязательно писать""")

if attention:
    print()
    print("!Вы используете версию без автообновления!")
    print("!Скачайте правильную версию на https://github.com/MaksPV/RadioTrainer/releases!")
    print()
print("""Какую базу?

0 - Выйти
1 - Случайно генерируемая
2 - Случайно генерируемые русские позывные""")
[print(i + 3, bases[i], sep=" - ") for i in range(len(bases))]

while True:
    baze = input()
    try:
        if 0 <= int(baze) - 3 <= len(bases) - 1 or baze == "2" or baze == "1" \
                or baze == "0":
            break
        else:
            print("Неправильный ввод")
    except:
        print("Неправильный ввод")
print()

if baze != "2" and baze != "1" and baze != "0":
    with open("bases/" + bases[int(baze) - 3], "r") as f:
        custom = f.read().split()
        f.close()
if baze == "0":
    exit()

modes = {"0": "Просто перепись позывных",
"1":  "Позывной -> русская фонетическая азбука",
"2": "Позывной -> международная фонетическая азбука",
"3": "Русская фонетическая азбука -> позывной",
"4": "Международная фонетическая азбука -> позывной"}

print("Выберите режим:")
[print(x, y, sep=" - ") for x, y in modes.items()]
while True:
    mode = input()
    if mode in "12340" and mode != "":
        break
    else:
        print("Неправильный ввод")

time_s = time()
true = 0
wrong = []

print("""
Сколько позыных?
0 - бесконечно""")

while True:
    count = input()
    if count.isdigit() and count != "0":
        iterator = range(int(count))
        break
    elif count == "0":
        iterator = repeat(1)
        break
    else:
        print("Неправильный ввод")
print()

for _ in iterator:
    time_start = time()
    if baze == "1":
        poz = generator()
    if baze == "2":
        poz = rus_generator()
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
        break
    else:
        print("Неправильно")
        wrong.append((poz1, answer))
    print()

print()
print("Итого:")
print(modes[mode])

if baze == "1":
    print("База из случайных")
elif baze == "2":
    print("База из случайных русских")
else:
    print(bases[int(baze) - 2])

print(f"""Прошло: {round(time() - time_s, 2)} секунд
Правильно: {true}
Неправильно: {len(wrong)}
Правильных позывных в минуту: {round(true / ((time() - time_s) / 60), 2)}""")
                               
if true != 0:
    print("В среднем на правильный позывной:", round((time() - time_s) / true, 2), "секунд")
else:
    print("В среднем на правильный позывной: 0 секунд")

print()
[print(x, y, sep="\t") for x, y in wrong]
print()

input("Enter чтобы выйти")    
