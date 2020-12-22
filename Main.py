from Data_Structures import *
from Algorithms import *
if __name__=='__main__':
	option=int(input('1)Data Structures\n2)Algorithms\n'))
	if option == 1:
		choose_ds=int(input('1)Stack\n2)Queue\n3)Linked List\n4)BST'))
		if choose_ds ==1:
			stack=Stack()
			stack.push(1)
			stack.push(2)
			stack.push(3)
			stack.peek()
			print(f'{stack.pop()} removed !')
			stack.peek()
			print('10 is Present !'if stack.contains(10) else 'Nope !')
			print('2 is Here !' if stack.contains(2) else 'Nope !')
		elif choose_ds==2:
			queue=Queue()
			queue.enqueue(1)
			queue.enqueue(2)
			queue.enqueue(3)
			queue.enqueue(4)
			queue.enqueue(5)
			queue.enqueue(6)
			queue.traverse()
			print('10 is Present !'if queue.contains(10) else 'Nope !')
			print('2 is Here !' if queue.contains(2) else 'Nope !')
		elif choose_ds==3:
			linked_list=Linked_List()

	elif option==2:
		choose_al=int(input('1)Linear Search\n2)Binary Search\n3)Bubble Sort\n4)Selection Sort\n5)Merge Sort\n6)Quick Sort\n7)Insertion Sort\n'))
		search=Search()
		if choose_al ==1:
			#The List of Elements as the Experimental Iteratable !
			check_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,10090,891,188,1,-1]
			key=10090
			non_key=-999898
			print('Yes its Here !'if search.linear_search(10090) else 'Nope !')
			print('Yes its Here !'if search.linear_search(-99998)else 'Nope !')
		elif choose_al ==2:
			#The List of Elements as the Experimental Iteratable !
			check_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,10090,891,188,1,-1]
			check_list.sort()
			key=10090
			non_key=-1
			print('Yes its Here !'if search.linear_search(check_list,10090) else 'Nope !')
			print('Yes its Here !'if search.linear_search(check_list,-1)else 'Nope !')
		elif choose_al == 3:
			test=[12,3,4,-56,7,8,9,990,-11,9,-189989,909090]
			sorting=Sorting()
			sorting.bubble_sort(test)
			print(test)
		elif choose_al == 4:
			test=[12,3,4,-56,7,8,9,990,-11,9,-189989,909090]
			sorting=Sorting()
			sorting.selection_sort(test)
			print(test)

		elif choose_al ==5:
			test=[12,3,4,-56,7,8,9,990,-11,9,-189989,-90909,999990,-99909090]
			sorting=Sorting()
			sorting.merge_sort(test)
			print(test)
		elif choose_al ==6:
			test=[12,3,4,-56,7,8,9,990,-11,9,-189989,-90909,999990,-99909090]
			sorting=Sorting()
			print(sorting.quick_sort(test))
		elif choose_al ==7:
			test=[12,3,4,-56,9,-989898,7,8,9,990,-11,9,-189989,-90909,999990,-99909090]
			print(test)
			sorting=Sorting()
			print(sorting.insertion_sort(test))
