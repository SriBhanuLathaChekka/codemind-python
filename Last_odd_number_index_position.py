n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(len(a)):
    if a[i]%2!=0:
        b=i
    
print(b)