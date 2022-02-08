user_guesses = 10
correct_answer = ['p', 'y', 't', 'h', 'o', 'n']
available_letters_to_guess = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
user_guest_display = ['_', '_', '_', '_', '_', '_']
display_updated_answer = ''
display_updated_alphabet = ''

print('Welcome to hangman! Can you save me by guessing the correct word! You have',
      user_guesses, 'guesses to save me! Your word is', len(correct_answer), 'letters long')
print('______')

while user_guesses > 0:
    guess = input('Guess a letter ')
    if len(guess) > 1:
        print('This is not a single letter, please enter a single letter to guess')
        continue
    elif guess.lower() in correct_answer:
        if user_guest_display == correct_answer:
            print('You won!!')
            break
        elif user_guesses == 0:
            print('Sorry, you have lost!! Better luck next time!!')
            break
        else:
            display_replacement_placeholder = correct_answer.index(guess.lower())
            user_guest_display.pop(display_replacement_placeholder)
            user_guest_display.insert(
            display_replacement_placeholder, guess.lower())
            user_guesses -= 1
            display_updated_answer = display_updated_answer.join(
                user_guest_display)
            print('That was correct!!!You have ',
                  user_guesses, 'guesses left!')
            print(display_updated_answer)
            available_letters_to_guess.pop(
                available_letters_to_guess.index(guess.lower()))
            display_updated_alphabet = display_updated_alphabet.join(
                available_letters_to_guess)
            print('Letters left to guess from!', display_updated_alphabet)
            display_updated_answer = ''
            display_updated_alphabet = ''
    else:
        if user_guesses == 0:
            print('Sorry, you have lost!! Better luck next time!!')
            break
        else:
            user_guesses -= 1
            print('That is not in the answer, please guess again! You have ',
                  user_guesses, 'guesses left!')
            display_updated_answer = display_updated_answer.join(
                user_guest_display)
            print(display_updated_answer)
            available_letters_to_guess.pop(
                available_letters_to_guess.index(guess.lower()))
            display_updated_alphabet = display_updated_alphabet.join(
                available_letters_to_guess)
            print('Letters left to guess from!', display_updated_alphabet)
            display_updated_answer = ''
            display_updated_alphabet = ''
