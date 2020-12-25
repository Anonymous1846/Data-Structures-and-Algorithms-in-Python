from Data_Structures import *
from Algorithms import *

#The Function is used to test the Sorting Algorithms !
def test_sorts(sorting_function,_iteratable):
	print('Before Sorting !')
	print(_iteratable)
	print('After Sorting !')
	print(sorting_function(_iteratable))
if __name__=='__main__':
	sorting=Sorting()
	test_list=[12,3,4,5,678,900,987,6,4,3,2,123,45,6,-989,-3,99,88,-90909090,234567890]
	option=int(input('1)Data Structures\n2)Algorithms\n'))
	if option == 1:
		choose_ds=int(input('1)Stack\n2)Queue\n3)Linked List\n4)BST\n5)Matrix'))
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
			linked_list.append(11)
			linked_list.append(2)
			linked_list.append(113)
			linked_list.append(21)
			linked_list.display()
			linked_list.delete(113)
			linked_list.display()
			print('21 is here !' if linked_list.search(2) else 'Nope !')
			print(f'The Linked List Has {linked_list.count()} Elements !')
		elif choose_ds==4:	

			bst=BST()
			bst.insert(10)
			bst.insert(11)
			bst.insert(112)
			bst.insert(113)
			bst.insert(-10)
			bst.insert(90911)
			bst.insert(-112)
			bst.insert(-19090913)
			print('\nInorder:')
			bst.inorder()
			print('\nPreOrder:')
			bst.preorder()
			print('\nPostOrder:')
			bst.postorder()
			print('\nThe Value 122 is present !\n' if bst.search(112) else 'Nope !')
			print('The Value 11112 is present !\n' if bst.search(11112) else 'Nope !')
			bst.delete(-112)
			bst.delete(112)
			bst.inorder()
			print(f'\nThe Current Height of the BST is {bst.height()}')
		elif choose_ds==5:
			matrix =Matrix(2,2)
			matrix1=Matrix(2,2)
			print('Enter The 2x2 Matix Info:')
			matrix.inputMatrix()
			print('\nGood, Now Enter The Second 2x2 Matrix :')
			matrix1.inputMatrix()
			print('yes ' if matrix1.equals(matrix) else 'Nope !')
			finalM=matrix.add(matrix1)
			for row in range(len(finalM)):
				for col in range(len(finalM[0])):
					print(finalM[row][col],end=' ')
				print(' ')
				
		
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
			test_sorts(sorting.bubble_sort,test_list)	
		elif choose_al == 4:
			test_sorts(sorting.selection_sort,test_list)
		elif choose_al ==5:
			test_sorts(sorting.merge_sort,test_list)
		elif choose_al ==6:
			test_sorts(sorting.quick_sort,test_list)
		elif choose_al ==7:
			test_sorts(sorting.insertion_sort,test_list)

	
