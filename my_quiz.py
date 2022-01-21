print("Welcome to the Quiz!!")

playing = input("Do you want to play? ")


if playing.lower() != 'yes':
    quit()


print("OK, Lets Begin!!")

score = 0


q1 = input("What does CPU stands for? ")
if q1.lower() == 'central processing unit':
    print("Correct!!")
    score += 1

else:
    print("Incorrect!")

q2 = input("What does RAM stands for? ")
if q2.lower() == 'random access memory':
    print("Correct!!")
    score += 1
else:
    print("Incorrect!")

q3 = input("What does GPU stands for? ")
if q3.lower() == 'graphics processing unit':
    print("Correct!!")
    score += 1

else:
    print("Incorrect!")

q4 = input("What does PSU stands for? ")
if q4.lower() == 'power supply':
    print("Correct!!")
    score += 1

else:
    print("Incorrect!")

print("You Scored", str(score),"answer correct!")