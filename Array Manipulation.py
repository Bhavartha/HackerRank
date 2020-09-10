n,q = list(map(int,input().split()))
arr = [0]*(n+1)

for _ in range(q):
    start,end,value = list(map(int,input().split()))
    arr[start-1]+=value
    arr[end]-=value

mx = arr[0]
prev = 0
for i in range(n):
    prev += arr[i]
    mx = max(mx,prev)

print(mx)
