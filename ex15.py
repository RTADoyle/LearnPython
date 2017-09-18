#calls the sys module and grabs the argv functionality
#from sys import argv
#first item is the script name, second one is the name of the file you want to open (ie ex15_sample.txt)
#script, filename = argv

#txt = open(filename) #opens the file you specified and stores it in txt

#print(f"Here's your file {filename}:") # reiterates the filename
#print(txt.read()) #looks into the file stored in txt and returns it

print("What file would you like to read?:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
