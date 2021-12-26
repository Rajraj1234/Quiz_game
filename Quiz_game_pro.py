x=input("Please enter your name:")
print("Hello "+ x +" Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower() 
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct answer : central processing unit")

answer = input("What does GPU stand for? ").lower() 
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct answer : graphics processing unit")

answer = input("What does RAM stand for? ").lower() 
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct answer : random access memory")

answer = input("What does PSU stand for? ").lower() 
if answer == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct answer : power supply unit")

z=(score/4)*100

print("You got " + str(score) + " questions correct!")
print("You got " + str(z) + "%.")
if z>=35:
    print("Congratulations!! You have passed this quiz")

else:
    print("You have not passed this quiz!!! \n try again")