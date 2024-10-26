import random
import pygame

# Word list for the decryptor mini-game
WORDS_DECRYPTOR = [
    'science', 'computer', 'student', 'newhacks', 'mac', 'apple',
    'tree', 'basketball', 'football', 'soccer', 'hacker', 'hat',
    'headphones', 'camera', 'word', 'easy', 'difficult', 'funny',
    'water', 'orange'
]


# Story class for handling text display and input
class Story:
    def __init__(self, screen, font, lines, delay=50):
        self.screen = screen
        self.font = font
        self.lines = lines
        self.delay = delay
        self.line_index = 0
        self.char_index = 0
        self.last_time = pygame.time.get_ticks()
        self.finished_lines = []
        self.input_text = ""
        self.feedback = []  # To hold feedback messages

    def update(self):
        # Handle the animated effect for text display
        if pygame.time.get_ticks() - self.last_time > self.delay:
            self.last_time = pygame.time.get_ticks()
            if self.line_index < len(self.lines):
                current_line = self.lines[self.line_index]
                self.char_index += 1
                if self.char_index > len(current_line):
                    self.finished_lines.append(current_line)
                    self.line_index += 1
                    self.char_index = 0

    def draw(self):
        # Draw the lines on the screen
        y_offset = 20
        for i, line in enumerate(self.finished_lines):
            self.screen.blit(self.font.render(line, True, (0, 255, 0)), (50, y_offset + i * 30))

        # Draw the line that is currently animating
        if self.line_index < len(self.lines):
            current_text = self.lines[self.line_index][:self.char_index]
            self.screen.blit(self.font.render(current_text, True, (0, 255, 0)),
                             (30, y_offset + len(self.finished_lines) * 30))

        # Draw feedback messages
        for j, feedback_msg in enumerate(self.feedback):
            self.screen.blit(self.font.render(feedback_msg, True, (255, 0, 0)),
                             (50, 500 + j * 30))

    def handle_input(self, event):
        # Capture user input for guessing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                user_input = self.input_text
                self.input_text = ""
                return user_input  # Return input for checking
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode
        return None

    def draw_input(self):
        # Draw the input prompt
        input_surface = self.font.render(f"> {self.input_text}", True, (0, 255, 0))
        self.screen.blit(input_surface, (50, 450))

    def add_feedback(self, message):
        # Add feedback message to display
        self.feedback.append(message)
        if len(self.feedback) > 3:
            self.feedback.pop(0)


def scramble(word):
    # Scramble the word
    letters = list(word)
    random.shuffle(letters)
    question = ''.join(letters)
    return question if question != word else scramble(word)


def caesar(word):
    # Apply Caesar cipher shift
    question = ""
    shift = random.randint(1, 3)
    for char in word:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            question += shifted_char
    return question, shift


def decryptor(screen, font):
    # Set up game with random words and scrambled message
    word1 = random.choice(WORDS_DECRYPTOR)
    word2 = random.choice(WORDS_DECRYPTOR)
    scrambled = scramble(word1)
    caesared, shift = caesar(word2)

    attempts1, attempts2 = 3, 3
    correct1, correct2 = False, False

    hints = [
        "I'm unique, like no one else, yet often paired with zero.",
        "I am a pair, always together! People call me Peace!",
        "People always have my number of wishes and bear tales!"
    ]
    shift_hint = hints[shift - 1]

    storyline = [
        "YOU MUST DECRYPT: Unscramble, then decipher the code!",
        f"Scrambled word: {scrambled}"
    ]
    story = Story(screen, font, storyline)

    # Game loop
    # ... (rest of your code remains unchanged)

    # Game loop
    # ... (rest of your code remains unchanged)

    # Game loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        story.update()
        story.draw()
        story.draw_input()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            user_input = story.handle_input(event)

            if user_input:
                # First stage: Unscramble word
                if not correct1:
                    if user_input.lower() == word1:
                        story.add_feedback("SUCCESS! Proceed to next challenge.")
                        correct1 = True
                        story.lines.append(f"Caesar Encrypted word: '{caesared}' - Hint: {shift_hint}")
                    else:
                        attempts1 -= 1
                        story.add_feedback("FAIL" if attempts1 > 0 else "You've lost!")
                    if attempts1 == 0:
                        running = False

                # Second stage: Caesar decryption
                elif correct1 and not correct2:
                    if user_input.lower() == word2:
                        story.add_feedback("Correct!")  # Display "Correct!" message
                        correct2 = True
                    else:
                        attempts2 -= 1
                        story.add_feedback("FAIL" if attempts2 > 0 else "You've lost!")
                    if attempts2 == 0:
                        running = False

        pygame.display.flip()

        # Delay before quitting if the challenge is completed successfully
        if correct2:
            story.add_feedback("Correct!")
            pygame.time.delay(3000)  # Keep "Correct!" message visible for 3 seconds
            running = False


    pygame.quit()


# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Decryptor Mini-Game")
font = pygame.font.Font(None, 28)
decryptor(screen, font)
pygame.quit()
