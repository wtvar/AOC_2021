#day_2 1
forward = 0
down = 0
up = 0
with open('input.txt') as text:
	for line in text:
		data = line.strip().split('\n')
		chars = data[0].strip().split(' ')
		direction = chars[0]
		value = int(chars[1])
		
		if direction == "forward":
			forward += value
		elif direction == "down":
			down += value
		elif direction == "up":
			up += value
		print(f'forward: {forward}')
		print(f'horizontal: {down - up}')
	print(f'result: {forward * (down - up)}')
