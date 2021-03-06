#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import random

def round_up(value,decimal=2):
    """
    替换内置round函数,实现保留2位小数的精确四舍五入
    """
    return round(value * 10**decimal ) / (1.0*10**decimal)


def limit_price(price,rate=0.10,decimal=2,rate_down=None):
    """
    获取涨停和跌停价格，保留2位小数，四舍五入
    :param price: float, last close price
    :param rate: float, limit rate
    :param decimal: int, decimal digit 
    :param rate_down: float,  lower rate, default is None
    :return highest,lowest, float
    """
    ratedown = -1 * rate 
    if rate_down!=None:
        ratedown = rate_down
    if rate<ratedown: #rate 为rate和ratedown中的最大者
        a = rate
        rate = ratedown
        ratedown = a
    return round_up(price*(1.0 + rate),decimal),round_up(price*(1.0+ratedown),decimal)

def random_price(low,high,decimal=2):
    """
    获取low-high之前的随机浮点数，保留decimal位小数，四舍五入
    """
    return round_up(random.uniform(low,high),decimal)

def randomnormal_price(mean,delta,decimal=2,uplimit=None,downlimit=None):
    """
    获取mean,delta之前的随机正态分布浮点数，保留decimal位小数，四舍五入
    正态分布: 在横轴区间（μ-σ,μ+σ）内的面道积为68.268949%，
    横轴区间（μ-1.96σ,μ+1.96σ）内的面积为95.449974%，
    横轴区间（μ-2.58σ,μ+2.58σ）内的面积为99.730020%。
    """
    rv = round_up(random.normalvariate(mean,delta),decimal)
    if uplimit!=None:
        if downlimit!=None:
            uplimit = max(uplimit,downlimit)
            downlimit = min(uplimit,downlimit)
        if rv > uplimit:
            return uplimit
        elif rv< downlimit:
            return downlimit
        else:
            pass
    else:
        if downlimit!=None:
            if rv <downlimit:
                return downlimit
    return rv

def random_rate_price(price,rate=0.10,decimal=2,rate_down=None):
    high,low = limit_price(price, rate, decimal, rate_down)
    return random_price(low, high, decimal)

class Ztrend:
    def __init__(self):
        base_type = [-2,-1,0,1,2] #0--横盘，1-震荡向上，2-单边上涨，-1-震荡向下，-2-单边下跌
        trend_type = [1,0,-2,0,-1,0,1,0,2,-1]
        self.trend = random.choice(trend_type)
    
    def trend_rate(self,price):
        rates = {
            -2:(-0.1,-0.015),
            -1:(-0.04,0.015),
            0:(-0.02,0.02),
            1:(-0.015,0.04),
            2:(0.015,0.1),
            }
        print(rates[self.trend])
        return random_rate_price(price,rate=rates[self.trend][1],decimal=2,rate_down=rates[self.trend][0])
        
class Randomkdata:
    def __init__(self,price,trand=0,rate=0.1):
        self.last = price
        self.limit = limit_price(price,rate,decimal=2)
        self.high = random_price(self.limit[1], self.limit[0], decimal=2)
        self.low = random_price(self.limit[1], self.limit[0], decimal=2)
        if self.high< self.low:
            a = self.high
            self.high = self.low
            self.low = a
        self.open = random_price(self.low, self.high, decimal=2)#limit_price(price,rate=0.03,decimal=2,rate_down=-0.02)
        #self.open = random_rate_price(price,rate=0.03,decimal=2,rate_down=-0.02)
        self.close = random_price(self.low, self.high, decimal=2)
        self.volume = 100
        self.ratio = round_up((self.close/price - 1.0)*100, decimal=2)
        
    def to_dict(self):
        return {'open':self.open,'close':self.close,'high':self.high,'low':self.low,'volume':self.volume,'last':self.last,'ratio':self.ratio}
        
    def set_rate(self,rate=0.1):
        self.rate = rate
    
    def get_limit(self,price):
        return limit_price(price, rate, decimal=2)
    
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
rate = 0.1
price = 10.0

h,l = limit_price(price, rate, decimal=2, rate_down=-0.02)
print(h,l)
print(round_up(price,4))

a = price*(1+rate)
print(a)
print(round_up(a))
rk = Randomkdata(price=price,trand=0,rate=0.1)
print(rk.get_limit(price))

print(rk.get_random_price(price))
print('Kdata: ')
print(rk.high)
print(rk.low)
print(rk.open)
print(rk.close)
print(rk.ratio)

print(rk.to_dict())

zt = Ztrend()
print(zt.trend)
#print(zt.trend_rate(price))