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
#--------------Begining of Doubly Linked List----------------#
class DLL:
	#the below is an inner class for the Node for Doubly Linked List !
	class NodeDLL:
		def __init__(self,data=None):
			self.data=data
			self.prev=None
			self.next=None
	def __init__(self):
		#creates a new node(head node ) each time we initialize a Doubly linked list !
		self.head=None
		#keeps track of the end Node
		self.tail=None
	def append(self,data):
		if self.head==None:
			self.head=self.NodeDLL(data)
			self.head.prev=None
			self.next=None
			self.tail=self.head
		else:
			current_node=self.NodeDLL(data)
			self.tail.next=current_node
			current_node.prev=self.tail
			current_node.next=None
			self.tail=current_node
			#traverses the list !, if there are any element !
	def display(self):
		if self.head!=None:
			current_node=self.head
			while current_node is not None:
				print(f'{current_node.data}->',end=' ')
				current_node=current_node.next
			print(' ')
			#Funtion to search for an element in the array, returns true if found otherwise false !
	def search(self,data):
		if self.head!=None:
			current_node=self.head
			while current_node is not None:
				if current_node.data==data:return True
				current_node=current_node.next
		return False
	#we traverse the list in the reverse order, and append the elements in the rev list and returns it !
	def reverse(self):
		rev=[]
		if self.head!=None:
			current_node=self.tail
			while current_node is not None:
				rev.append(current_node.data)
				current_node=current_node.prev
		return rev
	def length(self):
		if self.head!=None:
			length=0
			current_node=self.head
			while current_node is not None:
				length+=1
				current_node=current_node.next
			return length
		return 0
	#deletes a node in the doubly linked list if it is there !(checking by the numrical value !)
	def deleteNode(self,data):
		if self.head!=None:
			#if the head is the only element in the DLL, then
			if self.head.next is None:
				if self.head.data==data:
					self.head=None
				else:
					print('No Item Found !')
				return	
			#if the head is not null and the head node is to be deleted !
			if self.head.data==data:
				#storing the head node !
				head=self.head
				#new head will be the next head and previous head will be the None value !
				self.head=self.head.next
				self.head.prev=None
				return head.data
			#we will traverse till we reach a point where the next node of the current node is None
			current_node=self.head
			while current_node.next is not None:
				#when we get the data, we stop and break the loop the previous node's next will be the current node's next node and the next node's previous will be the current node's previous node !
				if current_node.data==data:
					break
				current_node=current_node.next
				#checking if it is not the last node !
			if current_node.next is not None:
				current_node.prev.next=current_node.next
				current_node.next.prev=current_node.prev
			else:
				if current_node.data==data:
					current_node.prev.next=None
				else:
					print('Not Found !')
			
			return current_node.data
