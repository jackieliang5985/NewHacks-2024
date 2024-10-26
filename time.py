import pygame
import time

# Define the words list
WORDS = ['computer', 'student', 'newhacks', 'apple',
         'basketball', 'soccer', 'hacker', 'hat',
         'headphones', 'camera']


# Story class for handling text display
class Story:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.lines = []
        self.line_index = 0
        self.last_time = pygame.time.get_ticks()
        self.delay = 500  # Delay for text animation

    def update(self):
        if self.line_index < len(self.lines):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_time > self.delay:
                self.last_time = current_time
                self.line_index += 1

    def draw(self):
        y_offset = 20
        for i in range(self.line_index):
            self.screen.blit(self.font.render(self.lines[i], True, (0, 255, 0)), (50, y_offset + i * 30))

    def add_line(self, line):
        self.lines.append(line)


def game(screen, font):
    story = Story(screen, font)
    story.add_line("The standardized typing test: type each word which appears...")
    story.add_line("Type 'ready' to begin...")

    input_text = ""
    waiting_for_input = True

    while True:
        screen.fill((0, 0, 0))  # Clear screen
        story.update()  # Update the story
        story.draw()  # Draw the story lines

        # Draw the current input
        input_surface = font.render(f"Input: {input_text}", True, (0, 255, 0))
        screen.blit(input_surface, (50, 550))

        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if waiting_for_input:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text.lower() == 'ready':
                            story.add_line("Game starting...")
                            waiting_for_input = False
                            time.sleep(1)  # Pause before starting the game
                            words(screen, font, story)
                        else:
                            story.add_line("Please type 'ready' to start.")
                            input_text = ""  # Clear input if not ready
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]  # Remove last character
                    else:
                        input_text += event.unicode  # Append the new character


def words(screen, font, story):
    for word in WORDS:
        # Only add the prompt for the current word once
        story.add_line(f"Type the word: {word}")
        answer = timer(word, 3, screen, font, story)

        # Check if the answer is incorrect
        if answer.strip().lower() != word:
            story.add_line("INCORRECT, YOU HAVE BEEN COMPROMISED!")
            break
    else:
        story.add_line("SUCCESS! YOU HAVE PASSED THE TYPING TASK.")

    # Display the final message
    while True:
        screen.fill((0, 0, 0))  # Clear screen
        story.update()  # Update the story
        story.draw()  # Draw the story lines
        pygame.display.flip()  # Update the display
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Add a short delay before closing the game
        time.sleep(2)
        pygame.quit()  # Close the window
        exit()


def timer(wordie, time, screen, font, story):
    # Display the word to type
    pygame.display.flip()

    input_text = ""
    start_time = pygame.time.get_ticks()

    while True:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert to seconds
        if elapsed_time >= time:
            story.add_line("YOU RAN OUT OF TIME AND HAVE BEEN COMPROMISED!!")
            return ""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text  # Return the typed input
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Remove last character
                else:
                    input_text += event.unicode  # Append the new character

        # Display current input
        screen.fill((0, 0, 0))  # Clear screen
        story.update()  # Update the story
        story.draw()  # Draw the story lines
        input_surface = font.render(f"Input: {input_text}", True, (0, 255, 0))
        screen.blit(input_surface, (50, 550))
        pygame.display.flip()  # Update the display


# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Typing Task")
font = pygame.font.Font(None, 36)
game(screen, font)
pygame.quit()
