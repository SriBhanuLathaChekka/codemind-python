n=int(input())
nums=map(int,input().split())
s=0
print(sum(filter(lambda x: x%2==0,nums)))