class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Linedlist:
	def __init__(self):

		self.head = Node

	def listprint(self):
	        printval = self.head

	        while printval is not None:
	            print(printval.data)
	            if printval.data == printval.next:
	            	printval = printval.next.next
	            else:
	            	printval = printval.next


list1 = Linedlist()
list1.head = Node(1)
sencond = Node(1)
fifth  = Node(3)

list1.head.next = sencond
sencond.next = fifth

list1.listprint()