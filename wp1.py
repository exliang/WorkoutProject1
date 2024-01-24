
#wp1.py

#Emily Liang
#exliang@uci.edu
#79453973

import sys 

def main():
	pass

def reverse_cipher():
	#read in data from a txt file
	#put each line in file into list, reverse the list & use string slicing to reverse each sentence
	#output data in another file
	reversed_lines = []
	file_input = input("Enter a filename to input contents to: ")
	file_output = input("Enter a filename to output contents to: ")
	with open(file_input, 'r') as input_file:  # opening the file to read
		for line in input_file: 
			line = line.strip()  #get rid of ending newlines/tabs/spaces
			reversed_lines.append(line[::-1])
	with open(file_output, 'a') as output_file:
		for reversed_lines in reversed_lines:
			output_file.write()

if __name__ == '__main__':
	main()