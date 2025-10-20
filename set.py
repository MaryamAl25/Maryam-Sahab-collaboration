#Creating a Set {}

'''
The elements can be of different types {integer, float, tuple, string etc.}
'''

numberSet = {1,2,3,4,3,2}
print(numberSet)

#creating an empty set
emptySet = {} #this create a dictionary
print(type(emptySet))

emptySet = set() #This create a empty set
print(type(emptySet))
#set can contain elements of different type
my_set = {1.0,"hello", (1,2,3)}
print(my_set)

#We can convert a list to set using set function
set_with_lists = set([1,2,3])
print(type(set_with_lists))
print(set_with_lists)

###############################################33
#Set Operations
A = {1,2,3,4}
B = {2,4,6,8,6,6}

print("A=",A)
print("B=",B)
s1 = A | B #elements in a or b or both
print("Union: A | B = ",s1) #No repeted elements
s2 = A & B #elements in a and b or both
print("Union: A & B = ",s2) #No repeted elements
s3 = A - B   # elements in a but not in b
print("Difference: A - B =",s3)
s4 = A ^ B   # elements in a or b but not both
print("Symmetric Diff: A ^ B =",s4)

#########################################################
'''
Adding elements to a set
'''
mySet = set()
mySet.update([9,12])
mySet.update([3,5])
mySet.update("SIKANDER")

print(mySet)

#########################################################

mySet.update(("India","Bharart"))
print(mySet)

#########################################################

L = [1,3,2,6,4]
ll = [x*10 for x in L]
print(ll)#[10, 30, 20, 60, 40]
ss = {x*10 for x in L}
print(ss)#{40, 10, 20, 60, 30}
L.extend([1,2])
print(L)#[1, 3, 2, 6, 4, 1, 2]
ss = {x*10 for x in L}
print(ss)#{40, 10, 20, 60, 30}

##########################################################
a = {1,2,3}
b = {x*2 for x in a|{4,5}}
print(b)
print(type(b))
