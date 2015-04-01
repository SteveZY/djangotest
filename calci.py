BBBBBB# -*- coding: utf-8 -*-
def chazh():
    i = 0
    while i < 100:
        if i%28 == 0 and i != 0: #i % 3==0 and (100-i)%4 ==0:
            if i  < 100:
                print 'Then possible cock num should be %d' % (i / 7)
        ():
i=i+28
def decf
#3x+4y=100 求解
    i = 0 
    while i < 100:

        if i %3 == 0 and (100 - i) % 4 == 0:
            print 'x=%d y = %d' % ((i / 3),(100 - i) /4)
        i = i + 1
#import math
def times(cash):
    n = 0
    while cash > 50000:
        cash = cash*0.95
        n = n +1
    return int(n + cash/5000)

def yangin20y():
    n = 1
    y=[1,0,0,0]
    while n <= 20:
        y[3] = y[2]
        y[2] = y[1]
        y[1] = y[0]
        y[0] = y[1] + y[3]
        n=n+1
    return sum(y)    

if __name__=="__main__":
#    chazh()
#    decfunc()
    print times(100000)
    print 'total sheep num is %d' % yangin20y()

