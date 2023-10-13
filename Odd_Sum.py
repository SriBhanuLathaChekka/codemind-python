n=int(input())
nums=list(map(int,input().split()))
print(sum(filter(lambda x: x%2!=0,nums)))