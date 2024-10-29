import random
fl = False
print("Количиство камней в начале игры = ")
n = random.randint(4, 30)
print(n)
while n > 1:
    try:
        if n >= 3:
            hod_player = int(input("введите число от 1 до 3: "))
        else:
            fl = True
            hod_player = int(input("введите число от 1 до 2: "))
    except ValueError:
        print("Некорректные данные ")
    else:
        if (hod_player<1 or hod_player>3) and fl == False:
            print("Вы можете брать только 1 или 2 или 3 камня за раз")
        elif fl == True and (hod_player <1 or hod_player>2):
            print("Вы пожете брать только 1 или 2 камня")
        else:
            if n >= 2:
                n -= hod_player
                if n == 0:
                    print("компьютер победил")
                    break
                elif n == 1:
                    print("победил пользователь")
                    break
            elif n == 0:
                print("компьютер победил")
                break
            elif n == 1:
                print("победил пользователь")
                break
            print(f"количество камней = {n}")
            print("Ход за компьютером")
            if n >= 3:
                hod_pc = random.randint(1,3)
                n -= hod_pc
                if n == 0:
                    print("победил пользователь")
                    break
                elif n == 1:
                    print("победил компбютер")
                    break
            elif n == 1:
                print("победил компьютер")
                break
            elif n == 2:
                hod_pc = random.randint(1, 2)
                n -= hod_pc
                if n == 0:
                    print("победил пользователь")
                    break
                elif n == 1:
                    print("победил компбютер")
                    break
            elif n == 0:
                print("победил пользователь")
                break
            print(f"компьютер взял {hod_pc} камня, осталось {n}")

