import pygame
import time

def display(screen, font, story):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            story.handle_input(event)

        screen.fill((0, 0, 0))  # Clear screen
        story.update()  # Update story to display text gradually
        story.draw()  # Draw the story text to the screen
        pygame.display.flip()  # Refresh the display

        # Check if all lines have been displayed
        if story.line_index >= len(story.lines):
            time.sleep(2)  # Brief pause to allow reading
            running = False

    pygame.quit()  # Close the window