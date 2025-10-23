import random

# inittial setup

word_bank=['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi','hashtag','booktok','hello','world']

word=random.choice(word_bank)
guessWord=['_'] * len(word)

attempts=10

#game loop

while attempts > 0:
    print('\nCurrent word:'+''.join(guessWord))
    guess=input('Guess a letter:').lower()  #lower() method converts a string into lower case and returns it
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessWord[i]=guess
        print('Great guess')
    else:
        attempts=attempts-1.   #attempts-=1
        print(f"You guessed it wrong! Number of attempts left:{attempts}")

    if '_' not in guessWord:
        print('Congratulatuons!!You guessed the word correctly!')
        break
    
if '_' in guessWord and attempts==0:
    print(f"You've run out of attempts! \nThe word was {word}")


# import random

# word_bank=['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi','hashtag','booktok','hello','world']
# word=random.choice(word_bank)

# guessWord=['_']*len(word)





# attempts=10

# while attempts>0:
#     print("Current word:"+''.join(guessWord))
#     guess=input("guess a letter:")
#     if guess in word:
#         print("Great guess!")
#         for i in range(len(word)):
#             if word[i]==guess:
#                 guessWord[i]=guess
#     else:
#         attempts-=1
#         print(f'You guessed wrong! Number of attempts left={attempts}')

#     if '_' not in guessWord:
#         print("congratulations you guesssed the word correctly")
#         break
    
# if attempts==0 and '_' in guessWord:
#     print(f"you couldn't guess the world! The word was {word}")










