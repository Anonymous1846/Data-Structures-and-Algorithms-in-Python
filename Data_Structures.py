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
class Linked_List:
	class Node:
		def __init__(self,data,next):
			self.data=data
			self.next=next
	def __init__(self,rootNode):
		self.rootNode=rootNode



#End of Linked List------------------------------------------#