#--------------Ending of Doubly Linked List------------------#
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
			#the Function to delete the node by value !
			#the below fucntion makes a call to the recursive private function _delete
	def delete(self,data):
		if self.root!=None:
			self._delete(data,self.root)
		else:
			print('The Tree is Empty !')
	def _delete(self,data,node):
		#Checks if the node is null
		if node!=None:
			#if root node data is given data it checks how many children it has 
			if node.data==data:
				#Nill Children 
				if node.left ==None and node.right==None:
					return None
				#Left child and no right Child
				if node.left!=None and node.right==None:
					return node.left
				#Right chil and Nill Left Child !
				if node.right!=None and node.left==None:
					return node.right
				#Two Children
				if node.right!=None and node.left!=None:
					#This Condition if For the nodes with two children !
					#The inorder successor is choosen
					#3
				#       /\
				#      2  4 It has two children !
				#     /  / \
				#    1  2   5
  				#In this case 4
					current_node=node.right
					#We will traverse till we get to the end left child !
					while current_node.left:
						current_node=current_node.left
						#The new Node data will be the inorder successor data !
					node.data=current_node.data
					#recursively deleting the current Node !
					node.right=self._delete(node.data,node.right)
			#Chcking if the node is greater than(Call will be made to current Function will left node paraemeter) or less than the current Node(right node paramter recursive function!)
			elif node.data>data:
				node.left=self._delete(data,node.left)
			else:
				node.right=self._delete(data,node.right)
			return node


	#here the The root term is passed on to the function and if it is none, then false is returned else true !	
	def search(self,value):
		if self.root!= None:
			return self._search(value,self.root)
		else:
			return False
		#The Function is iterative and if the value is less than the root node then then we search the left node,otheriwse the right node(recursive !)
	def _search(self,value,root):
		if value==root.data:
			return True
		elif value < root.data and root.left!=None:
			return self._search(value,root.left)
		elif value > root.data and root.right!=None:
			return self._search(value,root.right)
		return False
	#The hieght of the bst is the longest path from root node to the leaf node
	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
		else:
			return 0
		#The Current Height will be updated as we traverse the tree!
	def _height(self,root,current_height):
		#We return the current height of the tree as soon as we reach the end Node
		if root==None:return current_height
		#we update the length as we traverse through the left as well as the right node !
		left_height=self._height(root.left,current_height+1)
		right_height=self._height(root.right,current_height+1)
		# since we need the maximum distance from the root to the leaf node we choose the left and right node and return the max value !
		return max(left_height,right_height)
#--------------------Ending of BST----------------------#
#-----------------Starting of A matrix------------------#
#A matrix is used to store data in the form of rows an columns

