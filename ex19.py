#this sectin defines the function, but doesn't actually call it
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have{cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

#this section runs it, directly assigning alues to cheese_count and boxes_of_crackers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#this section runs it, using variables, which are directly hardcoded.  These variables live in the script, not in the function, but then are passed into the function.  
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#this runs it, using calculations
print("We can even do math inside too:")
cheese_and_crackers(10 +20, 5+6)

#this runs it, doing a combination of the above.  taking  a direct variable and performing some math on it
print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
