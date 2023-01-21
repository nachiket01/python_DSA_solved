def cy(n,arr,k):
    for i in range(n):
        if arr[i] == j:
            k = arr[i]
            arr[0],arr[i] = arr[i],arr[0]
    k+=1

    for i in range(1,k):
        arr[k],arr[i] = arr[i],arr[k]

arr = [1,2,3,3,1,3,5,6,3,2]
j = 5
n = len(arr)
k = None3
cy(n,arr,k)
print(arr)

