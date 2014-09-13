import random
print("ask the 8-ball")

      

answers = [
    'no',
    'always',
    'ask again later',
    'oooooooooooooooooooooooooooooooooooooooooooooooooohhh ya',
    'yes',
    'no',
    'with out a doutb',
    ]
while True:
    question = input('>')
    print("ask a question:")
    answer = random.choice(answers)
    print(answer)
