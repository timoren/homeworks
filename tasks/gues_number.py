import random

rand_num = random.randint(1, 10)
print(rand_num)
guess = 0
while guess != rand_num:
    guess = int(input('choose number between 1 - 10 '))
    if guess > rand_num:
        print('the num is bigger then need')
    elif guess < rand_num:
        print('the num is smaller the need')
    else:
        print('you got it')


