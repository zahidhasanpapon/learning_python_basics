secret_word = 'Zahid'
guess =''
count_guess = 0
limit_guess = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if count_guess < limit_guess:
         guess = input('Enter guess: ')
         count_guess += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print('Lost the game')
else:
    print('you win')