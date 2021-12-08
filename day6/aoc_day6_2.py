
my_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}


with open('input.txt') as text:
	for line in text:
		data = line.strip().split('\n')
		b = data[0]
		a = b.replace(",","")
	for item in a:
		my_dict[item] += 1
	#print(a)
	#print(my_dict)
	print('--------------------------')
	print('start')
	for iteration in range(1,257):
		print(f'iteration: {iteration}')
		
		print('starting dict')
		#for each value, increase value-1 by 1
		#for each 0 increase 8 by 1
		eights = 0
		sixes = 0
		print(my_dict)
		for item in my_dict:
			if my_dict[item] == 0:
				print(f'passing as item {item} is: {my_dict[item]}')
				pass
			elif my_dict[item] > 0:
				
				print(f' item is : {item}, value is: {my_dict[item]}')
				#print(type(item))
				if item == '0':
					#if the item is 0 then we increase 8 by the number of items in 0 and set 0 to zero
					#my_dict['8'] += my_dict['0']
					eights += my_dict['0']
					sixes += my_dict['0']
					print('increased 8, decreased 0')
					my_dict['0'] = 0

				else:
					#print(int(item))
					#print(int(item) - 1)
					my_dict[str(int(item) - 1)] += my_dict[item]
					my_dict[item] = 0
					print(f'decreased {item}, increased {str(int(item) - 1)}')
					print(my_dict)
		my_dict['8'] += eights
		my_dict['6'] += sixes
		eights = 0
		sixes = 0
		print('---------end of iteration---------')
	print(f'final: {my_dict}')
	sum = 0
	for item in my_dict:
		sum += my_dict[item]
	print(f'sum is: {sum}')
	print('end')
	print('--------------------------')
