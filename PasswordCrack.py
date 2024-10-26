import random

# Password setup and difficulty settings
password_levels = {
    "easy": ["hack", "code", "data", "link"],
    "medium": ["cyber123", "vault99", "admin007", "backup"],
    "hard": ["Qz8@Lk2!", "A1b9@xYz", "R@nd0m123", "Tr@ck3R!"]
}
password_level = random.choice(list(password_levels.keys()))
password = random.choice(password_levels[password_level])

# Shared variables
attempts = 0
hint_used = False
game_over = False
brute_force_progress = []
def dictionary_attack(guess):
    global attempts, game_over
    attempts += 1
    if guess == password:
        game_over = True
        return "Access Granted!"
    return "Incorrect guess."

def get_hint():
    global hint_used
    if hint_used:
        return "Hint already used!"
    hint_used = True
    return f"Hint: The password starts with '{password[0]}' and has {len(password)} characters."
