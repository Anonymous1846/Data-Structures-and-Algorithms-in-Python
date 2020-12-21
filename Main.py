from Data_Structures import *

if __name__=='__main__':
	option=int(input('1)Data Structures\n2)Algorithms\n'))
	if option == 1:
		choose_ds=int(input('1)Stack\n2)Queue\n'))
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
	elif option==2:
		choose_al=int(input('1)Linear Search\n2)Binary Search\n'))
		if choose_al ==1:
			#The List of Elements as the Experimental Iteratable !
			check_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,10090,891,188,1,-1]
			key=10090
			non_key=-999898
			print('Yes its Here !'if linear_search.linear_search(10090) else 'Nope !')
			print('Yes its Here !'if linear_search.linear_search(-99998)else 'Nope !')
		elif choose_al ==2:
			#The List of Elements as the Experimental Iteratable !
			check_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,10090,891,188,1,-1]
			check_list.sort()
			key=10090
			non_key=-999898
			print('Yes its Here !'if binary_search.linear_search(check_list,10090) else 'Nope !')
			print('Yes its Here !'if binary_search.linear_search(check_list,-99998)else 'Nope !')
