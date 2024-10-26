# Functions.py

import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.Font(pygame.font.get_default_font(), 18)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

input_text = ''
output_text = []
commands = ["help", "scan", "connect", "exit"]
current_node = None
available_ips = []

def draw_text(text, x, y, color=WHITE):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        screen.blit(line_surface, (x, y + i * 20))

# Function to generate random IPs
def generate_random_ips(count=3):
    ip_list = []
    for _ in range(count):
        ip = f"{random.randint(192, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
        ip_list.append(ip)
    return ip_list


ips = generate_random_ips()
important_ip = random.choice(ips)

def process_command(command):
    global current_node, available_ips, output_text
    parts = command.split()
    cmd = parts[0]

    if cmd == "help":
        output_text.append("Available commands:")
        output_text.append(" - help: Show this help message")
        output_text.append(" - scan: Scan for available networks")
        output_text.append(" - connect [IP]: Connect to a node")
        output_text.append(" - exit: Quit the simulator")

    elif cmd == "scan":
        available_ips = generate_random_ips()
        output_text.append("Scanning for networks...")
        output_text.append("Found nodes: " + ", ".join(available_ips))

    elif cmd == "connect":
        if len(parts) < 2:
            output_text.append("Error: No IP address provided.")
        else:
            ip = parts[1]
            if ip in available_ips:
                output_text.append(f"Connecting to {ip}...")
                current_node = ip
            else:
                output_text.append(f"Error: IP {ip} not found in network scan.")

    elif cmd == "exit":
        pygame.quit()
        sys.exit()

    else:
        output_text.append(f"Unknown command: {cmd}")

    if len(output_text) > 20:
        output_text.pop(0)
