print("How old are you?", end= '  ')
age = input()
print("How tall are you in inches?", end= '  ')
#if you put a number in below for the string the int thing then turns it into a string
height = int(input())
print("How much do you weigh?", end ='  ')
weight = input()
height_yards = height/36
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print(f"And you're {height_yards} yards")
