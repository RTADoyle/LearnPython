# this one is like your scripts with argv
#make a function and give it a name, *args is like argv but for #functions, and functions start with colons.
#the * takes all the arguments to the function and then put them in args as a list.   not used too often.  
def print_two(*args):
    arg1, arg2 = args   #unpapcks the arguments - everything to the left of the equal is part of rgs
    print(f"arg1: {arg1}, arg2: {arg2}")  #prints out arg1 and arg2

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):  #you don't need to do *args - you can just the names in the def statement
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
