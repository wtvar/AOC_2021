#advent of code 2021 day 1

increases = 0
count = 0
number_of_counts = 0
previous_item = 0
sum = 0
dict1 = {}
with open('input.txt') as text:
	#data = text.read()
	
	for line in text:
		data = line.strip().split('\n')
		sum += int(data[0])
		dict1[count] = sum
		print(dict1[count])
		count += 1
	print(type(dict))
	
	for count,item in dict1.items():
		print(count,':',item)

	print('----------------------')
	print('start of solution')
	for count,item in dict1.items():
		#print(item)
		if count == 3:
			number = item - dict1[count - 3]
			number2 = dict1[count-1]
			print(f'special case: number = {number}, number2 = {number2}')
			if number > number2:
				increases += 1
				print(f'increased to {increases}')
			else:
				pass
		if count > 3:
			number = item - dict1[count - 3]
			number2 = dict1[count -1] - dict1[count - 4]
			print(f'count is {count}')
			print(f'item is {item}')
			print(f'number is {number}')
			print(f'number2 is {number2}')
			if number > number2:
				increases += 1
				print(f'increased to {increases}')
			else:
				pass
		else:
			pass
		print(f'total increases: {increases}')
			
			
		
