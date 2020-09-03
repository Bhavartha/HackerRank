n,k = list(map(int,input().split()))
bill = list(map(int,input().split()))
b = int(input())
s = sum(bill)-bill[k]
if b==s//2:
    print("Bon Appetit")
else:
    print(b - s//2)
