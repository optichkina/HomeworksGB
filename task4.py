#. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

low_a = ord('a')
low_z = ord('z')

k = input("Введите первый символ от 'a' до 'z': ")
j = input("Введите второй символ от 'a' до 'z': ")

code_k = ord(k)
code_j = ord(j)

if (code_k < code_j
        and low_a <= code_k <= low_z
        and low_a <= code_j <= low_z):
    poz_k = code_k - low_a + 1
    poz_j = code_j - low_a + 1
    print(f"Позиция '{k}' = {poz_k}, позиция '{j}' = {poz_j}, букв между ними: {poz_j - poz_k - 1}")
else:
    print("Неверный ввод")