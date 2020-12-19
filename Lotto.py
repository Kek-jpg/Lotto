
import random

N = int(input("Введите N: "))
pulled_out_barrels = []

while len(pulled_out_barrels) < N:
    barrel = random.randint(1, N)
    if barrel not in pulled_out_barrels:
        pulled_out_barrels.append(barrel)
        tap = str(input("Введите что угодно и получите случайный бочонок ! "))
        print("Вытащен бочонок номер " + str(barrel) + " !")
print("Бочонки кончились, жеребьёвка завершена !")