# Decryptor Mini-Game
import random

WORDS_DECRYPTOR = ['science', 'computer', 'student', 'newhacks', 'mac', 'apple',
                   'tree', 'basketball', 'football', 'soccer', 'hacker', 'hat',
                   'headphones', 'camera', 'word', 'easy', 'difficult', 'funny',
                   'water', 'orange']
def decryptor():
    word1 = random.choice(WORDS_DECRYPTOR)
    word2 = random.choice(WORDS_DECRYPTOR)
    scrambled = scramble(word1)
    caesared, shift = caesar(word2)

    attempt1 = 3
    attempt2 = 3

    print("YOU MUST DECRYPT: First let's unscramble, then de-cipher, shall we??")
    print(f"Your scrambled word is: {scrambled}")

    while attempt1 > 0:
        guess = input("").strip().lower()
        if guess == word1:
            print("SUCCESS")
            break
        else:
            attempt1 -= 1
            print("FAIL")

    if attempt1 == 0:
        print("You've lost!")
        exit()

    message = ""
    if shift == 1:
        message = ("I'm unique, like no one else, yet often paired with zero."
                   " I am often first but can also stand alone.")
    elif shift == 2:
        message = "I am a pair, always together! People call me Peace!"
    else:
        message = ("People always have my number of wishes, alongside how many "
                   "bears are used in the nostalgic fairy tales!")

    print(f"NOW, your encrypted word is: '{caesared}' using Caesar Cipher with the shift "
          f"being the answer to the following riddle: \n{message}")

    while attempt2 > 0:
        guess = input("").strip().lower()
        if guess == word2:
            print("SUCCESS")
            # Exit back to main screen for other mini games
        else:
            attempt2 -= 1
            print("FAIL")

    if attempt2 == 0:
        print("You've lost!")
        exit()

def scramble(wordo):
    letters = list(wordo)
    random.shuffle(letters)
    question = ''.join(letters)
    if question == wordo:
        return scramble(wordo)
    return question

def caesar(wordo):
    question = ""
    shift = random.randint(1, 3)
    for char in wordo:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            question += shifted_char
    return question, shift

decryptor()
