#!/usr/bin/python3
'''
Лабораторная работа №1

Цель работы: изучение симплекс-метода решения
задачи линейного программирования

Вариант № 5 '''
from fractions import Fraction

global n, m #кол-во строк и столбцов


'''
чтение данных из файла
в первой строке записывается кол-во строк и столбцов
в последующих строках задается исходная симплекс-таблица
'''
def getData(): 
    mas = []
    n = 0
    m = 0
    with open('tab1.txt', 'r') as f:
        n, m = map(int, f.readline().strip().split())
        for i in range(4):
            mas.append(list(map(Fraction, f.readline().strip().split())))
    
    return mas, n, m


#проверяем F строку на положительные элементы
def checkF(mas):
    for i in range(m):
        if mas[n-1][i] > 0:
            return 0
    else:
        return 1


'''проверяем столбец свободных членов на
на отрицательные элементы'''
def checkS0(mas):
    for i in range(n-1):
        if mas[i][0] < 0:
            return i
    else:
        return -1


#нахождение разрешающей строки
def findRString(mas, col=-1):
    if col == -1:
        for i in range(n):
            if mas[i][0] < 0:
                return i
    else:
        mi = 10**5
        ind = 0
        for i in range(n-1):
            if mas[i][col] == 0:
                continue
            num = mas[i][0] / mas[i][col]
            if mi > num and num >= 0:
                mi = num
                ind = i
        return ind


#нахождение разрешающего столбца
def findRTable(mas, st=-1):

    if st != -1:
        for i in range(1, m):
            if mas[st][i] < 0:
                return i
    else:
        for i in range(1, m):
            if mas[n-1][i] > 0:
                return i


#пересчет симплекс-таблицы
def ChangeMas(mas, st, col):
    res = [[0]*m for i in range(n)]
    res[st][col] = 1 / mas[st][col]
    
    for i in range(n):
        if i != st:
            res[i][col] = (-1) * mas[i][col] / mas[st][col]

    for i in range(m):
        if i != col:
            res[st][i] = mas[st][i] / mas[st][col]

    for i in range(n):
        for j in range(m):
            if i != st and j != col:
                res[i][j] = mas[i][j] - (mas[st][j]*mas[i][col] / mas[st][col])

    return res



if __name__ == '__main__':

    SimpTab, n, m = getData()
    print(" первоначальная Симплекс-таблица\n")
   
    for i in SimpTab:
        print(*i)

    q = 0

    while not checkF(SimpTab):
        print('Итерация', q)
        
        f = checkS0(SimpTab)
        st = -1
        col = -1

        if f != -1:
            st = f
            col = findRTable(SimpTab, st)
        else:
            col = findRTable(SimpTab)
            st = findRString(SimpTab, col)

        print('Разрешающая строка = {} Разрешающий столбец = {}'.format(st+1, col+1))

        SimpTab = ChangeMas(SimpTab, st, col)

        print("Новая симплекс-таблица\n")

        for i in SimpTab:
            print(*i)
        q += 1
