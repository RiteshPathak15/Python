# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable

# Syntax:
variable=input()

# But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.
# Example:
variable=int(input())
variable=float(input())

# We can also display a text using input function. This will make input() function take user input and display a message as well
# Example:(For Char)
a=input("Enter the name: ")
print(a)

# Example:(For Int):
a=int(input("Enter the number"))
print(a)