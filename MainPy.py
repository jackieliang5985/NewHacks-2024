import pygame
import sys
from StartingScreen import Story
from Intro import running_intro
from HomeScreen import HomeScreenMenu
from Firewall import pattern_recognition, maze_navigation
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hacker Intro")
font = pygame.font.Font(pygame.font.get_default_font(), 18)

completed_games = []
MENU, GAME1, GAME2, GAME3 = range(4)
current_state = MENU

# Story lines for the intro
story_lines = [
    "Connecting to secure network...",
    "Authentication successful.",
    "Welcome, Agent X.",
    "Current mission: Infiltrate the mainframe of Ginky CO.",
    "Gather all classified data and avoid detection.",
    "Type 'start' to begin your mission..."
]

def main():
    global current_state
    pygame.display.set_caption("Hacking Game")
    home_menu = HomeScreenMenu(screen)


    game_running = True
    while game_running:

        # Randomly trigger the firewall
        if random.randint(0, 500) < 5:  # 5% chance to trigger firewall
            game_selected = random.choice([pattern_recognition, maze_navigation])

            if game_selected(screen):
                print("Firewall bypassed!")
            else:
                game_running = False
                pygame.quit()
                sys.exit()
                #print("Failed to bypass the firewall!")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            selected_mode = home_menu.handle_input(event)
            if selected_mode != 0:  # A game mode was selected
                current_state = selected_mode  # Update the state to the selected game

        home_menu.draw()
        pygame.display.flip()

        # Add game handling logic based on current_state
        if current_state == 1:
            print("Starting Game 1...")
            # Call game 1 function or logic here
            current_state = 0  # Reset back to home screen after game
        elif current_state == 2:
            print("Starting Game 2...")
            # Call game 2 function or logic here
            current_state = 0  # Reset back to home screen after game
        elif current_state == 3:
            print("Starting Game 3...")
            # Call game 3 function or logic here
            current_state = 0  # Reset back to home screen after game

        pygame.display.flip()

story = Story(screen, font, story_lines)
running_intro(screen, font, story_lines, main, story)
pygame.quit()
sys.exit()
