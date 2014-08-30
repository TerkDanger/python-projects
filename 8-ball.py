import random



answers = [
     'yes',
     'no',
     'yes loeloe',
     '#o ya',
     'cheve ss',
     'o ya',
     '#bibble jasuse',
     'with out a doubt',
]
while True :
    print (' ask the 8-ball:')  
    question = input('>')
    answer = random.choice(answers)
    print(answer)
    print()
