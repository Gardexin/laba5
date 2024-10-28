import re

def useless_function():
    print("useless text")

fl = False
while fl == False:
    user_input = input("Введите оклад: ")
    if re.fullmatch(r"(\d+)", user_input):
        oklad = int(user_input)
        fl = True
    elif re.fullmatch(r"(\d+\.\d+)", user_input):
        oklad = float(user_input)
        fl = True
    else:
        print('Оклад должен быть положительным числом')

kvartal_premia = oklad * 2/3
summa_na_ruki = kvartal_premia * 0.87
print(f'сумма на руки = {summa_na_ruki}, kvartal_premia = {kvartal_premia}')
