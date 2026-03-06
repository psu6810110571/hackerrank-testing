import random

def guess_number(guess):
    # สุ่มตัวเลขระหว่าง 1 ถึง 10
    answer = random.randint(1, 10)
    
    if guess == answer:
        return "You win"
    elif guess < answer:
        return "Too low"
    else:
        return "Too high"