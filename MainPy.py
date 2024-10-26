import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hack In")

font = pygame.font.Font(pygame.font.get_default_font(), 18)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

input_text = ''
output_text = []
commands = ["help", "scan", "connect", "exit"]
current_node = None
def draw_text(text, x, y, color=WHITE):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        screen.blit(line_surface, (x, y + i * 20))


def process_command(command):
    global current_node
    parts = command.split()
    cmd = parts[0]

    if cmd == "help":
        output_text.append("Available commands:")
        output_text.append(" - help: Show this help message")
        output_text.append(" - scan: Scan for available networks")
        output_text.append(" - connect [IP]: Connect to a node")
        output_text.append(" - exit: Quit the simulator")

    elif cmd == "scan":
        output_text.append("Scanning for networks...")
        output_text.append("Found nodes: 192.168.1.10, 192.168.1.15")

    elif cmd == "connect":
        if len(parts) < 2:
            output_text.append("Error: No IP address provided.")
        else:
            ip = parts[1]
            output_text.append(f"Connecting to {ip}...")
            current_node = ip

    elif cmd == "exit":
        pygame.quit()
        sys.exit()

    else:
        output_text.append(f"Unknown command: {cmd}")

    if len(output_text) > 20:
        output_text.pop(0)

running = True
while running:
    screen.fill(BLACK)

    for i, line in enumerate(output_text):
        draw_text(line, 10, 10 + i * 20, GREEN)

    draw_text(f"> {input_text}", 10, SCREEN_HEIGHT - 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                process_command(input_text)
                input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
    pygame.display.flip()

pygame.quit()
