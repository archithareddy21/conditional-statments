
import random
user=input("enter a choice")
choices=["rock","paper","scissors"]
computer_guess=random.choice(choices)
print(f"\nyour choice {user},computer choice {computer_guess}.\n")
if user==computer_guess:
    print("it is a tie")
elif user=='rock':
    if computer_guess=='scissors':
        print('you win')
    else:
        print('sorry,you lose') 
elif user=='paper':
    if computer_guess=='rock':
        print('you win')
    else:
        print('sorry,yoo lose')
elif user=='scissors':
    if computer_guess=='paper':
        print('you win') 
    else:
        print('sorry,you lose') 
                 
