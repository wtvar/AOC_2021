#advent of code 2021 day 1

increases = 0

with open('input.txt') as text:
	#data = text.read()
	previous_item = 0
	for line in text:
		data = line.strip().split('\n')
		print(f'0 data is {data}')
		print(f'1 data is type: {type(data)}')
		print(f'2 previous_item is type: {type(previous_item)}')
		print(f'3 data[0] is type: {type(data[0])}')
		print(f'4 int(data[0]) is type: {type(int(data[0]))}')
		print('------------------------')
		if int(data[0]) > int(previous_item):
			increases += 1
		else:
			pass
		previous_item = data[0]
		print(f'current increases value: {increases}')
	print(f'total increases: {increases-1}')
