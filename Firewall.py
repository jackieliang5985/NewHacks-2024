import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def pattern_recognition(screen):
    pattern_length = random.randint(3, 6)  # Length of the pattern
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    pattern = random.sample(colors, pattern_length)  # Random color pattern

    screen.fill(BLACK)
    for i, color in enumerate(pattern):
        pygame.draw.rect(screen, pygame.Color(color), (100 + i * 100, 250, 80, 80))

    pygame.display.flip()
    pygame.time.delay(2000)
    screen.fill(BLACK)
    pygame.display.flip()

    player_pattern = []
    input_text = ''

    while len(player_pattern) < pattern_length:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text in colors:
                        player_pattern.append(input_text)
                        input_text = ''
                    else:
                        print("Invalid color! Please try again.")
                        input_text = ''

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    input_text += event.unicode

        screen.fill(BLACK)

        font = pygame.font.Font(None, 36)
        input_surface = font.render(f"Current Input: {input_text}", True, WHITE)
        screen.blit(input_surface, (100, 350))

        guessed_pattern_surface = font.render(f"Guessed Pattern: {', '.join(player_pattern)}", True, WHITE)
        screen.blit(guessed_pattern_surface, (100, 400))

        pygame.display.flip()

    if player_pattern == pattern:
        print("Access Granted!")
        return True
    else:
        print(f"Access Denied! The correct pattern was: {', '.join(pattern)}")
        return False


def maze_navigation(screen):
    maze = [
        "#########",
        "#       #",
        "# ##### #",
        "# #     #",
        "# # ### #",
        "#       #",
        "#########",
    ]

    player_pos = [1, 1]
    exit_pos = [5, 1]
    maze_height = len(maze)
    maze_width = len(maze[0])
    def draw_maze():
        for y in range(maze_height):
            for x in range(maze_width):
                if maze[y][x] == "#":
                    pygame.draw.rect(screen, (255, 255, 255), (x * 80, y * 80, 80, 80))
                if (y, x) == (player_pos[0], player_pos[1]):
                    pygame.draw.rect(screen, GREEN, (x * 80, y * 80, 80, 80))
                if (y, x) == (exit_pos[0], exit_pos[1]):
                    pygame.draw.rect(screen, RED, (x * 80, y * 80, 80, 80))

    running = True
    while running:
        screen.fill(BLACK)
        draw_maze()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and maze[player_pos[0] - 1][player_pos[1]] != "#":
                    player_pos[0] -= 1
                elif event.key == pygame.K_DOWN and maze[player_pos[0] + 1][player_pos[1]] != "#":
                    player_pos[0] += 1
                elif event.key == pygame.K_LEFT and maze[player_pos[0]][player_pos[1] - 1] != "#":
                    player_pos[1] -= 1
                elif event.key == pygame.K_RIGHT and maze[player_pos[0]][player_pos[1] + 1] != "#":
                    player_pos[1] += 1

                if player_pos == exit_pos:
                    print("You have reached the exit! Access Granted!")
                    return True

    return False
