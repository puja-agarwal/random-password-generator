

import tkinter as tk  # for gui
from functools import partial
import random  # to choose a random character
import pyperclip  # to copy the password to clipboard


def generator(x):
    # defining a variable with all the available character
    available_characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    # length of password
    lengthinput = x
    pa = ""

    # choosing random characters(number of characters that will be used for password=lengthinput) from available_characters
    for i in range(int(lengthinput)):
        password = "".join(random.choices(available_characters))
        pa = pa + password
    print("\nThis Password Generator is developed by Puja Agarwal\nTHANK YOU")

    u = copy1(pa)
    return pa


def call_result(label_result, n1):
    num1 = (n1.get())
    result = generator(num1)
    label_result.config(text="Password : %s" % result)
    return


def copy1(a):
    buttonCopy = tk.Button(root, text="Copy").grid(row=6, column=0)
    pyperclip.copy(a)
    labelNum8 = tk.Label(root, text="'Password Copied to Clipboard'").grid(row=7, column=0)
    labelNum8 = tk.Label(root, text="Developed by Students of C V Raman College of Engineering").grid(row=30, column=1)


root = tk.Tk()
root.geometry('700x200')

root.title('Password Generator')

number1 = tk.StringVar()

labelNum1 = tk.Label(root, text="Enter Password Length in numbers").grid(row=1, column=0)

labelResult = tk.Label(root)

labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=1)

call_result = partial(call_result, labelResult, number1)

buttonCal = tk.Button(root, text="Generate Password", command=call_result).grid(row=3, column=1)

root.mainloop()


def generatePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = []

    for i in pwlength:

        password = ""
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)

        passwords.append(password)

    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
        return pword


def main():
    numPasswords = int(input("How many passwords do you want to generate? "))

    print("Generating " + str(numPasswords) + " passwords")

    passwordLengths = []

    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        passwordLengths.append(length)

    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print("Password #" + str(i + 1) + " = " + Password[i])


main()
