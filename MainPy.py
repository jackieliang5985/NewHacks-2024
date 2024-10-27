import pygame
import sys

from SpeedType import game
from Decryptor import decryptor
from Functions import ips, important_ip
from PasswordCrack import play_game_1
from StartingScreen import Story
from Intro import running_intro
from HomeScreen import HomeScreenMenu
from Firewall import trigger_firewall_minigame
import random

from WinnerScreen import display

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hacker Intro")
font = pygame.font.Font(pygame.font.get_default_font(), 18)

completed_games = set()
MENU, GAME1, GAME2, GAME3 = range(4)
current_state = MENU


# Story lines for the intro
def load_lines_from_file(filename):
    lines = {}
    with open(filename, 'r') as file:
        current_section = None
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                current_section = line[2:]  # Remove the '#' and space
                lines[current_section] = []
            elif current_section:
                lines[current_section].append(line)
    return lines

# Load story lines from the combined text file
story_data = load_lines_from_file('story_data.txt')
story_lines = story_data['STORY LINES']
story_lines = [line.replace('{ips}', str(ips)) for line in story_lines]
winning_line = story_data['WINNING LINES']
losing_lines = story_data['LOSING LINES']
firewall_blocked_lines = story_data['FIREWALL BLOCKED LINES']

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
            lose_story = Story(screen, font, losing_lines)
            display(screen, font, lose_story)

        elapsed_minutes = (elapsed_time // 60000) % 60
        elapsed_seconds = (elapsed_time // 1000) % 60
        timer_text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"  # Format as MM:SS

        # Check if we should trigger the firewall
        if current_time - last_firewall_trigger > 60000:  # 1 minutes in milliseconds 60000
            last_firewall_trigger = current_time  # Update the last trigger time
            firewall_success = trigger_firewall_minigame(screen)  # Call the function to trigger the firewall

            if not firewall_success:  # If firewall mini-game failed
                game_running = False
                lose_story_by_firewall = Story(screen, font, firewall_blocked_lines)
                display(screen, font, lose_story_by_firewall)

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
                lose_story = Story(screen, font, losing_lines)
                display(screen, font, lose_story)

            completed_games.add(current_state)
            current_state = 0  # Reset back to home screen after game

        elif current_state == 2:
            print("Starting Game 2...")
            check_win2 = decryptor(screen, font)
            if not check_win2:
                print("REACHED")
                game_running = False
                lose_story = Story(screen, font, losing_lines)
                display(screen, font, lose_story)

            completed_games.add(current_state)
            current_state = 0  # Reset back to home screen after game

        elif current_state == 3:
            check_win2 = game(screen, font)
            if not check_win2:
                print("REACHED")
                game_running = False
                lose_story = Story(screen, font, losing_lines)
                display(screen, font, lose_story)

            completed_games.add(current_state)
            current_state = 0  # Reset back to home screen after game

        pygame.display.flip()

        if completed_games == {1, 2, 3}:
            game_running = False
            win_story = Story(screen, font, winning_line)
            display(screen, font, win_story)

story = Story(screen, font, story_lines)
running_intro(screen, font, story_lines, main, story)
pygame.quit()
sys.exit()
