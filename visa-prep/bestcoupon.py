bill=int(input().strip())
tenoff= bill*0.10
hunoff= 100
md=max(tenoff,hunoff)
topay=bill-md
print(int(topay))
