'''
class is a user defined data type:
	Objects are specific instances of a class:

class Phone:

	def set_color(self,color):
		self.color = color

	def set_cost(self,cost):
		self.cost = cost

	def show_color(self):
		return self.color

	def show_cost(self):
		return self.cost
	
	def make_call(self):
		print("making phone call")
	
	def play_game(self):
		print("playing the game ")

p = Phone()

p.make_call()
p.set_color("red")
p.set_cost(12)

print(p.show_cost())
print(p.show_color())

'''
''''
class Employee:

	def __init__(self,name,age,salary,gender):

		self.name = name
		self.age = age
		self.salary = salary
		self.gender = gender

	def employee_details(self):
		print(self.name)
		print(self.age)
		print(self.salary)
		print(self.gender)

p = Employee("nachiket",14,150000,'Male')

p.employee_details()

'''
'''
class Vehicle:
	def __init__(self,mileage,cost):
		self.mileage = mileage
		self.cost  = cost

	def show_details(self):
		print(self.cost,self.mileage)

class Car(Vehicle):
	def __init__(self,mileage,cost,tyres,HP):
		super().__init__(mileage,cost)
		self.tyres = tyres
		self.HP = HP


	def show_car(self):
		print("Honda civic")
		print(self.tyres,self.HP)


p = Car(24,400000,'mechlien',250)
p.show_details()
p.show_car()
'''
'''
class Parent1:
	def assing1(self,data):
		self.surname = data
	def show1(self):
		return self.surname

class Parent2:
	def assing2(self,data):
		self.Mother_name = data
	def show2(self):
		return self.Mother_name

class Child(Parent1,Parent2):
	def assing3(self,name):
		self.name = name

	def show3(self):
		return self.name

child = Child()

child.assing1("tekade")
child.assing2("Rameshwar")
child.assing3("Nachiket")

print(child.show1())
print(child.show2())
print(child.show3())
'''
'''
class Parent:

	def assing_last(self,last):
		self.last = last 

	def show_last(self):
		return self.last

class Child:
	
	def assing_middle(self,middle):
		self.middle = middle

	def show_middle(self):
		return self.middle

class GrandChild(Parent,Child):
	def assing_name(self,name):
		self.name = name

	def show_name(self):
		return self.name

child = GrandChild()
child.assing_name("Nachiket")
child.assing_middle("Rameshwar")
child.assing_last("Tekade")

print(child.show_name())
print(child.show_middle())
print(child.show_last())
'''
'''
class Car:
	def __str__(self):
		return f"this is a product object of company {self.company} and product_name is {self.product_name} "
	
	def __add__(self,car2):
		car3 = Car()
		car3.product_name = self.company
		car3.company = car2.company
		return car3

c1 = Car()
c1.company = "Tekade Industries & Co."
c1.product_name = "Kali-3"

c2 = Car()
c2.company = "Tekade Industries"
c2.product_name = "Kali-1"


c3 = c1 + c2
print(c3.__dict__)

'''
'''
class  Car(object):

	def __init__(self,company,product_name):
		self.company = company
		self.product_name = product_name

	def __str__(self):
		return f"company name : {self.company} and product_name : {self.product_name} "

c1 = Car("tekade industries","kali-3")
c2 = Car("tekade ind","kali")

print(c1,"\n",c2)
'''
'''

class Node:
	def __init__(self,data, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return f"node {self.data} --> {self.next}"



def print_link(head):
	while head:
		print(head.data)
		head = head.next

def count(head):
	c = 0
	while head:
		c+=1
		head = head.next

	print(f" there are {c} nodes")

def add_last(head,data):
	if not head:
		return Node(data)
	ptr = head

	while ptr.next:
		ptr = ptr.next
	ptr.next = Node(data) 
	return head

def insert_at_front(head,data):
	return Node(data,head)
 
a = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
#add_last(a,5)
#print_link(a)

def delete_at_any(head, pos):
	ptr = 0
	temp = head
	if pos == 1:
		head = head.next
		return head
	pos -=1 
	while temp:
		ptr +=1
		if ptr == pos:
			temp.next = temp.next.next		
			break
		temp =temp.next
			
	return head

def reverse(head):
	if not head or not head.next:
		return head
	p,c,n = head, head.next, head.next.next

	while n:
		c.next = p
		p = c
		c = n
		n = n.next
	head.next = None
	c.next = p
	return c 




#print(a)
#a = delete_at_any(a,4)
print(a)
#print_link(a)
a= reverse(a)
print(a)

'''
'''
class  Node(object):
	"""docstring for  Node"""
	def me(self, data, next = None):
		self.data = data
		self.next = next

	def __str__(self):
		return f'{self.data} --> {self.next}'

name = Node()
name.me("Name:")

first = Node()
first.me("Nachiket")
name.next = first

second = Node()
second.me("rameshwar")
first.next = second

third = Node()
third.me("Tekade")
second.next = third

fourth = Node()
fourth.me("khamgaon")
third.next = fourth

#print(name)

def middle(name):
	counter= 0
	temp = name

	while temp:
		counter +=1
		temp = temp.next	
	pos = int(counter / 2)
	ptr = 0
	temp2 = name

	while ptr < pos:
		ptr +=1
		temp2 = temp2.next
	temp2.next = None
	return temp2

#middle(name)

def del_middle(name):
	counter= 0
	temp = name

	while temp:
		counter +=1
		temp = temp.next

	pos = int(counter / 2)

	ptr = 0

	temp3 = name

	#print(temp3,"ss",name)

	while name:
		
		if pos == ptr:
			print(temp3,"afr",name)

			name.next = name.next.next
			break

		ptr +=1 
		name = name.next
	#print(temp3,name)

	return temp3

def del_by_val(name,a):
	if name is None:
		print("can't delete LL is empty")
	n= name
	while n.next is not None:
		if a == n.data:
			break
		n= n.next

	if n.next is None:
		print("not pres")
	else:
		n.next = n.next.next

	return name


print(del_by_val(name,"Nachiket"))
'''

