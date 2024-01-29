
#wp1.py

#Emily Liang
#exliang@uci.edu
#79453973

import sys 

def main():
	reverse_cipher()

def reverse_cipher():
	file_input = sys.argv[1] 
	file_output = sys.argv[2]

	input_file = open(file_input, 'rb')
	output_file = open(file_output, 'wb')
	input_file.seek(0,2)  # move file pointer to end of file
	current_pos = input_file.tell()
	index = -1

	while current_pos >= 0:  # a condition thats True as long as there are more bytes to read 
		# print("input_file.read(1):",input_file.read(1))
		output_file.write(input_file.read(1))

		# if input_file.read(1) == b"\r" or input_file.read(1) == b"\n" or input_file.read(1) == b"\r\r" or input_file.read(1) == b"\r\n" or input_file.read(1) == b"\n\n":
		# 	# write to file but w/out the newline
		# 	print("CARRIAGE RETURN FOUND")
		# 	continue
		# else:
		# 	output_file.write(input_file.read(1))

		if current_pos >= 2:  # if there's more than 2 chars left in file to read 
			input_file.seek(index,2)  # move file pointer to the indexth char from end of file
		else:
			# print("else seek(0)")
			input_file.seek(0)
		# print("current_pos after moving pointer by 1:", current_pos)
		# print("current index after moving pointer by 1:", index)
		current_pos -= 1  # decrease current position
		index -= 1
	# output_file.write(input_file.read(1))  # writing the first letter 

	input_file.close()
	output_file.close()

if __name__ == '__main__':
	main()

# Citations:
# - https://pynative.com/python-file-seek/#h-seek-backward-with-negative-offset

	# output_file = open(file_output, 'a+')
	# line_num = 1
	# for line in output_file:
	# 	if line_num % 2 == 0:  # even
	# 		line.
	# 	line_num += 1

		# if input_file.read(1) == "\n":
		# 	# write to file but w/out the newline
		# 	print("NEWLINE read")
		# else:
