# Python 3 program to find the minimum
# possible difference between maximum
# and minimum elements when we have to
# add / subtract every number by k


def getMinDiff(arr, n, k):

	if (n == 1):
		return 0
	arr.sort()
	ans = arr[n-1] - arr[0]

	small = arr[0] + k
	big = arr[n-1] - k
	
	if (small > big):
		small, big = big, small

	for i in range(1, n-1):
	
		subtract = arr[i] - k
		add = arr[i] + k

		if (subtract >= small or add <= big):
			continue
		if (big - subtract <= add - small):
			small = subtract
		else:
			big = add
	return min(ans, big - small)


# Driver function
arr = [ 4, 6 ]
n = len(arr)
k = 10

print("Maximum difference is", getMinDiff(arr, n, k))

# This code is contributed by
# Smitha Dinesh Semwal
