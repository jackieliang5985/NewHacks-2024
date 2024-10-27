import random
import pygame
from StartingScreen import Story

# Define password levels
password_levels = {
    "easy": ["abc", "123"],
    "medium": ["hack", "code", "data", "link"],
    "hard": ["password1", "username1"],
}

# Randomly select a password level and the corresponding password
password_level = "easy"
password = random.choice(password_levels[password_level])

# Initialize shared variables
attempts = 0
hint_used = False
game_over = False
win = False

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hacker Intro")
font = pygame.font.Font(pygame.font.get_default_font(), 24)


def dictionary_attack(guess):
    """Function to check if the user's guess matches the password."""
    global attempts, game_over, win
    attempts += 1

    # Compare normalized guess to password
    if guess.strip().lower() == password.lower():
        game_over = True
        win = True  # Set win to True if the guess is correct
        return "Access Granted!"

    # End game if maximum attempts are reached
    if attempts >= 3:
        game_over = True
        win = False  # Set win to False if max attempts reached
        return ("You've exceeded the maximum number of attempts", "Access Denied.")

    return "Incorrect guess."


def get_hint():
    """Provide a hint based on the difficulty level."""
    global hint_used
    if hint_used:
        return "Hint already used!"
    hint_used = True
    if password_level == "hard":
        return [
            f"Hint: The password comprises a widely used phrase,",
            f"starting with '{password[0]}', and ending with '{password[-1]}'."
        ]

    return [f"Hint: The password starts with '{password[0]}' and has {len(password)} characters."]


def play_game_1():
    global attempts, hint_used, game_over, password_level, password, win
    attempts = 0
    hint_used = False
    game_over = False
    win = False

    storyline = [
        "Welcome, Agent X.",
        "You've been given a hint of some 'vulnerability'",
        "within Ginky's bank account.",
        "Your task is to find out what his password is,",
        " but beware; you only have a few tries.",
        "We've found some information; please press h"
    ]

    story = Story(screen, font, storyline, 10)
    feedback = ""  # Variable to hold feedback messages
    hint_message = []  # Changed to a list to hold multiple lines

    while True:  # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # Return False if game is quit

            # Handle input for the story
            story.handle_input(event)

            # Check for user input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Use dictionary_attack to check the input text
                    guess_feedback = dictionary_attack(story.input_text)
                    feedback = guess_feedback  # Store feedback message
                    story.input_text = ""  # Reset input text after checking
                elif event.key == pygame.K_BACKSPACE:
                    story.input_text = story.input_text[:-1]
                elif event.key == pygame.K_h:  # Hint when 'h' is pressed
                    hint_message = get_hint()  # This will be a list now

        # Update the story display
        story.update()

        # Clear screen with black background
        screen.fill((0, 0, 0))

        # Draw the story and input
        story.draw()
        story.draw_input()

        # Render and draw feedback message
        feedback_surface = font.render(feedback, True, (0, 255, 0))
        screen.blit(feedback_surface, (50, 550))  # Display feedback

        # Render and draw hint message
        for i, line in enumerate(hint_message):
            hint_surface = font.render(line, True, (255, 255, 0))  # Yellow for hints
            screen.blit(hint_surface, (50, 525 + i * 30))  # Adjust the vertical position for each line

        # Update display
        pygame.display.flip()

        # Add a small delay to control frame rate
        pygame.time.delay(50)

        # Break loop if game is over
        if game_over:
            pygame.time.delay(2000)  # Show final message for 2 seconds
            return win  # Return True if win, False if loss
