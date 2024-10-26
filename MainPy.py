import pygame
import sys
from Functions import screen, draw_text, process_command, BLACK, GREEN, SCREEN_HEIGHT, output_text

pygame.init()

running = True
input_text = ''

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
sys.exit()
