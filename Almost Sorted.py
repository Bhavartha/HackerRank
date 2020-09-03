_ = input()
arr = list(map(int,input().split()))
sarr = sorted(arr)
us=[]
if sarr==arr:
    print('yes')
else:
    for i in range(len(sarr)):
        if sarr[i]!=arr[i]:
            us.append(i)
    if len(us)==2:
        print(f"yes\nswap {us[0]+1} {us[-1]+1}")
    elif arr[us[0]:us[-1]+1] == sorted(arr[us[0]:us[-1]+1],reverse=True):
        print(f"yes\nreverse {us[0]+1} {us[-1]+1}")
    else:
        print("no")
