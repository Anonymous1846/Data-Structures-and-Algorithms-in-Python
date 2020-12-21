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
	def bubble_sort(self,items):
		pass
#---------------End of Sorting----------------------#
