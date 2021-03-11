"""
This code should get the user to guess a random number between 1 and 10.
If the user is right, congratulate them.
If they're wrong, say if the answer is higher or lower.
Then say what the answer was.
"""

import random
answer = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

print("random number "+str(answer))
# If the number is correct, tell the user
# Otherwise, tell them if the answer is higher or lower than their guess

if(answer==guess):
    print('The number was {}'.format(answer))
if(answer<guess):
    print('The number was lower than their guess')
else:
    print('The number was higher than their guess')