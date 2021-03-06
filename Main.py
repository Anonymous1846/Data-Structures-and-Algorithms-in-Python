from Data_Structures import *
from Algorithms import *
from random import *
#Difference between the start and the end time will give the effective runtime !
import timeit
#Below funtion is for testing out the matrices
def tester(func,args):
	print(args)
	for i in range(len(func)):					
		for j in range(len(func[0])):
			print(f'{func[i][j]}\t',end=' ')
		print(' ')
#The Function is used to test the Sorting Algorithms !
#The test sort takes the function and The iteratable as an arguement, and prints the list before and after sorting the list !
#also shows the amount of time taken !
def test_sorts(sorting_function,_iteratable):
	print(f'Before Sorting {len(_iteratable)} Elements !\n')
	print(_iteratable)
	print(f'After Sorting {len(_iteratable)} Elements !\n')
	start=timeit.default_timer()
	print(sorting_function(_iteratable))
	print(f'Algorithm Execution Time :{round(timeit.default_timer()-start,2)} seconds !')
#the below function takes the searching function and the iteratable as an argument and returns the positive prompt if it is found and negative prompt if it is not found !

if __name__=='__main__':
	#initialing the object for soritng 
	sorting=Sorting()
	#initializing the object for Searching 
	searching=Search()
	#the Normal Testing list changed to the numbers 
	#The following line will generate 1000 numbers whose range is between 0 and 10,000
	test_list=[randint(0,5000) for i in range(5000)]
	#The test_list used for soriting will be used for finding the number via linear and binary search !
	key=choice(test_list)
	non_key=randint(99999,999999)
	option=int(input('1)Data Structures\n2)Algorithms\n'))
	if option == 1:
		choose_ds=int(input('1)Stack\n2)Queue\n3)Linked List\n4)BST\n5)Doubly Linked List\n6)Matrix'))
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
			dll=DLL()
			dll.append(12)
			dll.append(13)
			dll.append(14)
			dll.append(15)
			dll.append(16)
			dll.display()
			print(f'The DLL has {dll.length()} Elements !')
			print('12 is found !' if dll.search(12) else 'Nope ')
			print('17 is found !' if dll.search(17) else 'Nope ')
			print('The reverse of the Current DLL is ',dll.reverse())
			print(f'{dll.deleteNode(14)} Deleted !')
			print(f'{dll.deleteNode(16)} Deleted !')
			dll.display()
		elif choose_ds==6:
			matrix =Matrix(2,2)
			matrix1=Matrix(2,2)
			print('Enter The 2x2 Matix Info:')
			matrix.inputMatrix()
			matrix.outputMatrix()
			print('\nGood, Now Enter The Second 2x2 Matrix :')
			matrix1.inputMatrix()
			matrix1.outputMatrix()
			#calculated the sum and displayed it via the tester fucntion declared above
			#The tester function takes two arguments one is the function which returns the 2d matrix and the other is prompt/heading !
			sumMatrix=matrix.add(matrix1)
			tester(sumMatrix,'\tSum\n------------------------\n')
			subMatrix=matrix.subtract(matrix1)
			tester(subMatrix,'\tDifference\n------------------------\n')	
			trans=matrix.transpose()
			tester(trans,'\tTranspose\n------------------------\n')
			prdt=matrix.multiply(matrix1)
			tester(prdt,'\tProduct\n------------------------\n')
			div=matrix.scalar_division(2)
			tester(div,'\tScalar Division\n------------------------\n')


		
	elif option==2:
		choose_al=int(input('1)Linear Search\n2)Binary Search\n3)Jump Search\n4)Exponential Search\n5)Bubble Sort\n6)Selection Sort\n7)Merge Sort\n8)Quick Sort\n9)Insertion Sort\n10)Radix Sort\n11)Shell Sort\n12)Max Heap Sort\n'))
		search=Search()
		if choose_al ==1:
			#test case for linear search !
			#difference between the initial and end time will give the runtime of the algorithm !
			start_time=timeit.default_timer()
			print(f'{key} is found ! Runtime: {round(timeit.default_timer()-start_time,2)}secs' if searching.linear_search(test_list,key) else f'Not Found  Runtime: {round(timeit.default_timer()-start_time,2)}secs!')
			print(f'{key} is found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs' if searching.linear_search(test_list,non_key) else f'Not Found  Runtime: {round(timeit.default_timer()-start_time,2)} secs!')
		elif choose_al ==2:
			#test case for binary search !
			test_list.sort()
			start_time=timeit.default_timer()
			print(f'{key} is found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs' if searching.binary_search(test_list,key) else f'Not Found Runtime: {round(timeit.default_timer()-start_time,2)} secs!')
			print(f'{key} is found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs' if searching.binary_search(test_list,non_key) else f'Not Found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs!')
		elif choose_al == 3:
			#test case for Jump search !
			test_list.sort()
			start_time=timeit.default_timer()
			print(f'{key} is found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs' if searching.jump_search(test_list,key) else f'Not Found Runtime: {round(timeit.default_timer()-start_time,2)} secs!')
			print(f'{key} is found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs' if searching.jump_search(test_list,non_key) else f'Not Found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs!')
	
		elif choose_al == 4:
			#test case for Exponential Search !
			test_list.sort()
			start_time=timeit.default_timer()
			print(f'{key} is found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs' if searching.exp_search(test_list,key) else f'Not Found Runtime: {round(timeit.default_timer()-start_time,2)} secs!')
			print(f'{key} is found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs' if searching.exp_search(test_list,non_key) else f'Not Found ! Runtime: {round(timeit.default_timer()-start_time,2)} secs!')
		elif choose_al == 5:
			test_sorts(sorting.bubble_sort,test_list)
		elif choose_al == 6:
			test_sorts(sorting.selection_sort,test_list)
		elif choose_al == 7:
			test_sorts(sorting.merge_sort,test_list)
		elif choose_al == 8:
			test_sorts(sorting.quick_sort,test_list)
		elif choose_al == 9:
			test_sorts(sorting.insertion_sort,test_list)
		elif choose_al == 10:
			test_sorts(sorting.radix_sort,test_list)
		elif choose_al == 11:
			test_sorts(sorting.shell_sort,test_list)
		elif choose_al ==12:
			test_sorts(sorting.max_heap_sort,test_list)


	
