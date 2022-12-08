import random

lower_case = "abcdefghijklmnopqrstuvwxyz"

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number = "0123456789"

symbols = "#@=$?*/%+-"

total = lower_case + upper_case + number + symbols

lgn = int (input ("Votre Longueur : "))

longeur = lgn

password = "".join(random.sample(total, longeur))

print("Votre mot de passe GitHub est : " + password)

bien = "Si ce script vous à été pratique n'hésitez pas à le partager à vos amis."

input('\n' + bien)

input('\nAppuyer sur entrée ...')