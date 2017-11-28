#!/usr/bin/python3

global n, m

def GetData():
  file = open("tab6.txt")
  n = 0; m = 0
  n, m = map(int, file.readline().strip().split())
  a = [list(map(int, file.readline().strip().split())) for i in range(n)]
  return a, n, m

def Bernulli(mas):
  su = []
  for i in mas:
    su.append(sum(i))

  ma = su[0]
  ind = 0
  for i in range(n):
    if su[i] > ma:
      ma = su[i]
      ind = i

  return ma/m, ind

def pessimist(mas):
  mi = []
  for i in mas:
    mi.append(min(i))

  ma = mi[0]
  ind = 0
  for i in range(n):
    if ma < mi[i]:
      ma = mi[i]
      ind = i
  return ma, ind

def optimist(mas):
  ma = []
  for i in mas:
    ma.append(max(i))
  mael = ma[0]
  ind = 0
  for i in range(n):
    if mael < ma[i]:
      mael = ma[i]
      ind = i
  return mael, ind

def Gurvic(mas, alpha):
  res = []
  for i in mas:
    el = alpha*min(i) + (1 - alpha)*max(i)
    res.append(el)
  ma = res[0]
  ind = 0
  for i in range(n):
    if ma < res[i]:
      ma = res[i]
      ind = i
  return ma, ind

def MaxStolb(mas, j):
  re = []
  for i in range(n):
    re.append(mas[i][j])
  return max(re)

def Sevidg(mas):
  r = [[0]*m for i in range(n)]
  for i in range(n):
    for j in range(m):
      r[i][j] = MaxStolb(mas, j) - mas[i][j]

  re = []
  for i in r:
    re.append(max(i))

  ind = 0
  mi = re[ind]
  for i in range(n):
    if mi > re[i]:
      mi = re[i]
      ind = i

  return r, mi, ind



if __name__ == '__main__':
  mas, n, m = GetData()
  print(mas)
  res = Bernulli(mas)
  print("Критерий Бернулли\n игра == {} Стратегия = {}".format(res[0], res[1]+1))

  res = pessimist(mas)
  print("Критерий Вальда\n игра == {} Стратегия = {}".format(res[0], res[1]+1))

  res = optimist(mas)
  print("Критерий максимума\n игра == {} Стратегия = {}".format(res[0], res[1]+1))

  res = Gurvic(mas, 0.5)
  print("Критерий Гурвица\n игра == {} Стратегия = {}".format(res[0], res[1]+1))

  re, mi, ind = Sevidg(mas)
  print("Критерий Севиджа\n игра == {} Стратегия = {}".format(mi, ind+1))
  for i in re:
    for j in i:
      print(j, end=" ")
    print()
