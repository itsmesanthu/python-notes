# today topic is input and output ,comment
name=input("enter your name: ")
place=input("enter your place: ")
branch=input("enter your branch: ")
collage=input("enter your collage: ") 
sub1=int(input("enter your sub1 marks: "))
sub2=int(input("enter your sub2 marks: "))
sub3=int(input("enter your sub3 marks: "))
totol=sub1+sub2+sub3
parcentage=(totol/300)*100
print("My name is ",name)
print("My place is ", place)
print("My branch is ", branch)
print("My total marks is ", totol)
print("My parcentage is ", parcentage)
#basic Simple Instructions for Self-Introduction
print(f"Hello everyone, good morning! My name is {name}. I am from {place}. "
      f"I am pursuing my {branch} at {collage} and I got a percentage of {parcentage}. "
      f"I am interested in software development and cybersecurity. I also enjoy gaming and fitness. "
      f"My goal is to work in a reputed company, make my parents proud, and achieve a good status in society. "
      f"That’s all about me. Thank you for listening.")
#comments 
# single line comment
       #print("hi i am santhosh gp")
# multi line comment
"""
 Hello everyone, good morning!.My name is {name} .I am from {place} .
I am pursuing my {branch} at {collage} i got a praeccntage of {parcentage}.
I am interested in software development and cybersecurity. I also enjoy gaming and fitness.
My goal is to work in a reputed company, make my parents proud, and achieve a good status in society.
That’s all about me. Thank you for listening.”
"""