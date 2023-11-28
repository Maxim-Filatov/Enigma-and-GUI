# -*- coding: cp1251 -*-
import random
from tkinter import *
from tkinter import ttk


def generate_enigma_key():
    # Генерация случайного ключа
    rotor1 = list("0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя ")
    rotor2 = list("0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя ");

    # Перемешивание элементов списков
    random.shuffle(rotor1)
    random.shuffle(rotor2)
    return {'rotor1': rotor1, 'rotor2': rotor2}


# Генерация ключа
key = generate_enigma_key()


def encrypt_one(char, key):
    # Шифрование одного символа
    return key['rotor2'][key['rotor1'].index(char)] if char in key['rotor1'] else char


def decrypt_one(char, key):
    # Расшифрование одного символа
    return key['rotor1'][key['rotor2'].index(char)] if char in key['rotor2'] else char


def encrypt(mesg, key):
    # Шифрование всего сообщения
    return ''.join(encrypt_one(char, key) for char in mesg)


def decrypt(encrypted_mesg, key):
    # Расшифрование всего сообщения
    return ''.join(decrypt_one(char, key) for char in encrypted_mesg)


def main():
    # Создание окна
    root = Tk()
    root.title("Enigma")
    root.geometry("300x250")

    # Вставка текстового поля для вывода результата
    result = ttk.Label(justify=CENTER, width=45, background="#D3D3D3")
    result.pack(anchor=N, pady=10)

    # Вывод зашифрованного сообщения
    def show_encrypted_mess():
        result["text"] = encrypt(entry.get(), key)

    # Вывод расшифрованного сообщения
    def show_decrypted_mess():
        result["text"] = decrypt(entry.get(), key)

    # Добавление текстового поля
    entry = ttk.Entry(justify=CENTER, width=45)
    entry.pack(anchor=N, pady=10)

    # Добавление кнопок
    button_encrypt = ttk.Button(text="Зашифровать", command=show_encrypted_mess)
    button_decrypt = ttk.Button(text="Расшифровать", command=show_decrypted_mess)
    button_encrypt.pack()
    button_decrypt.pack()

    root.mainloop()


def get_encryption_key():
    print(key)


# get_encryption_key()
main()
