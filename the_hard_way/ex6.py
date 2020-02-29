
# set the variable to value 10
types_of_people = 10
# set variable to fstring with types_of_people variable in the sentence
x = f"There are {types_of_people} types of people."

# set binary value to binary
binary = "binary"
# set do_not to string "don't"
do_not = "don't"
# set y to fstring with binary and do_not in the sentence
y = f"Those who know {binary} and those who {do_not}."

# print result of x and y
print(x)
print(y)

# print result of x and y on fstring
print(f"I said: '{x}'")
print(f"I also said: '{y}'")

# set hilarious to False
hilarious = False

# set joke_evaluation as string and attach {variable space}
joke_evaluation = "Isn't that joke so funny?! {}"
# print using the variable name with format method and hilarious value as argument
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
