import pygame
import sys
from StartingScreen import Story
from Intro import running_intro
from HomeScreen import HomeScreenMenu

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
    pygame.display.set_caption("Hacking Game")

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if current_state == MENU:
            home = HomeScreenMenu(screen)

        elif current_state == GAME1:
            "run game 1"
            print("game1")

        elif current_state == GAME2:
            "run game 2"
            print("game2")

        pygame.display.flip()

story = Story(screen, font, story_lines)
running_intro(screen, font, story_lines, main, story)
pygame.quit()
sys.exit()