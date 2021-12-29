import random
import time
"""
0:石头
1:剪刀
2:布
"""
player1_win = 0
player2_win = 0
draw = 0
n = 0
start = time.time()
while n < 30000:
    n += 1
    player1 = random.randint(0, 2)
    player2 = random.randint(0, 2)
    if (player1 == 0):
        if (player2 == 0):
            draw += 1
            print("平局")
        elif (player2 == 1):
            player1_win += 1
            print("player1赢")
        else:
            player2_win += 1
            print("player2赢")
    elif (player1 == 1):
        if (player2 == 0):
            player2_win += 1
            print("player2赢")

        elif (player2 == 1):
            draw += 1
            print("平局")

        else:
            player1_win += 1
            print("player1赢")

    else:
        if (player2 == 0):
            player1_win += 1
            print("player1赢")

        elif (player2 == 1):
            player2_win += 1
            print("player2赢")
        else:
            draw += 1
            print("平局")

print("player1_win", player1_win)
print("player2_win", player2_win)
print("draw", draw)
end = time.time()

print("time:",end - start)