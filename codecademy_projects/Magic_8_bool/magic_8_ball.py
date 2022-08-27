# code cademy project for python 3 
# Magic 8 ball is project based on control flow and booliens and conditions and more

# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

import random 
name = "Oussama"
question = "Yes"

answer = ""
random_number = random.randint(1, 9)

# these print value call the random variabl which is assign with  a mudel random these mudel we use it to randamly take a number bettween 1 and 9 each time you print it
print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
  
elif random_number == 2:
  answer = "It is decidedly so"
  
elif random_number == 3:
  answer = "Without a doubt."
  
elif random_number == 4:
  answer = "Reply hazy, try again."
  
elif random_number == 5:
  answer = "Ask again later."
  
elif random_number == 6:
  answer = "Better not tell you now."
  
elif random_number == 7:
  answer = "My sources say no."
  
elif random_number == 8:
  answer = "Outlook not so good."
  
elif random_number == 9:
  answer = "Very doubtful."
  
else:
  answer = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)