n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=' ')
    for j in range(1,i+1):
         print(j,end='  ')
    print()
o/p:-  1  
      1  2  
    1  2  3  
  1  2  3  4  
1  2  3  4  5  