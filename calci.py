# -*- coding: utf-8 -*-
def chazh():
    i = 0
    while i < 100:
        if i%28 == 0 and i != 0: #i % 3==0 and (100-i)%4 ==0:
            if i  < 100:
                print 'Then possible cock num should be %d' % (i / 7)
        i=i+28
def decfunc(): 
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

if __name__=="__main__":
#    chazh()
#    decfunc()
    print times(100000)


