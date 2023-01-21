#move all elements to negative side of array
arr = [1,-2,-2,2,4,1,-5,-4,-8,-9,55,63]
j = []
k = []
for i in range(len(arr)):
    if arr[i]< 0:
        j.append(arr[i])
    elif arr[i]>0:
        k.append(arr[i])

h = len(k)
h -=1
for i in range(h):
    j.append(k[i])
print(j)
