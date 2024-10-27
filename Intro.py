import pygame
from Functions import important_ip
def running_intro(screen, font, story_lines, main, story):
    pygame.mixer.init()
    pygame.mixer.music.load('hackermusic.mp3')  # Update this with your actual path
    pygame.mixer.music.set_volume(10)  # Set volume to 50%
    pygame.mixer.music.play(-1)  # Play the music indefinitely
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

        if story.input_text.lower() == 'hi' or len(story.finished_lines) == len(story.lines):
            main()

        pygame.display.flip()
