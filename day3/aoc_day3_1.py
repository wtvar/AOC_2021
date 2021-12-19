
counter = 0
end_string = ''
other_string = ''
counting = {'1':0, '2':0, '3':0, '4':0, '5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
print(counting['1'])
with open('input.txt') as text:
	for line in text:
		data = line.strip().split('\n')
		for x in range(1,13):
			print(f'x is: {x}')
			result = data[0][x-1]
			print(f'result: {result}')
			if int(result) > 0:
				counting[str(x)] += 1
				print(f' result is > 0 : {counting[str(x)]}')
			else:
				counting[str(x)] -= 1
				print(f' result is < 0 : {counting[str(x)]}')
	print(counting)
	for x in counting.values():
		print(x)
		if x > 0:
			end_string += '1'
		else:
			end_string += '0'
	print(end_string)
	print(f'end: {int(end_string,2)}')
	for digit in end_string:
		if digit == '0':
			other_string += '1'
		else:
			other_string += '0'
	print(other_string)
	print(f' end2: {int(other_string,2)}')
	print(f'final: {int(end_string,2) * int(other_string,2)}')
	
			
