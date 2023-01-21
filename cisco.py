 # rotten tomato
 class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		
		queue,counter = [],0
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if(grid[i][j] == 2):
		            queue.append([i,j])
		
		while(len(queue)>0):
		    counter+=1
    		for i in range(len(queue)):
    		    tempo = queue.pop(0)
    		    for i in [0,-1,1]:
    		        for j in [0,-1,1]:
    		            if(i == 0 or j == 0):
        		            drow = tempo[0]+i
        		            dcol = tempo[1]+j
        		            if(drow>=0 and dcol>=0 and drow<len(grid) and dcol<len(grid[0]) and grid[drow][dcol] ==  1):
        		                grid[drow][dcol] = 2
        		                queue.append([drow,dcol])
		    
		if(self.isnotAllRotten(grid)):
		    return -1
		return counter-1
		
		
	def isnotAllRotten(self,grid):
	    for i in grid:
	        for j in i:
	            if(j == 1):
	                return 1
	    return 0

------------------------------------------------------------------------------------

#Permutation of a given string...

#User function Template for python3
class Solution:
    def recurPermute(self,S,ds,ans,freq):
        if len(ds) == len(S):
            ans.append(''.join(ds.copy()))
        for i in range(len(S)):
            if freq[i] == False:
                freq[i] = True
                ds.append(S[i])
                self.recurPermute(S,ds,ans,freq)
                ds.remove(S[i])
                freq[i] = False
    def find_permutation(self, S):
        # Code here
        freq = [False] * len(S)
        ans = []
        self.recurPermute(S,[],ans,freq)
        res = []
        for i in ans:
            if i not in res:
                res.append(i)
        return sorted(res)        

------------------------------------------------------------------------------------

# MST 

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        
        parent = [-1]*V
        keys = [float("inf")]*V
        keys[0]=0
        mst = [False]*V
        
        
        for count in range(V-1):
            
            Min = 10e9
            ind = -1
            
            for e in range(V):
                if not mst[e] and keys[e]<Min:
                    Min = keys[e]
                    ind = e
            mst[ind] = True     
            
            for child in adj[ind]:
                v = child[0]
                weight = child[1]
                
                if not mst[v] and weight<keys[v]:
                    parent[v] = u
                    keys[v] = weight
                    
        return sum(keys)

------------------------------------------------------------------------------------
#Dijkstra

import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, v, adj, s):
        #code here
        heap=[]
        dist=[999999]*v
        heapq.heappush(heap,[0,s])
        dist[s]=0
        while(len(heap)!=0):
            top=heapq.heappop(heap)
            node=top[1]
            temp=top[0]
            for i in adj[node]:
                ver=i[0]
                path=i[1]
                if(dist[ver]>temp+path):
                    dist[ver]=temp+path
                    heapq.heappush(heap,[dist[ver],ver])
        return dist
------------------------------------------------------------------------------------
#Reverse a linkedList 
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        stack=[]
        curr=head
        while curr!=None:
            stack.append(curr.data)
            curr=curr.next

        curr=head
        while curr!=None:
            curr.data=stack.pop()
            curr=curr.next

        return head
------------------------------------------------------------------------------------
#number of 1 Bits 
def setBits(self, N):
		# code here
        k = bin(N).replace("0b","").replace("0","")
        return len(k)

------------------------------------------------------------------------------------
#class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):

        m=max(arr[:k])

        mxs=[m]

        for i in range(1,n-k+1):

            if arr[i+k-1]>m: m=arr[i+k-1]

            elif arr[i-1]==m: m=max(arr[i:i+k])

            mxs.append(m)

        return mxs
------------------------------------------------------------------------------------
#class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here

        if p == "":
            return -1

        countP, window = {}, {}
        for c in p:
            countP[c] = 1 + countP.get(c, 0)

        have, need = 0, len(countP)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countP and window[c] == countP[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countP and window[s[l]] < countP[s[l]]:
                    have -= 1
                l += 1
        l,r=res
        return s[l : r + 1] if resLen != float("infinity") else -1 
------------------------------------------------------------------------------------
#Check for Balanced Tree
class Solution:
    def Balanced(self, root):
        if root == None:
            return 0, True
        lh,isLeftBalanced = self.Balanced(root.left)
        rh, isRightBalanced = self.Balanced(root.right)
 
        h = 1 + max(lh,rh)
        if lh - rh >1 or rh - lh > 1:
            return h, False
        if isLeftBalanced and isRightBalanced:
            return h, True
        else:
            return h, False

    

    def isBalanced(self,root):     
    #add code here
        h, ans = self.Balanced(root)
        return ans

------------------------------------------------------------------------------------
 #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        dp = [-1]*(n+1)
        def ways(n):
            if n<0:
                return 0
            if n==0 or n==1:
                return 1
            
            if dp[n]!=-1:
                return dp[n]%(10**9 + 7)
            dp[n] =(ways(n-3)+ways(n-2)+ways(n-1))%(10**9 + 7)
            return dp[n]%(10**9 + 7)
            
        return ways(n)%(10**9 + 7)
------------------------------------------------------------------------------------
#Sum of Middle Elements of two sorted arrays

class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here 
        ar1.extend(ar2)
        ar1.sort()
        return ar1[n-1]+ar1[n]

------------------------------------------------------------------------------------

#second most occuring string
class Solution:

    def secFrequent(self, arr, n):
        l = []
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1 
            else:
                d[i]+=1 
        for i in d:
            l.append(d[i])
        m = max(l)
        l.remove(m)
        m1 = max(l)
        for i in d:
            if d[i] == m1:
                return i 


------------------------------------------------------------------------------------

# A Python program to sort a binary array

def sortBinaryArray(a, n):
	j = -1
	for i in range(n):

		# if number is smaller
		# than 1 then swap it
		# with j-th number
		if a[i] < 1:
			j = j + 1

			# swap
			a[i], a[j] = a[j], a[i]


# Driver code
if __name__ == "__main__":
	a = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1,
		1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
	n = len(a)

	# Function call
	sortBinaryArray(a, n)

	for i in range(n):
		print(a[i], end=" ")

# This code is contributed by Shrikant13.
------------------------------------------------------------------------------------
# find all lonely numbers

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        
        ans = []
        for x in nums:
            if counts[x] == 1 and x - 1 not in counts and x + 1 not in counts:
                ans.append(x)
        return ans

------------------------------------------------------------------------------------
#Classes and Objects
class Student {
    public:
        void input() {
            for (int i = 0; i < 5; i++) {
                int current_value;
                cin >> current_value;
                d_sum += current_value;
            }
        }
        int calculateTotalScore() {
            return d_sum;
        }
    private:
        int d_sum = 0;  
};
------------------------------------------------------------------------------------

# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced


def areBracketsBalanced(expr):
	stack = []

	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:

			# IF current character is not opening
			# bracket, then it must be closing.
			# So stack cannot be empty at this point.
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	# Check Empty Stack
	if stack:
		return False
	return True


# Driver Code
if __name__ == "__main__":
	expr = "{()}[]"

	# Function call
	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")

# This code is contributed by AnkitRai01 and improved
# by Raju Pitta
