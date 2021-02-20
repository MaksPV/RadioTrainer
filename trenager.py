from random import choice, randint
from time import time
from os import listdir, mkdir
from itertools import repeat
from sys import exit
from dict import *

version = 1.0
type_of = "terminal"


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

bases = listdir(path="bases")

print("""  _               ___                   
 |_)  _.  _| o  _  | ._ _. o ._   _  ._ 
 | \ (_| (_| | (_) | | (_| | | | (/_ |  
                                        """)
print(f"Версия: {str(version)}")
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

print()
print("Сколько раз повторять?")
print("0 - бесконечность раз")
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
print()
input("Enter чтобы выйти")    
