class Search:
	#Linear Search compares all the possibilites and returns true if found !
	def linear_search(self,list_of_items,key):
		flag=False
		for value in list_of_items:
			if value == key:
				flag=True
		return flag
	#The Array shoul be sorted and the function returns -1 if not Found !
	def binary_search(self,list_of_items,key):
		begin_index,end_index=0,len(list_of_items)-1
		while begin_index < end_index:
			mid=(begin_index+end_index)//2
			if list_of_items[mid]==key:
				return mid
			elif list_of_items[mid]<key:
				begin=mid+1
			elif list_of_items[mid]>key:
				end=mid-1
			else:
				return -1
#---------------------End of Searching --------------------------------------------#
#------------Start of Sorting-----------------------------#
class Sorting:
#in bubble sort algorithm, the adacent elements are compared and if the left element is greater than the right element then they are swapped !
	def bubble_sort(self,items):
		for i in range(len(items)-1,0,-1):
			for j in range(i):
				if items[j] > items[j+1]:
					items[j],items[j+1]=items[j+1],items[j]
#The output list will be in reverse, as we have taken the max value in each iteration
#In case of Selection sort the max value/ min value is selected and it is updated each time !
	def selection_sort(self,items):
		#travesing throoghout the list index -1
		for i in range(len(items)-1):
			max_value=i
			for j in range(i,len(items)):
				if items[j]>items[max_value]:
					items[max_value],items[j]=items[j],items[max_value]
#merge sort is a divide an conquer algorithms, and is recursive!
#----The Merge Sort has three functions to make it work- namely the actual merge sort to be called, merge function to join them and the final merge sort to sort the half of elements !
	def merge_sort(self,items):
		#passing the parameters namely the begining index, last index and the actual list/iterable !
		self._merge_sort(0,len(items)-1,items)
	def _merge_sort(self,first_index,last_index,items):
		if first_index <last_index:
			#Obtaining a middle element by the Finding the Average/Dividing by Two LOL !
			middle_index=(first_index+last_index)//2
			self._merge_sort(first_index,middle_index,items)
			self._merge_sort(middle_index+1,last_index,items)
			self.merge(first_index,middle_index,last_index,items)
	def merge(self,first,middle,last,items):
		left=items[first:middle]
		right=items[middle:last+1]
		left.append(999999)
		right.append(999999)
		i,j=0,0
		for k in range(first,last+1):
			if left[i]<=right[j]:
				items[k]=left[i]
				i+=1
			else:
				items[k]=right[j]
				j+=1
#Quick sort is a divide and Conquer Approach and a pivot point is selected and that point is compared to the elements, if they are less than the pivot ,then it comes to the left!
#if its greater than pivot then they are swapped to the right!
	def quick_sort(self,items):
		if len(items)<=1:
			return items
		else:
			pivot=items.pop()
		greater_than,less_than=[],[]
		for value in items:
			if value<pivot:
				less_than.append(value)
			else:
				greater_than.append(value)
		return self.quick_sort(less_than)+[pivot]+self.quick_sort(greater_than)
	#Implementation of insertion sort !
	def insertion_sort(self,items):
		#The First Element is stored into a Sorted List and The Rest of Elements in An Unsorted List
		for value in range(1,len(items)):
			#the value to be sorted is obtained each iterartion 
			#it is compared with the previous element and swapped if previous element is larger!
			value_to_be_sorted=items[value]
			while value_to_be_sorted < items[value-1] and value >0:
				items[value],items[value-1]=items[value-1],items[value]
				value-=1
		return items
	#Ending of Insertion Sort !


#---------------End of Sorting----------------------#
