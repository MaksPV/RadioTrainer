import requests
from os import mkdir

print("Загрузка")
mkdir("files")
with open("files/RadioTrainer.exe", "wb") as f:
    file = requests.get('https://raw.githubusercontent.com/MaksPV/RadioTrainer/main/dist/files/RadioTrainer.exe')
    f.write(file.content)
    f.close()
with open("files/last_version.txt", "wb") as f:
    file = requests.get('https://raw.githubusercontent.com/MaksPV/RadioTrainer/main/dist/files/last_version.txt')
    f.write(file.content)
    f.close()
with open("starter.exe", "wb") as f:
    file = requests.get('https://raw.githubusercontent.com/MaksPV/RadioTrainer/main/dist/starter.exe')
    f.write(file.content)
    f.close()

print("Успешно, чтобы запустить, запустите starter.exe")
input()