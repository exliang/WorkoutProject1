
#wp1.py

#Emily Liang
#exliang@uci.edu
#79453973

import sys 

def main():
	reverse_cipher()

def reverse_cipher():
	reversed_lines = []
	file_input = sys.argv[1] 
	file_output = sys.argv[2]
	with open(file_input, 'r') as input_file:  # opening the txt file to read
		for line in input_file: 
			line = line.strip()  #get rid of ending newlines/tabs/spaces
			reversed_lines.append(line[::-1])  #appending the reversed line to the list
	with open(file_output, 'a') as output_file:
		for reversed_lines in reversed(reversed_lines):
			output_file.write(reversed_lines + "\n")

if __name__ == '__main__':
	main()
