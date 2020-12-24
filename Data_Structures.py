#------------------------------------------------The Class Implementation of Stack ----------------------------------------#
class Stack:
	def __init__(self):
		#initialing an empty list to insert the new data/nodes/values !
		self.the_data_list=[]
	#In Stack, the push fucntion is used to append data at the end of the list, so that it follows the LIFO(Last In First Out) principle !
	def push(self,value):
		#appends/adds the data at the end of the list !
		self.the_data_list.append(value)
	def pop(self):
		if len(self.the_data_list) == 0:
			print('Stackunderflow !!')
		else:
			#Removes the lates element from the list !
			return self.the_data_list.pop(-1)
	#returns the size/number of elements in the stack !
	def count(self):
		return len(self.the_data_list)
	#returns true if the value is in the list/stack !
	def contains(self,value):
		return value in self.the_data_list
	#returns the latest/top elements without removing it !
	def peek(self):
		print(self.the_data_list[-1])
#------------------------End of Class Implementation of Stack-------------------------------#


#--------------------------Start of Class Implementation of Queue-----------------------------------------#
class Queue:
	def __init__(self):
		#The Queue elements will be stored in the List !
		self.the_queue_list=[]
	def enqueue(self,value):
		self.the_queue_list.append(value)
	def dequeue(self):
		if len(self.the_queue_list)==0:
			print('Queue underflow !')
		else:
			#removing the first element/front of the queue !
			return self.the_queue_list.pop(0)
	def contains(self,value):
		return value in self.the_queue_list
	
	def traverse(self):
		for value in self.the_queue_list:
			print(value,end=' ')
		print(' ')

#--------------------------End of Class Implementation of Queue-----------------------------------------#

#--------------Implemenatation of Linked List -----------------------------------#
#the Linked List has nods which are connected to which next node(Node has data and Next part )
#Node(data,next)->Node(data,next)->Node(data,next)->null
class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class Linked_List:
	def __init__(self):
		self.head=None
# A data elmeent is added at the end of the linke list !
	def append(self,data):
		if self.head is None:
			self.head=Node(data)
		else:
			#if the head varibale is not None, then the current node is updated each time by the next node and the new node is added at the end !
			current_node=self.head
			while current_node.next!=None:
				current_node=current_node.next
			current_node.next=Node(data)
#The Linked is traversed till the end and counter variable initialized at zero is increased at each iteration !
	def count(self):
		counter=0
		current_node=self.head
		while current_node is not None:
			current_node=current_node.next
			counter+=1
		return counter
	#We traverse the linked list till we encounter a null value !
	def display(self):
		current_node=self.head
		while current_node is not None:
			print(f'{current_node.data}->',end=' ')
			current_node=current_node.next
		print(' ')
		#the list is checked whether the head is present or not if yes the list is not empty, otherwise the next successor of the head is choosen, 
	def delete(self,value):
		if self.head is None:
			print('Empty List !')
			return 
		if self.head.data==value:
			self.head=self.head.next
			return 
		#if the next node data value of the list is equal to the given value then the while loop is broken, and the next node of the current node is taken as the previous node the updated next node is next of the next node !
		current_node=self.head
		while current_node.next is not None:
			if current_node.next.data==value:
				break
			current_node=current_node.next
		if current_node.next is None:
			print('Node not here !')
		else:
			current_node.next=current_node.next.next
			#The List is traversed throughout the length and in each iteration the node data is compared if the given data matched the node data, if yes true is returned else false !
	def search(self,value):
		current_node=self.head
		flag=False
		while current_node is not None:
			if current_node.data==value:
				flag=True
				break
			current_node=current_node.next
		return flag
#End of Linked List------------------------------------------#

#------------------begining of BST------------------------#
#The below node is for Binary Search Tree, it has left and right pointer(s)
#In a binary search tree the left child must be less than the root node and the right child must be greater than the root node and so on !
class BSTNode:
	def __init__(self,data=None):
		self.data=data
		self.left=None
		self.right=None
class BST:
	def __init__(self):
		self.root=None
	def insert(self,value):
		if self.root is None:
			self.root=BSTNode(value)
		else:
			self._insert(value,self.root)
	def _insert(self,value,current_node):
		if current_node.data>value:
			if current_node.left == None:
				current_node.left=BSTNode(value)
			else:
				self._insert(value,current_node.left)
		elif current_node.data<value:
				if current_node.right == None:
					current_node.right=BSTNode(value)
				else:
					self._insert(value,current_node.right)
		else:
			print('Already Exists !!!')

	#Inorder Traversal !
	def inorder(self):
		self._inorder(self.root)
	def _inorder(self,root):
		if root!=None:
			self._inorder(root.left)
			print(f'{root.data} ',end=' ')
			self._inorder(root.right)
	#Preorder Traversal !
	def preorder(self):
		self._preorder(self.root)
	def _preorder(self,root):
		if root!=None:
			print(f'{root.data} ',end=' ')
			self._preorder(root.left)	
			self._preorder(root.right)
	def postorder(self):
		self._postorder(self.root)
	def _postorder(self,root):
		if root!=None:
			self._postorder(root.left)	
			self._postorder(root.right)
			print(f'{root.data} ',end=' ')
	def delete_node(self,data):
		pass
	
	def search(self,value):
		if self.root!=None:
			return self._search(value,self.root)
		else:
			return False
	def _search(self,value,root):
		if value==root.data:
			return True
		elif value<root.data and root.left!=None:
			self._search(value,root.left)
		elif value>root.data and root.right!=None:
			self._search(value,root.right)
		return False

#--------------------Ending of BST----------------------#
