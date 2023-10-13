n=int(input())
a=list(map(int,input().split()))
s=0
f=0
for i in range(0,n,2):
    s=s+a[i]
for i in range(1,n,2):
    f=f+a[i]
print(abs(s-f))