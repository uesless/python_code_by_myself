# coding=utf-8
# python2.7
# 16-10-20
# 16-11-02更新
# 姓名pk，纯属娱乐…

import random

def boomhp(a, b, c, d): #返回随机值，ab区间为普通攻击，cd区间为暴击
  temp = random.randint(1, 10)#检测暴击，有大概1/10的几率是暴击
  if temp > 1:
    hp = random.randint(a, b)
    return hp
  else:
    boo = random.randint(c, d)
    return boo

def pk(namea, nameb): #程序主体
  hpa = hpb = 1000 #初始生命值各为1000
  while True:
    temp1 = boomhp(1, 101, 101, 2000)
    hpa -= temp1
    if temp1 > 71:
      temp2 = '被暴击损失'
    else:
      temp2 = '损失'
    print namea, '出刀', nameb, temp2, temp1, '还剩', hpa
    hp = random.randint(1, 101)
    temp1 = boomhp(1, 101, 101, 2000)
    hpb -= temp1
    if temp1 > 71:
      temp2 = '被暴击损失'
    else:
      temp2 = '损失'
    print nameb, '出刀', namea, temp2, temp1, '还剩', hpb
    if hpa < 0:
      print namea + '无敌啦'
      break
    elif hpb < 0:
      print nameb + '赢得比赛'
      break

pk(raw_input('选手一叫啥名 ：'), raw_input('选手二叫啥名 ：'))
