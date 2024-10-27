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
from Firewall import pattern_recognition, maze_navigation, trigger_firewall_minigame
import random

from WinnerScreen import winner

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hacker Intro")
font = pygame.font.Font(pygame.font.get_default_font(), 18)

completed_games = set()
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

winning_line = ["ACCESS GRANTED: Welcome, Agent...",
    "System Breach Confirmed. Gaining Access to Corporate Data Servers...",
    "Security Clearance Level: 9 - Top Secret Access Enabled",
    "Decrypting Files...",
    "Loading Classified Data...",
    "",
    "Name: John Doe | Position: Head of R&D | ID: JDOE-937",
    "Email: john.doe@corporation.com | Phone: (555) 0198-273",
    "Last Login: 2024-10-23 14:35:12",
    " ",
    "Name: Sarah Blake | Position: Director of Finance | ID: SBLK-102",
    "Email: sarah.blake@corporation.com | Phone: (555) 0145-389",
    "Last Login: 2024-10-21 08:20:05",
    "",
    "Name: Dr. Eleanor Chen | Position: Chief Scientist | ID: ECHE-553",
    "Email: eleanor.chen@corporation.com | Phone: (555) 0179-552",
    "Last Login: 2024-10-20 17:58:30",
    "",
    "Warning: Security Protocol Activated!",
    "Routing through Secure Proxy... Masking IP Address...",
    "Accessing Financial Records... || Loading Sensitive Company Intelligence...",
    "File Download Complete. Exiting System...",
    "Mission Accomplished. Disconnecting from Network..."]

def main():
    global current_state
    pygame.display.set_caption("Hacking Game")
    home_menu = HomeScreenMenu(screen, completed_games)

    game_running = True
    last_firewall_trigger = pygame.time.get_ticks()
    game_start_time = pygame.time.get_ticks()

    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - game_start_time

        if elapsed_time > 300000:  # 5 minutes
            print("REACHED")
            game_running = False
            pygame.quit()
            sys.exit()

        elapsed_minutes = (elapsed_time // 60000) % 60
        elapsed_seconds = (elapsed_time // 1000) % 60
        timer_text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"  # Format as MM:SS

        # Check if we should trigger the firewall
        if current_time - last_firewall_trigger > 120000:  # 2 minutes in milliseconds
            last_firewall_trigger = current_time  # Update the last trigger time
            trigger_firewall_minigame(screen)  # Call the function to trigger the firewall

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            selected_mode = home_menu.handle_input(event)
            if selected_mode != 0:  # A game mode was selected
                current_state = selected_mode  # Update the state to the selected game

        home_menu.draw()

        # Render the timer text
        timer_surface = font.render(timer_text, True, (255, 255, 255))
        screen.blit(timer_surface, (10, 10))

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
                # call losing window

            completed_games.add(current_state)
            current_state = 0  # Reset back to home screen after game

        elif current_state == 2:
            print("Starting Game 2...")
            check_win2 = decryptor(screen, font)
            if not check_win2:
                print("REACHED")
                game_running = False
                pygame.quit()
                sys.exit()

            completed_games.add(current_state)
            current_state = 0  # Reset back to home screen after game

        elif current_state == 3:
            check_win2 = game(screen, font)
            if not check_win2:
                print("REACHED")
                game_running = False
                pygame.quit()
                sys.exit()

            completed_games.add(current_state)
            current_state = 0  # Reset back to home screen after game

        pygame.display.flip()

        if completed_games == {1, 2, 3}:
            game_running = False
            win_story = Story(screen, font, winning_line)
            winner(screen, font, win_story)

story = Story(screen, font, story_lines)
running_intro(screen, font, story_lines, main, story)
pygame.quit()
sys.exit()
