#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import random

def round_up(value,decimal=2):
    """
    替换内置round函数,实现保留2位小数的精确四舍五入
    """
    return round(value * 10**decimal ) / (1.0*10**decimal)

def random_price(low,high,decimal=2):
    """
    获取low-high之前的随机浮点数，保留decimal位小数，四舍五入
    """
    return round_up(random.uniform(low,high),decimal)

def limit_price(price,rate=0.10):
    """
    获取涨停和跌停价格，保留2位小数，四舍五入
    """
    return round_up(price*(1.0 + rate),2),round_up(price*(1.0-rate),2)

class Randomkdata:
    def __init__(self,price,trand=0,rate=0.1):
        self.open = 1
        self.close = 2
        self.now = 2
        self.high = 3
        self.low =4
        self.rate = rate
        self.limit = self.get_limit(price)
    
    def set_rate(self,rate=0.1):
        self.rate = rate
    
    def get_limit(self,price):
        return round_up(price*(1.0 + self.rate),2),round_up(price*(1.0-self.rate),2)
    
    def set_trand(trand=0):
        k = random(0,1)
        if trand>0:
            pass
        elif trand<0:
            k = -1*k
        else:
            pass
        return k
    
    def get_random_price(self,price):
        print(self.limit[0])
        v = random.uniform(price,self.limit[0])
        print('v=',v)
        return round_up(v,2)
   
price = 4.23
price = 13.25
price = 11.65
price = 2.82
price = 3.46
print(round_up(price,4))
rate = 0.1
a = price*(1+rate)
print(a)
print(round_up(a))
rk = Randomkdata(price=price,trand=0,rate=0.1)
print(rk.get_limit(price))

print(rk.get_random_price(price))

