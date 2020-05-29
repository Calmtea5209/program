l=[2,9,6,85,32,65,94,5,5,49,23,2,0]
for i in range(0,len(l)):
    for k in range(len(l)-1,0,-1):
        if l[k]<l[k-1]:
            l[k],l[k-1] =l[k-1],l[k]
print(l)            
    


    
    
