import random

password_levels = {
    "easy": ["abc", "123"],
    "medium": ["hack", "code", "data", "link"],
    "hard": ["password1", "username1"],
}
password_level = random.choice(list(password_levels.keys()))
password = random.choice(password_levels[password_level])

# Shared variables
attempts = 0
hint_used = False
game_over = False

def dictionary_attack(guess):
    global attempts, game_over
    attempts += 1
    if guess == password:
        game_over = True
        return "Access Granted!"
    if attempts > 3:
        return False
    return "Incorrect guess."

def get_hint():
    global hint_used
    if hint_used:
        return "Hint already used!"
    hint_used = True
    if password_level == "hard":
        return f"Hint: The password comprises of a widely used pharse, starting with '{password[0]}', and ends with {password[len(password)-1]}"
    return f"Hint: The password starts with '{password[0]}' and has {len(password)} characters."

def play_game_1():
    global attempts, hint_used, game_over, password_level, password
    attempts = 0
    hint_used = False
    game_over = False

    print(f"You are playing the '{password_level}' level.")

    while not game_over:
        guess = input("Enter your guess or type 'hint' for a hint: ").strip()

        if guess.lower() == "hint":
            print(get_hint())
            continue

        feedback = dictionary_attack(guess)
        print(feedback)

        if game_over:
            if feedback == "Access Granted!":
                print("Congratulations! You've successfully accessed the system.")
            else:
                print("You've exceeded the maximum number of attempts. Access Denied.")

play_game_1()
