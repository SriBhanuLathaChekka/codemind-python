n=int(input())
if n%2==1:
    print("weird")
elif n in range(2,5):
    print("not weird")
elif n in range(6,20):
    print("weird")
else:
    print("not weird")