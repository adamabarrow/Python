'''
Created on Apr 26, 2021

@author: Adama Barrow
'''
# The objective of this program is to test the user on basic high school trivia questions.

#Make a variable called score to keep track of the correct answers. And set
#it to 0.

#Ask the user question one. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
 
#Ask the user question two. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."

#Ask the user question three. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."

#Ask the user question four. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."

#Calculate the percentage the user got. And store it in a variable called p

#Print out the users score: "You got a [score]/4. Or a [p]%."


score = 0 

x = input("What is the powerhouse of a cell? A.Mitochondria B.Nucleus C.Ribosome")

x = x.upper()

if(x == "A"):
    print("Correct")
    score = score + 1 
else:
    print("Incorrect, the correct answer is A.")
    
    
y = input("How many states compromise the United States? A.13 B.45 C.50")

y = y.upper()

if(y == "C"):
    print("Correct")
    score = score + 1 
else:
    print("Incorrect, the correct answer is C.")
    
    
a = input("In y = mx + b, what does m stand for? A.Slope B.Output C.I don't understand math")

a = a.upper()

if(a == "A"):
    print("Correct")
    score = score + 1 
else:
    print("Incorrect, the correct answer is A.")
    

b = input("In English a person, place, or thing is called? A.Verb B.Adjective C.Noun")

b = b.upper()

if(b == "C"):
    print("Correct")
    score = score + 1 
else:
    print("Incorrect, the correct answer is C.")
    
    
if(score == 4):
    print("You got a 4/4. Or a 100%.")
    
if(score == 3):
    print("You got a 3/4. Or a 75%.")
    
if(score == 2):
    print("You got a 2/4. Or a 50%.")
    
if(score == 1):
    print("You got a 1/4. Or a 25%.")
    
if(score == 0):
    print("You got a 0/4. Or a 0%.")