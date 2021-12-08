

new_data = []

def fish_check(number):
	if number == ",":
		pass
	elif int(number) > 0:
		new_string += (str(int(number) - 1))
	elif int(number) == 0:
		new_string += ', 6'
		new_fish += 1
	return number


with open('input.txt') as text:
	for line in text:
		data = line.strip().split('\n')
		#print(data)
		#print(data[0])
		b = data[0]
		a = b.replace(",","")
		#print(a)
		#print(type(a))
	print('--------------------------')
	print('start')
	for iteration in range(1,257):
		print(f'iteration: {iteration}')
		new_string = ''
		#print(f'a is: {a}')
		new_fish = 0
		for number in str(a):
			
			
			#print(number)
			#print(type(number))
			if number == ",":
				pass
			elif int(number) > 0:
				new_string += (str(int(number) - 1))
			elif int(number) == 0:
				new_string += '6'
				new_fish += 1
		#print(f'new_string after loop: {new_string}')
		#print('adding new fish:')
		#print(new_fish)
		
		for fish in range(new_fish):
			new_string += '8'
		#print(f'new string after fish added: {new_string}')
		
		#print(f'iteration: {iteration}')
		#print(f' current string: {new_string}')
		a = new_string
	
	print(f'count: {len(new_string)}')
	#print('end')
	#print('--------------------------')
	