class Matrix:
	def __init__(self,rows,cols):
		self.rows=rows
		self.cols=cols
		self.matrixList=[[0]*self.cols]*self.rows
	def inputMatrix(self):
		#one liner to get user input matrix !
		self.matrixList=[[int(input('>>'))for x in range(self.cols)] for x in range(self.rows)]
	def outputMatrix(self):
		for i in range(self.rows):
			for j in range(self.cols):
				print(f'{self.matrixList[i][j]}\t',end=' ')
			print(' ')
	def add(self,matrix1):
		new_matrix=[[0]*self.cols]*self.rows
	
		if self.rows==matrix1.rows and self.cols==matrix1.cols:
			new_matrix=[[self.matrixList[i][j]+matrix1.matrixList[i][j] for j in range(self.cols)] for i in range(self.rows)]
		return new_matrix
		
	def subtract(self,matrix1):
		new_matrix=[[0]*self.cols]*self.rows
		#for matrix multiplication the rows of the second matrix must be equal to the cols of the first matrix !
		
		if self.rows==matrix1.rows and self.cols==matrix1.cols:
			new_matrix=[[sum(a*b for a,b in zip(_i,_j)) for _j in zip(*matrix1.matrixList)] for _i in self.matrixList]	
		return new_matrix
	def transpose(self):
		transpose=[[0]*self.rows]*self.cols
		#intilizing a new matrix of the order colsxrows(Such that the new matrix can have the rows equal to that of the ol matrix and cols equal to that of rows of new cols !)
		transpose=[[self.matrixList[j][i] for j in range(len(self.matrixList))] for i in range(len(self.matrixList[0]))]
		return transpose
	#matrix multiplication
	def multiply(self,matrix1):
		#inorder to perform matrix multiplication, the rows of the second matrix need to be equal to the cols in the first matrix !
		if self.cols==matrix1.rows:
			#using list comprehension to calculate the matrices !, zip means to concatenate the value and * means to unpack them !
			#the first eleme  
			result_matrix=[[sum(a*b for a,b in zip(x_row,y_col))for y_col in zip(*matrix1.matrixList)] for x_row in self.matrixList]
		return result_matrix
	#scaler division,here the inverse of a scalar value is multiplied by individual matrix elements !
	def scalar_division(self,val):
		self.matrixList=[[self.matrixList[i][j]//val for j in range(len(self.matrixList[0]))] for i in range(len(self.matrixList))]
		return self.matrixList
#-----------------Ending of A matrix------------------# 
#---An AVL is an enhanced Binary Search Tree, where the search time can be optimized by adjusting the hieght of the tree.The hieght difference between the left and right sub-tree is either -1,0,1,otherwise we need to perform 
#rotaion----------#
class AVL:
	#SImilar to the BST, the AVL tree has a Node which has the left and right sub children
	class AVLNode:
		def __init__(self,data=None):
			self.data=data
			self.left=None
			self.right=None
			self.height=0
	#the ctr for the AVL Tree !
	def __init__(self):
		self.root=None
	#a recursive function to calculate the height !
	def calHeight(self,node):
		if not root:
			return 0
		#if the root node is Null, then the height of the AVL tree is 0,other wise we return the max height of the tree !
		return node.height
	def balanceFactor(self,node):
		if not root:
			return 0
		#the balance factor is the difference between the heights of the right and left subtree !
		#the optimal balance factor is in the range of {-1,0,1}
		return self.calHeight(self,node.left)-self.calHeight(self,node.right)
	def rotateRight(self,node):
		#inorder to perform the right rotation, we choose the current node and the then shift to the left child of the current node
		#Then keeping the left node, then we shift to its right Node !

		temporaryLeft=node.left
		currenttemp=temporaryLeft.right

		#the right node of the temporary left child is the function parameter node
		temporaryLeft.right=node
		node.left=currenttemp
		node.height=max(self.calHeight(node.left),self.calHeight(node.right))+1
		temporaryLeft.height=max(self.calHeight(temporaryLeft.left),self.calHeight(temporaryLeft.right)) +1
		return temporaryLeft
	def rotateLeft(self,node):
		#inorder to perform the right rotation, we choose the current node and the then shift to the left child of the current node
		#Then keeping the left node, then we shift to its right Node !

		temporaryRight=node.right
		currenttemp=temporaryRight.left

		#the right node of the temporary left child is the function parameter node
		temporaryRight.left=node
		node.right=currenttemp
		node.height=max(self.calHeight(node.left),self.calHeight(node.right))+1
		temporaryRight.height=max(self.calHeight(temporaryRight.left),self.calHeight(temporaryRight.right)) +1
		return temporaryRight
	def delete(self,data):
		if self.root:
			#calling the helper function to remove the node(data)
			self.root=self._delete(data,self.root)
	#helper function, which takes the parameters data and the node(in this case the root node)
	def _delete(self,data,node):
		if not node:
			return node
		if data<node.data:
			node.left=self._delete(data,node.left)
		elif data>node.data:
			node.right=self._delete(data,node.right)
		else:
			if not node.left and not node.right:
				print('Okay Lets Remove a Leaf Node !')
				del node
				#after deleting the node,we then return None Value !
				return None
			if not node.left:
				#if the left child is empty,then we remove the right child!
				temp=node.right
				del node
				return temp
			#if the right child is empty,then we remove the left child !
			elif not node.right:
				temp=node.left
				del node
				return temp
			#the last case will be removing the node with two children !
			temp=self.getPredecessor(node.left)
			node.data=temp.data
			node.left=self._delete(temp.data,node.left)

		if not node:
			return node
		#calculating the maximum height !
		node.height=max(self.calHeight(node.left),self.calHeight(node.right))+1
		balance=self.balanceFactor(node)
		#if the balance factor is positive and greater than one !
		if balance>1 and self.balanceFactor(node.left)>=0:
			return self.rotateRight(node)
		#in case of left right tree
		if balance >1 and self.balanceFactor(node.left)<0:
			node.left=self.rotateLeft(node.left)
			return self.rotateRight(node)
		if balance<-1 and self.balanceFactor(node.right)<=0:
			return self.rotateLeft(node)
		if balance<-1 and self.balanceFactor(node.right)>0:
			node.right=self.rotateRight(node.right)
			return self.rotateLeft(node)
		return node

	#Helper function to get the predecessor !
	def getPredecessor(self,node):
		if node.right:
			#recursive call to the right child 
			return self.getPredecessor(node.right)
		return node
#----------------------Ending of AVL---------------------------------#1
