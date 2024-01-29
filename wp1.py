
# wp1.py

# Emily Liang
# exliang@uci.edu
# 79453973

import sys


def main():
    reverse_cipher()


def reverse_cipher():
    file_input = sys.argv[1]
    file_output = sys.argv[2]

    input_file = open(file_input, 'rb')
    output_file = open(file_output, 'wb')

    input_file.seek(0, 2)  # move file pointer to end of file
    end = input_file.tell()  # current pos of file pointer
    index = 0  # char count

    while index <= end:  # loops when char count <= total chars in file
        char1 = read_char(input_file)
        index += 1
        if index <= end:  # char count <= total chars (call before seek)
            input_file.seek(-1, 1)  # moves file pointer to left 1
            char2 = read_char(input_file)
            if char1 == b'\n' and char2 == b'\r':
                output_file.write(b'\r\n')
                index += 1
                if index <= end:
                    input_file.seek(-1, 1)  # move file pointer to left 1 again
            else:
                output_file.write(char1)  # if it's not \n & \r write 1 char
        else:  # 1 char left
            output_file.write(char1)  # if it's not \n & \r write 1 char

    input_file.close()
    output_file.close()


def read_char(input_file):  # reads char w/out changing pos of file pointer
    # keeps track of file's current pos, reads, goes back to current pos
    current_pos = input_file.tell()
    char = input_file.read(1)
    input_file.seek(current_pos)  # moves file to current pos after reading
    return char


if __name__ == '__main__':
    main()

# Citations:
# - https://pynative.com/python-file-seek/#h-seek-backward-with-negative-offset
