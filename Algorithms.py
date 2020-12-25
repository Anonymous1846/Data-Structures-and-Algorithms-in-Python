#The following class contains the implementation of the Searching And Sorting Algorithms !
#Searching Algorithms are Linear Search(Worst Case O(n), Best Case O(1), Average Case: O(n))
#and The Binary Search which is a divide and conuer approach (Best Case O(1), Worst Case: O(log n), Average Case:O(log n))
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
#-------------------------------------Start of Sorting-----------------------------#
class Sorting:
#in bubble sort algorithm, the ajdacent elements are compared and if the left element is greater than the right element then they are swapped !
	def bubble_sort(self,items):
		for i in range(len(items)-1,0,-1):
			for j in range(i):
				if items[j] > items[j+1]:
					items[j],items[j+1]=items[j+1],items[j]
		return items
#The output list will be in reverse, as we have taken the max value in each iteration
#In case of Selection sort the max value/ min value is selected and it is updated at each iteration  !
	def selection_sort(self,items):
		#travesing throghout the list index -1
		for i in range(len(items)-1):
			min_value=i
			for j in range(i,len(items)):
				if items[j]<items[min_value]:
					items[min_value],items[j]=items[j],items[min_value]
		return items
#merge sort is a divide an conquer algorithms, and is recursive!
#The merge sort divides the list into halves until they become indivisible, then they are joined back to the sorted position,also the recursive version of merge sort is applied !
	def merge_sort(self,items):
		#we will using the merge function to properly merge the final sorted list !
		#base case if the list has only one element, to justify the indivisibilty !
		if len(items)<=1:
			return items
		#recursive calling of the merge_sort function, until we get to the point that we cannot divide the elements !
		left,right=self.merge_sort(items[:9]),self.merge_sort(items[9:])	
		return self.merge(left,right)
	def merge(self,left_list,right_list):
		#Used to store the merged lists
		the_final_list=[]
		left_index,right_index=0,0
		#While the left index and right index values are less than their list length values, we append the values in the final list !
		while left_index<len(left_list) and right_index<len(right_list):
			if left_list[left_index] < right_list[right_index]:
				#we check for the smaller value and append them to the list !
				the_final_list.append(left_list[left_index])
				#updating the left index by one if the left value is inserted, same done for right list value !
				left_index+=1
			else:
				the_final_list.append(left_list[right_index])
				right_index+=1
				#after checking if there are any elements remaining to be pushed to the final array/list !
		if len(left_list)==left_index:
			the_final_list.extend(right_list[right_index:])
		else:
			the_final_list.extend(left_list[left_index:])
		return the_final_list

#Quick sort is a divide and Conquer Approach and a pivot point is selected and that point is compared to the elements, if they are less than the pivot ,then it comes to the left!
#if its greater than pivot then they are swapped to the right!1
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
