# --------------- Assigning ---------------
a = 1  # a now contains the number 1
print("Part 1: a is", a)
b = 5  # b contains the number 5, a still contains 1
print("Part 2: a is", a, " b is", b)
a = b  # Both a and b now has the value 5
print("Part 3: a is", a, " b is", b)


# --------------- Comparison ---------------
a = 1  # a is now 1

print("Is 1 the same as 1?", 1 == 1)
print("Is a the same as a?", a == a)

# Two equal signs checks whether the values on either side are the same
print("Does a equal to 1?", a == 1)

# One exclemation mark and one equal sign checks whether the two values are NOT the same
print("Is 1 and 1 different?", 1 != 1)
print("Is 1 and 2 different?", 1 != 2)
print("Is a something else than 1?", a != 1)


# Angle-brackets are used to compare sizes
print("Is 1 less than 5?", 1 < 5)
print("Is 5 greater than 1?", 5 > 1)

print("Is 1 greater than 5?", 1 > 5)
print("Is 5 less than 1?", 5 < 1)

print("Is 1 less than, or equal to 5", 1 <= 5)
print("Is 1 less than, or equal to 1", 1 <= 1)
print("Is 5 greater than, or equal to 1", 5 >= 1)
print("Is 1 greater than, or equal to 1", 1 >= 1)


# --------------- If-else statements ---------------
# The most basic if statement

# If the statement beteween the if and the colon is true, then the first part of the code is executed
print("If True")
if True:
    print("This is always printed")
else:
    print("This is never printed")


# If the statement between the if and the colon is false, then the code after the else statement is executed
print("If False")
if False:
    print("This is never printed")
else:
    print("This is always printed")


a = 1  # a is still 1

print("First if:")
if a == 1:
    print("A is 1!")
else:
    print("A is not equal to 1!")

# Important! Python knows what code to execute from the indentation it has in the code file
# After the if and else statements, the code has 4 spaces before it, that allows python to know that it belongs to that statement
# To go back out of the statement, remove the 4 spaces before the code, like the line with a = 2 below

a = 2  # a is no longer 1

print("Second if:")
if a == 1:
    print("A is 1!")
else:
    print("A is not equal to 1!")


# --------------- While loops ---------------
# While loops keeps repeating the code inside of it, WHILE the statement before the colon is true,
# when the statement before the colon becomes false, it will continue executing the code below it

a = 1
while a < 5:
    print("a is currently:", a)
    print(a, "is less than 5")
    a = a + 1

print("a is no longer less than 5, because it is:", a)
