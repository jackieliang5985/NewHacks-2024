import pygame
from Functions import important_ip
def running_intro(screen, font, story_lines, main, story):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            story.handle_input(event)

        screen.fill((0, 0, 0))
        story.update()
        story.draw()
        story.draw_input()

        if story.input_text.lower() == important_ip and len(story.finished_lines) == len(story.lines):
            main()

        pygame.display.flip()
