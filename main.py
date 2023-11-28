# -*- coding: cp1251 -*-
import random
from tkinter import *
from tkinter import ttk


def generate_enigma_key():
    # ��������� ���������� �����
    rotor1 = list("0123456789�������������������������������� ")
    rotor2 = list("0123456789�������������������������������� ");

    # ������������� ��������� �������
    random.shuffle(rotor1)
    random.shuffle(rotor2)
    return {'rotor1': rotor1, 'rotor2': rotor2}


# ��������� �����
key = generate_enigma_key()


def encrypt_one(char, key):
    # ���������� ������ �������
    return key['rotor2'][key['rotor1'].index(char)] if char in key['rotor1'] else char


def decrypt_one(char, key):
    # ������������� ������ �������
    return key['rotor1'][key['rotor2'].index(char)] if char in key['rotor2'] else char


def encrypt(mesg, key):
    # ���������� ����� ���������
    return ''.join(encrypt_one(char, key) for char in mesg)


def decrypt(encrypted_mesg, key):
    # ������������� ����� ���������
    return ''.join(decrypt_one(char, key) for char in encrypted_mesg)


def main():
    # �������� ����
    root = Tk()
    root.title("Enigma")
    root.geometry("300x250")

    # ������� ���������� ���� ��� ������ ����������
    result = ttk.Label(justify=CENTER, width=45, background="#D3D3D3")
    result.pack(anchor=N, pady=10)

    # ����� �������������� ���������
    def show_encrypted_mess():
        result["text"] = encrypt(entry.get(), key)

    # ����� ��������������� ���������
    def show_decrypted_mess():
        result["text"] = decrypt(entry.get(), key)

    # ���������� ���������� ����
    entry = ttk.Entry(justify=CENTER, width=45)
    entry.pack(anchor=N, pady=10)

    # ���������� ������
    button_encrypt = ttk.Button(text="�����������", command=show_encrypted_mess)
    button_decrypt = ttk.Button(text="������������", command=show_decrypted_mess)
    button_encrypt.pack()
    button_decrypt.pack()

    root.mainloop()


def get_encryption_key():
    print(key)


# get_encryption_key()
main()
