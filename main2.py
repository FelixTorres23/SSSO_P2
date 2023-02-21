import os
import random
import string
import shutil


def copiar_carpeta(src_folder, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    for item in os.listdir(src_folder):
        s = os.path.join(src_folder, item)
        d = os.path.join(dst_folder, item)
        if os.path.isdir(s):
            copiar_carpeta(s, d)
        else:
            shutil.copy2(s, d)


def numeros_a_letras(text):
    new_text = ''
    for char in text:
        if char.isdigit():
            new_text += random.choice(string.ascii_uppercase)
        else:
            new_text += char
    return new_text

def letras_a_numeros(text):
    new_text = ''
    for char in text:
        if char.isalpha():
            new_text += str(random.randint(0,9))
        else:
            new_text += char
    return new_text


folder_path = input("Ingrese la ruta de la carpeta a procesar: ")

copiar_carpeta(folder_path, folder_path + '_copy')


for root, dirs, files in os.walk(folder_path + '_copy'):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'r') as f:
            content = f.read()
            content = letras_a_numeros(content)
            content = numeros_a_letras(content)
        with open(file_path, 'w') as f:
            f.write(content)

print("Procesamiento de archivos finalizado.")
