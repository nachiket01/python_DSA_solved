'''
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

'''
'''
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