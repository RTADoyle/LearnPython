from sys import argv

script, input_file = argv

#function that reads whatever f is.
def print_all(f):
    print(f.read())

#function that moves to the beginning of file f.
def rewind(f):
    f.seek(0)
#function that reads the line # associated with the row # from line_count
def print_a_line(line_count, f):
    print(line_count, f.readline())

#opens up a file to be used later in script
current_file = open(input_file)

print("First let's print the whole file:\n")

#prints content of current file, also moves to the end.
print_all(current_file)

#moves back to the beginning of the file
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

#establishes value of current line as 1, feeding that to print_a_line function
current_line = 1
print_a_line(current_line, current_file)

#adds one to current line, and prints that line #
current_line = current_line + 1
print_a_line(current_line, current_file)

#adds one to current line, and prints that line
current_line = current_line + 1
print_a_line(current_line, current_file)
