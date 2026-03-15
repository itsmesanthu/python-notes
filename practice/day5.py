'''string manipulation basics in Python!
Concatenation (+)
Repetition (*)
String methods (upper, lower, replace, strip, split, join, find, len, format)
Escape sequences (\n, \t, \\, \')
'''
# Concatenation
first_name = "Santhosh "
last_name = "gp"
full_name = first_name + " " + last_name
print(full_name)   # Santhosh  gp

# Repetition
word = "Hello "
repeated_word = word * 3
print(repeated_word)   # HelloHelloHello

# Uppercase
text = "hello, world!"
uppercase_text = text.upper()
print(uppercase_text)   # HELLO, WORLD!

# Lowercase
text1 = "HELLO, WORLD!"
lowercase_text = text1.lower()
print(lowercase_text)   # hello, world!

# Replace
text2 = "Hello, World!"
new_text = text2.replace("World", "Python")
print(new_text)   # Hello, Python!

# Strip
text3 = "  Hello, World!  "
stripped_text = text3.strip()
print(stripped_text)   # Hello, World!

# Split
text4 = "Hello, World!"
words = text4.split(", ")
print(words)   # ['Hello', 'World!']

# Join
words = ["Hello", "World!"]
next_text = ", ".join(words)
print(next_text)   # Hello, World!

# Find
text4 = "Hello, World!"
index = text4.find("World")
print(index)   # 7

# Length
text5 = "i am gamer"
length = len(text5)
print(length)   # 13

# Format
name = "santhosh gp"
age = 21
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  

#Escape Sequences
#newline
text = "Hello\nWorld!"
print(text)   
#tab
hi= "Hello\tWorld!"
print(hi)
#backslash
back = "Hello\\World!"
print(back)
#single quote
single = "it\'s me santhu"
print(single)
#accessment operator
hi="uta aytha"
print(hi[0])
print(hi[1:3])
print(hi[1:])
print(hi[:3])