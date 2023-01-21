'''
import math

def preprocess(p, x, y, n):
	for i in range(n):
		p[i] = x[i] * x[i] + y[i] * y[i]

	p.sort()
	print(p)
# Return count of points lie inside
# or on circumference of circle using
# binary search on p[0..n-1]

def query(p, n, rad):

	start = 0
	end = n - 1
	while ((end - start) > 1):
		mid = (start + end) // 2
		tp = math.sqrt(p[mid])
		print(tp,start,mid,end)
		if (tp > (rad * 1.0)):
			end = mid - 1
		else:
			start = mid


	tp1 = math.sqrt(p[start])
	tp2 = math.sqrt(p[end])

	if (tp1 > (rad * 1.0)):
		return 0
	elif (tp2 <= (rad * 1.0)):
		return end + 1
	else:
		return start + 1

# Driver Code
if __name__ == "__main__":
	
	x = [1,2,8,9]
	y = [0,-7,1,-6]
	n = len(x)

	# Compute distances of all points and keep
	# the distances sorted so that query can
	# work in O(logn) using Binary Search.
	p = [0] * n
	preprocess(p, x, y, n)

	# Print number of points in a
	# circle of radius 4.
	print(query(p, n, 4))


b1 = [[7,11],[12,11],[7,5],[12,5]]
b2 = [[5,12],[8,12],[5,9],[8,9]]

b1_max= max(b1)
b2_min = min(b2)
intersectional_down_point = []
intersectional_up_point= []

#print(b1_max,b2_min)
if b2_min[0] < b1_max[0]:
	diff = b1_max[0] - b2_min[0] 
	intersectional_down_point.append(b1[len(b1)-1][0] -diff)
	intersectional_down_point.append(b1[len(b1)-1][1])

	intersectional_up_point.append(b1_max[0])
	intersectional_up_point.append(b1_max[1]-diff)
else:
	diff = b2_min[0] - b1_max[0]
	intersectional_down_point.append(b1[0][0] -diff)
	intersectional_down_point.append(b1[0][1])

	intersectional_up_point.append(b1_max[0])
	intersectional_up_point.append(b1_max[1]-diff)

print(intersectional_down_point) 
print(intersectional_up_point) 
'''
class me:

	def se(self,a):
		self.a = a
		print(self.a,"why it is so tensed")

me = me()

print(me.se(45))
