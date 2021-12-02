#day_2 2
forward = 0
down = 0
up = 0
aim = 0
depth = 0

with open('input.txt') as text:
	for line in text:
		data = line.strip().split('\n')
		chars = data[0].strip().split(' ')
		direction = chars[0]
		value = int(chars[1])
		
		if direction == "forward":
			forward += value
			depth += aim * value
		elif direction == "down":
			aim += value
		elif direction == "up":
			aim -= value
		print(f'forward: {forward}')
		print(f'horizontal: {depth}')
	print(f'result: {forward * (depth)}')
