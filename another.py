def yangin20y():
    n = 1
    y=[1,0,0,0]
    while n <= 20:
        y[3] = y[2]
        y[2] = y[1]
        y[1] = y[0]
        y[0] = y[1] + y[3]
        n=n+1
        print y
    return sum(y)    

if __name__=="__main__":
#    chazh()
#    decfunc()
#    print times(100000)
    print 'total sheep num is %d' % yangin20y()

