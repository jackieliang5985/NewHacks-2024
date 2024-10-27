from tabnanny import check

import pygame
import sys

from SpeedType import game
from Decryptor import decryptor
from Functions import ips, important_ip
from PasswordCrack import play_game_1
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
    f"Identifying vulnerable IPs... {ips}",
    "These weak points are your gateways. Proceed with caution.",
    "Gather all classified data and avoid detection.",
    "Attempt to connect to the correct IP to begin your mission..."
]

def main():
    global current_state
    pygame.display.set_caption("Hacking Game")
    home_menu = HomeScreenMenu(screen)

    game_running = True
    last_firewall_trigger = pygame.time.get_ticks()  # Initialize the timer

    while game_running:
        current_time = pygame.time.get_ticks()  # Get current time

        # Randomly trigger the firewall every 2 Mins (20000 milliseconds)
        if current_time - last_firewall_trigger > 120000:  # Check if 2 Mins have passed
            last_firewall_trigger = current_time  # Reset the timer
            game_selected = random.choice([pattern_recognition, maze_navigation])

            if game_selected(screen):
                print("Firewall bypassed!")
            else:
                game_running = False
                pygame.quit()
                sys.exit()
                # print("Failed to bypass the firewall!")

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
            check_win1 = play_game_1()
            if not check_win1:
                print("REACHED")
                game_running = False
                pygame.quit()
                sys.exit()
                #call losing window

            completed_games.append(current_state)
            current_state = 0  # Reset back to home screen after game

        elif current_state == 2:
            print("Starting Game 2...")
            check_win2 = decryptor(screen, font)
            if not check_win2:
                print("REACHED")
                game_running = False
                pygame.quit()
                sys.exit()

            completed_games.append(current_state)
            current_state = 0  # Reset back to home screen after game

        elif current_state == 3:
            check_win2 = game(screen, font)
            if not check_win2:
                print("REACHED")
                game_running = False
                pygame.quit()
                sys.exit()

            completed_games.append(current_state)
            current_state = 0  # Reset back to home screen after game

        pygame.display.flip()

        if 1 in completed_games and 2 in completed_games and 3 in completed_games:
            game_running = False
            #winner screen

story = Story(screen, font, story_lines)
running_intro(screen, font, story_lines, main, story)
pygame.quit()
sys.exit()
