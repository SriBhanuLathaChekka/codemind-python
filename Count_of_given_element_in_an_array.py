n=int(input())
nums=list(map(int,input().split()))
num=int(input())
c=0
for i in range(0,n):
    if(nums[i]==num):
        c+=1
print(c)
