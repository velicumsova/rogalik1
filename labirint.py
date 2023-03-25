# код отвечающий за лабиринт и перемещение по ниму
from random import randint
from random import choice
import time
import os
import keyboard
def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')
keyboard.block_key('w')
keyboard.block_key('a')
keyboard.block_key('s')
keyboard.block_key('d')
#типы клеток:
#0 - нет комнаты
#1 - вход
#2 - выход
#3 - монстр
#4 - сундук
#5 - фонтан
#6 - торговец
#7 - коридор
#8 - стена
#9 - игрок


class Room:
    def init(self, x=None, y=None):
        self.idRoom = x
        self.typeRoom = y

    def print_info(self):  # вывод id и тип комнаты
        print(self.idRoom, self.typeRoom)

class RoomMonster(Room): #room with monster
    def __init__(self, plug, x, y):
        super().init(x, y)
        self.plug = plug

    def print_info(self):
        super().print_info()  # вызов метода родительского класса
        print(self.plug)

class RoomFountain(Room): #room fountain
    def __init__(self, health, x, y):  #
        super().init(x, y)
        self.health = health

    def print_info(self):
        super().print_info()
        print(self.health)

class RoomChest(Room):
    def __init__(self, money, items,  x, y):
        super().init(x, y)
        self.money = money
        self.items = items

    def print_info(self):
        super().print_info()  # вызов метода родительского класса
        print(self.money, '', self.items)