'''
def solve(n, arr, x, y):
    # CODE HERE
	count = 0
	total = 0
	for i in range(x,y+1):
		count+=1
		total += arr[i]
		print(arr[i],total)
	print(total/count)


arr= [6,2,5,4,3,1]
n = 6
x = 2
y = 5
#solve(n,arr,x,y)


n= 6
k = str()
temp= str()
j = str()
def me(j,temp,n,k):
	for i in range(1,n):
		k = temp
		temp += str(i)
		j += temp+k[::-1] + " "
	
	return j
#print(me(j,temp,n,k))

'''
'''
parlg=[1,2,3,4,5]
lok = 5

for i in range(lok):
	if i%2== 0:
		parlg[i] = 0
print(parlg)



class sllnode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
        

    def __repr__(self):
        return "SllNode object: data = {}".format(self.data)   
    
    def get_data(self):
        #return the self.data attribute
        return self.data


    def set_data(self,new_data):
        #replace the exsiting value of the self.data attribute with new_data parameter
        self.data = new_data
        
    def get_next(self):
        #return the self.next attribute
        return self.next
        
    def set_next(self,new_next):
        #replace the exsiting value of the self.data attribute with new_next parameter
        
        self.next = new_next


    def get_previous(self):
        # return self.previous attribute
        return self.previous

    def set_previous(self,new_previous): 
        #replace the existing value of the self.previous attribute with new_previous parameter
        self.previous = new_previous

class sll:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "sll node obj: head = {}".format(self.hear)
    
    def is_empty(self):
        # Returns true if the linked list is empty
        return self.head is None 

    def add_front(self,new_data):
        # Add a node whose data is the new_data argument to the front of the linkedlist
         
        temp = sllnode(new_data)
        temp.set_next(self.head)
        self.head = temp
        
        
        
    def size(self):
        # Treverse the linkedlist and return an integer value representing the number of nodes in the linkedlist. the time complexity is 0(n) because every node in the linked list must visited in order to calculate the size of the linked list.
      
        size = 0
        if self.head is None:
            return 0
        
        current = self.head
        while current is not None: # while there are still nodes 
            size+=1
            current = current.get_next()
        
        return size


       
    
    def search(self,data):
# treverses the linked list and returns the true if the data searched for is present in one  of the Nodes . otherwise False.


        if self.head is None:
            return "Linked list is empty. No node to search "

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False



    def remove(self, data):
        # Removes the girst occurence of s node that contains the data argument as its self.data variable returns
        if self.head is None:
            return "the linked list is no nodes to remove"
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A node with that data value is not present"
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())




a= {1,2,3,1,1,1,1}
i= iter(a)
print(next(i,"chutya sample na "))
print(next(i,"chutya sample na "))
print(next(i,"chutya sample na "))
print(next(i,"chutya sample na "))


mat = [[2,35],[1,35],[3,40],[4,35],[6,40],[5,35]]
second_high = 0
first_high = 0
ls = []
for i in range(len(mat)):
    if mat[i][1] >= first_high:
        first_high = mat[i][1]
    elif second_high < first_high:
        second_high = mat[i][1]
        break
for i in range(len(mat)):
    if mat[i][1] == second_high:
        ls.append(mat[i][0])
ls.sort()
print(ls)
'''
'''

def fun(n):
    if n == 0 or n ==1:
        return n
    else:
        f1 = fun(n-1)
        f2 = fun(n-2)
        ans = f1 + f2 
        return ans


def f(ans,n,temp):
    if n == 0 or n == 1:
        return n
    else:
        ans = ans * n
    
    f(ans,n-1,temp)
    temp.append(ans)
    return temp[0]

n = 7
ans = 1
temp = []
print(f(ans,n,temp))
'''

position = 2
value = 7
arr = [1,2,3,4,5,6]
temp = []

if position == 0:
	position = 0
else:
	position -= 1

for i in range(len(arr)):
	if (position) == i:
		temp.append(value)
		temp.append(arr[i])

	else:
		temp.append(arr[i])

print(temp)