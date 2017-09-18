#defines variable types_of_people
types_of_people = 10
#when x is called later, it will be a combination of the text and the variable
x = f"There are {types_of_people} types of people."
#creates variables below
binary = "binary"
do_not = "don't"

#formatted string - blend of 2 variables and text
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

#sets up joke_Evaluation, and applies a true false condition to it.  if you change False to something besides True, you'll get an error.
hilarious = True
joke_evaluation = "Isnt that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
