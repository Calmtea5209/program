def fa(x):  #費式數列(遞迴)
    if (x<=2):
        return 1
    else: 
        return fa(x-1)+fa(x-2)
def fb(x):  #費式數列(迴圈)
    a=1
    b=0
    c=1
    for i in range(1,x+1,1):
        c=a+b
        a=b
        b=c
    return c
n=int(input("請輸入項數:"))
print (fb(n))
