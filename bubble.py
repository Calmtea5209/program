b=input("請輸入欲排序數字，用空格分隔:")
l=b.split(" ")
l=list(map(int,l))
for i in range(0,len(l)-1):
    for k in range(len(l)-1,i,-1):
        if l[k]<l[k-1]:
            l[k],l[k-1] =l[k-1],l[k]
for i in range(0,len(l)):
    print(l[i]," ",end="")