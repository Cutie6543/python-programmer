n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    c=i
    for j in range(1, i+1):
         print(c,' ',sep=' ',end=" ")
     print()
o/p:- 1   
      2   2   
    3   3   3   
  4   4   4   4   
5   5   5   5   5   