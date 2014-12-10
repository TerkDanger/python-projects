import random

print("welcome")
print("enter your question below:")

while True: 
    question = input('> ')
    answers = ['yes.','no.','maybe.','ask again later.']
    answer = random.choice(answers)
    print(answer)