class Labyrinth(object):
    rooms_place = [[0, 0, 0, 0], [0, 0,0,0], [0, 0,0,0], [0,0, 0, 0]]
    walls = [[0 for j in range(144)] for i in range(60)]

    def generate(self):
        self.rooms_place = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.walls = [[0 for j in range(144)] for i in range(60)]
        rooms_num = randint(4, 7)
        #заполнение
        i = 0
        j = 0
        while (i<3 or j<3):
            ways=[]
            if i<3 and self.rooms_place[i+1][j]==0: #снизу
                ways.append(3)
            if j<3 and self.rooms_place[i][j+1]==0: #справа
                ways.append(2)
            if (len(ways)>0):
                chosenway=choice(ways)
                if(chosenway==2):
                    j+=1
                if(chosenway==3):
                    i+=1
            self.rooms_place[i][j]=1
        i = 0
        j = 0
        while (i<3 or j<3):
            ways=[]
            if i<3 and self.rooms_place[i+1][j]<2: #снизу
                ways.append(3)
            if j<3 and self.rooms_place[i][j+1]<2: #справа
                ways.append(2)
            if (len(ways)>0):
                chosenway=choice(ways)
                if(chosenway==2):
                    j+=1
                if(chosenway==3):
                    i+=1
            self.rooms_place[i][j]=1
        self.rooms_place[3][3] = 2
        self.rooms_place[0][1] = 6
        for i in range(4):
            for j in range(4):
                if self.rooms_place[i][j]==1:
                    if rooms_num>0:
                        self.rooms_place[i][j] = randint(3,6)
                        rooms_num=rooms_num-1
                    else:
                        self.rooms_place[i][j] = 7
        self.rooms_place[0][0]=1


        #перенос в двумерный массив
        for i in range(1, 62):
            for j in range(1, 146):
                #стороны:
                if (i==1 or i%15==0) and (1<j<144 and j%36!=0): #горизонтальные
                    if ((0 < self.rooms_place[(i-1) // 15][j // 36]) and (i<59 and 0 == self.rooms_place[(i+1) // 15][j // 36])) or ((0 == self.rooms_place[(i-1) // 15][j // 36]) and (i<59 and 0 < self.rooms_place[(i+1) // 15][j // 36])):
                        self.walls[i-1][j-1] = 8
                    elif (i==1 or i==60) and (i<60 and self.rooms_place[(i+1) // 15][j // 36] >0 or (i>1 and self.rooms_place[(i-1) // 15][j // 36] >0)):
                        self.walls[i-1][j-1] = 8
                    elif (1<i<60) and not(13<j<23 or 49<j<59 or 85<j<95 or 121<j<131) and ((0 < self.rooms_place[(i+1) // 15][j // 36] < 7) or (0 < self.rooms_place[(i-1) // 15][j // 36] < 7)):
                        self.walls[i-1][j-1] = 8
                    else:
                        self.walls[i - 1][j - 1] = 0
                elif (j==1 or j%36==0) and (1<i<60 and i%15!=0): #вертикальные
                    if ((0 < self.rooms_place[i // 15][(j - 1) // 36]) and (j<143 and 0 == self.rooms_place[i // 15][(j + 1) // 36])) or ((0 == self.rooms_place[i // 15][(j - 1) // 36]) and (j<143 and 0 < self.rooms_place[i // 15][(j + 1) // 36])):
                        self.walls[i-1][j-1] = 8
                    elif (j==1 or j==144) and (j<144 and self.rooms_place[i // 15][(j+1) // 36] >0 or (j>1 and self.rooms_place[i // 15][(j-1) // 36] >0)):
                        self.walls[i-1][j-1] = 8
                    elif (1<j<144) and not(6<i<10 or 21<i<25 or 36<i<40 or 51<i<55) and ((0 < self.rooms_place[i// 15][(j+1) // 36] < 7) or (0 < self.rooms_place[i // 15][(j-1) // 36] < 7)):
                        self.walls[i-1][j-1] = 8
                elif (1<i<60) and (1<j<144):
                    if self.rooms_place[i//15][j//36] == 1:
                        self.walls[i - 1][j - 1] = 1
                    elif self.rooms_place[i//15][j//36] == 2:
                        self.walls[i - 1][j - 1] = 2
                    elif self.rooms_place[i//15][j//36] == 3:
                        self.walls[i - 1][j - 1] = 3
                    elif self.rooms_place[i//15][j//36] == 4:
                        self.walls[i - 1][j - 1] = 4
                    elif self.rooms_place[i//15][j//36] == 5:
                        self.walls[i - 1][j - 1] = 5
                    elif self.rooms_place[i // 15][j // 36] == 6:
                        self.walls[i - 1][j - 1] = 6
            self.walls[0][0] = 8
            self.walls[2][2] = 9
            self.walls[59][143] = 8
            for i in range(60):
                for j in range(144):
                    if 0<i<59 and self.walls[i-1][j] == 8 and self.walls[i+1][j] == 8:
                        self.walls[i][j] = 8
                    elif 0<j<143 and self.walls[i][j+1] == 8 and self.walls[i][j-1] == 8:
                        self.walls[i][j] = 8

    def draw(self,x,y,count):
        clear_console()
        for i in range(60):
            for j in range(144):
                if self.walls[i][j] == 9:
                    print("\u001b[37;1m", end="")
                    print("&", end="")
                # elif self.walls[i][j] == 1:
                #     print("\u001b[48;5;232m", end="")
                #     print(" ", end="")
                #     print("\u001b[48;5;235m", end="")
                # elif self.walls[i][j] == 2:
                #     print("\u001b[48;5;232m", end="")
                #     print(" ", end="")
                #     print("\u001b[48;5;235m", end="")
                # elif self.walls[i][j] == 3:
                #     print("\u001b[48;5;52m", end="")
                #     print(" ", end="")
                #     print("\u001b[48;5;235m", end="")
                # elif self.walls[i][j] == 4:
                #     print("\u001b[48;5;94m", end="")
                #     print(" ", end="")
                #     print("\u001b[48;5;235m", end="")
                # elif self.walls[i][j] == 5:
                #     print("\u001b[48;5;63m", end="")
                #     print(" ", end="")
                #     print("\u001b[48;5;235m", end="")
                # elif self.walls[i][j] == 6:
                #     print("\u001b[48;5;28m", end="")
                #     print(" ", end="")
                #     print("\u001b[48;5;235m", end="")
                elif self.walls[i][j] == 8:
                    print("\u001b[48;5;136m", end="")
                    print(" ", end="")
                    print("\u001b[48;5;235m", end="")

                else:
                    print(" ", end="")
            print()
        print("Уровень: ", count)
        print("_____________________________")
        print("Комната " , "№" ,4*(x//15)+y//36+1, end="")
        if self.rooms_place[x//15][y//36]==1:
            print(", вход.", end="")
        elif self.rooms_place[x//15][y//36]==2:
            print(", выход.", end="")
        elif self.rooms_place[x//15][y//36]==3:
            print(", с монстром.", end="")
        elif self.rooms_place[x//15][y//36]==4:
            print(", с сундуком.", end="")
        elif self.rooms_place[x//15][y//36]==5:
            print(", с фонтаном.", end="")
        elif self.rooms_place[x//15][y//36]==6:
            print(", с торговцем.", end="")
        elif self.rooms_place[x//15][y//36]==7:
            print(", коридор.", end="")
        print(" *состояние*.")
        print("_____________________________")
        print("HP: ", )
        print("_____________________________")


def move(level, i, j):
    if keyboard.is_pressed('w'):
        if (level.walls[i-1][j] !=8):
            k=level.walls[i-1][j]
            level.walls[i - 1][j]=9
            level.walls[i][j]=k
            i -=1
    if keyboard.is_pressed('a'):
        if (level.walls[i][j-1] != 8):
            k = level.walls[i][j-1]
            level.walls[i][j-1] = 9
            level.walls[i][j] = k
            j -= 1
    if keyboard.is_pressed('s'):
        if (level.walls[i + 1][j] != 8):
            k = level.walls[i + 1][j]
            level.walls[i + 1][j] = 9
            level.walls[i][j] = k
            i += 1
    if keyboard.is_pressed('d'):
        if (level.walls[i][j+1] != 8):
            k = level.walls[i][j+1]
            level.walls[i][j+1] = 9
            level.walls[i][j] = k
            j += 1
    return level,i,j

level = Labyrinth()
count=1
while not(keyboard.is_pressed('ESCAPE')):
    i = 2
    j = 2
    level.generate()
    while not(keyboard.is_pressed('RETURN') and level.rooms_place[i//15][j//36]==2):
        time.sleep(0.001)
        level, i, j = move(level, i, j)
        level.draw(i,j,count)
    count+=1




