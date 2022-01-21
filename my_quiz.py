#Quiz_game
print("Welcome to the Quiz!!")

#Asking user whether wanna play or not
playing = input("Do you want to play? ")

#if answer is yes the it will continue else program will end
if playing.lower() != 'yes':
    quit()


print("OK, Lets Begin!!")

#Declaring the score
score = 0

#First Question
q1 = input("What does CPU stands for? ")
if q1.lower() == 'central processing unit':
    print("Correct!!")
    score += 1

else:
    print("Incorrect!")

#Second Question
q2 = input("What does RAM stands for? ")
if q2.lower() == 'random access memory':
    print("Correct!!")
    score += 1
else:
    print("Incorrect!")

#Third Question
q3 = input("What does GPU stands for? ")
if q3.lower() == 'graphics processing unit':
    print("Correct!!")
    score += 1

else:
    print("Incorrect!")
    
#Fourth Question
q4 = input("What does PSU stands for? ")
if q4.lower() == 'power supply':
    print("Correct!!")
    score += 1

else:
    print("Incorrect!")

#Displaying the final Score
print("You Scored", str(score),"answer correct!")
