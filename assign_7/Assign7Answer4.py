
import re
import random

def phone_number():
    a = '1 ('
    for i in range(3):
        a += str(random.randrange(2,10))
    a += ') '
    a += str(random.randrange(0,10))
    a += str(random.randrange(0,10))
    a += str(random.randrange(0,10,2))
    a += '-'
    a += str(random.randrange(0,6))
    a += str(random.randrange(0,10))
    a += str(random.randrange(0,10))
    a += str(random.randrange(0,10))
    print(a)
    return a


# The code below will test your work by calling your function many times and ensuring that
# your function returns phone numbers fulfill the above rules.
# HOWEVER, the code below will not check whether your code is too restrictive! The TAs will
# check for that by reading your code.
pattern = r'1 \([2-9]\d{2}\) \d{2}[02468]-[0-5]\d{3}'
trials = 100
successes = 0
for i in range(trials):
    phone = phone_number()
    correct = re.match(pattern, phone) is not None
    if not correct:
        print(f'Invalid phone number generated: {phone}')
    successes += 1 if correct else 0

print(f'Percentage correct: {100*successes/trials}%')
