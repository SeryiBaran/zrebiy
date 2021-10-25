import random

COL = 400

def zsh(x):
    rfv = []
    for i in range(x):
        rrdint = random.randint(0, 3)
        rfv.append(rrdint)
    return rfv

def sort_rfv():
    global oned, twod, d3, d4
    oned = 0
    twod = 0
    d3 = 0
    d4 = 0
    for i in range(len(out_zsh)):
        if out_zsh[i] == 0:
            oned += 1
        elif out_zsh[i] == 1:
            twod += 1
        elif out_zsh[i] == 2:
            d3 += 1
        elif out_zsh[i] == 3:
            d4 += 1

out_zsh = zsh(COL)
out_sort_rfv = sort_rfv()
users = {}
users.fromkeys([oned, twod, d3, d4], ["0", "1", "2", "3"])
users[oned] = "0"
users[twod] = "1"
users[d3] = "2"
users[d4] = "3"
users_list = [oned, twod, d3, d4]
users_list.sort()
winner_num = users_list[-1]
winner = users[winner_num]
if oned == twod or oned == d3 or oned == d4 or twod == oned or twod == d3 or twod == d4 or d3 == oned or d3 == twod or d3 == d4 or d4 == oned or d4 == twod or d4 == d3:
    winner = "Ошибка/ничья!"
for i in out_zsh:
    print(i)
print("Итого:")
print(f"Пользователь 0 набрал: {oned}")
print(f"Пользователь 1 набрал: {twod}")
print(f"Пользователь 2 набрал: {d3}")
print(f"Пользователь 3 набрал: {d4}")
print(f"Победил: {winner}")
