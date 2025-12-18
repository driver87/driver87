my_string = "Hello, World!"
print(my_string)

string_with_quotes = "Hello, it's me! "
another_with_quotes = 'He said "You are amazing!" yesterday.'
print(string_with_quotes + another_with_quotes)

another_with_quotes = "She said \"You are amazing!\" yesterday."
print(another_with_quotes)

multiline_string = """This is an example of multiline string.
You can write whatever and wherever you want.
Just write between the three quotes"""
print(multiline_string)

"""This is an example of multiline string used as a comment.
You can write whatever and wherever you want.
Just write between the three quotes"""

name = "Ankur"
greeting = "Hello, " + name
print(greeting)

#You cannot add an integer to a string directly.
age = 38
age_as_string = str(age)
print("You are " + age_as_string + " years old.")

#String Formatting using f strings (Python 3.6+)

age = 40
print(f"You are {age} years old.")

#Example of format method

name = "Talwar"
final_greeting = "How are you, {}?" # This has now become a template
talwar_greeting = final_greeting.format(name)
print(talwar_greeting)

name = "bob"
bob_greeting = final_greeting.format(name) 
print(bob_greeting)
