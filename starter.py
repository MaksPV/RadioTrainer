from os import system
import requests
import subprocess


print("Проверка обновлений")
try:
    upd = requests.get('https://raw.githubusercontent.com/MaksPV/RadioTrainer/main/dist/files/last_version.txt')
    upd_info = upd.text.splitlines()
    upd_vers = float(upd_info[0])
    with open("files/last_version.txt", "r") as f:
        now = f.read().splitlines()
        now_vers = float(now[0])
    
    if upd_vers > now_vers:
        print(f"""
Найдено обновление
{upd_info[0]}

Изменения:
{'''
'''.join(upd_info[1:])}

Обновить?
1 - Да, 2 - Нет""")
        menu = input()
        if menu == "1":
            new_vers = requests.get('https://raw.githubusercontent.com/MaksPV/RadioTrainer/main/dist/files/RadioTrainer.exe')
            with open("files/RadioTrainer.exe", "wb") as f:
                f.write(new_vers.content)
                f.close()
            new_last = requests.get('https://raw.githubusercontent.com/MaksPV/RadioTrainer/main/dist/files/last_version.txt')
            with open("files/last_version.txt", "wb") as f:
                f.write(new_last.content)
                f.close()
    elif upd_vers == now_vers:
        print("Установлена последняя версия, вы прекрасны")
    elif upd_vers < now_vers:
        print("Не хочешь попасть в команду RadioTrainer?")
    else:
        print("Ошибка, файл обновлений не найден")
except BaseException:
    print("Нет интернета, попробуйте позже")

subprocess.call("files/RadioTrainer.exe")
