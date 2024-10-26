import pygame

class HomeScreenMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.button_rects = [
            pygame.Rect(250, 200, 300, 60),  # Button for Game 1
            pygame.Rect(250, 280, 300, 60),  # Button for Game 2
            pygame.Rect(250, 360, 300, 60)  # Button for Game 3
        ]
        self.mode_names = ["Task 1", "Task 2", "Task 3"]

    def draw(self):
        self.screen.fill((0, 0, 50))  # Background color
        self.draw_text("Hacking into Ginky", 220, 150)
        self.draw_file_buttons()

    def draw_text(self, text, x, y):
        rendered_text = self.font.render(text, True, (0, 255, 0))  # Green text
        self.screen.blit(rendered_text, (x, y))

    def draw_file_buttons(self):
        for index, rect in enumerate(self.button_rects):
            pygame.draw.rect(self.screen, (0, 255, 0), rect)

            # Center the text on the button
            text_surface = self.font.render(self.mode_names[index], True, (0, 0, 0))  # Black text for contrast
            text_width, text_height = self.font.size(self.mode_names[index])
            text_x = rect.x + (rect.width - text_width) // 2
            text_y = rect.y + (rect.height - text_height) // 2

            # Draw the text on top of the button
            self.screen.blit(text_surface, (text_x, text_y))

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for index, rect in enumerate(self.button_rects):
                    if rect.collidepoint(event.pos):
                        return index + 1
        return 0