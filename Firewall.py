import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def pattern_recognition(screen):
    pattern_length = random.randint(2, 4)
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    pattern = random.sample(colors, pattern_length)

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


def generate_maze(width, height):
    # Create a grid of walls
    maze = [["#" for _ in range(width)] for _ in range(height)]

    # Directions for moving in the maze
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    # Recursive function to generate the maze
    def carve_passages_from(x, y):
        random.shuffle(directions)  # Randomize directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == "#":
                maze[y + dy // 2][x + dx // 2] = " "  # Carve a path
                maze[ny][nx] = " "  # Carve the next cell
                carve_passages_from(nx, ny)  # Recursively carve from the new cell

    # Start carving from the initial position
    maze[1][1] = " "  # Starting point
    carve_passages_from(1, 1)

    maze[1][1] = " "  # Start position
    maze[height - 2][1] = " "  # Exit position
    return maze


def maze_navigation(screen):
    width, height = 21, 15  # Define the maze size (width, height) - odd numbers for walls
    maze = generate_maze(width, height)  # Generate the maze

    player_pos = [1, 1]  # Starting position (1, 1)
    exit_pos = [height - 2, 1]  # Exit position at the bottom

    def draw_maze():
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[y][x] == "#":
                    pygame.draw.rect(screen, WHITE, (x * 40, y * 40, 40, 40))  # Walls
                if (y, x) == (player_pos[0], player_pos[1]):
                    pygame.draw.rect(screen, RED, (x * 40, y * 40, 40, 40))  # Player
                if (y, x) == (exit_pos[0], exit_pos[1]):
                    pygame.draw.rect(screen, GREEN, (x * 40, y * 40, 40, 40))  # Exit
# Timer
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        remaining_time = max(0, 15 - elapsed_time)
        font = pygame.font.Font(pygame.font.get_default_font(), 26)  # Choose font size
        time_surface = font.render(f"Time Remaining: {int(remaining_time)}s", True, (0, 255, 0))
        screen.blit(time_surface, (10, 10))

    start_ticks = pygame.time.get_ticks()
    running = True
    while running:
        screen.fill(BLACK)
        draw_maze()
        pygame.display.flip()

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # seconds
        if elapsed_time > 15:  # 15 sec limit
            print("Time's up! Access Denied!")
            return False

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

                if player_pos == exit_pos:  # Exit position
                    print("You have reached the exit! Access Granted!")
                    return True  # Successfully navigated the maze

    return False  # Player did not reach the exit
