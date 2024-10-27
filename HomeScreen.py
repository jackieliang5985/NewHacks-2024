import pygame

class HomeScreenMenu:
    def __init__(self, screen, completed_tasks):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.button_rects = [
            pygame.Rect(250, 200, 300, 60),  # Button for Task 1
            pygame.Rect(250, 280, 300, 60),  # Button for Task 2
            pygame.Rect(250, 360, 300, 60)   # Button for Task 3
        ]
        self.mode_names = ["Task 1", "Task 2", "Task 3"]
        self.completed_tasks = completed_tasks

    def draw(self):
        self.screen.fill((0, 0, 50))  # Background color
        self.draw_text("Hacking into Ginky", 220, 150)
        self.draw_file_buttons()

    def draw_text(self, text, x, y):
        rendered_text = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(rendered_text, (x, y))

    def draw_file_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        for index, rect in enumerate(self.button_rects):
            if (index + 1) in self.completed_tasks:
                color = (100, 100, 100)
            else:
                color = (0, 200, 0) if rect.collidepoint(mouse_pos) else (0, 255, 0)

            pygame.draw.rect(self.screen, color, rect)

            # Center the text on the button
            text_surface = self.font.render(self.mode_names[index], True, (0, 0, 0))
            text_width, text_height = self.font.size(self.mode_names[index])
            text_x = rect.x + (rect.width - text_width) // 2
            text_y = rect.y + (rect.height - text_height) // 2

            self.screen.blit(text_surface, (text_x, text_y))

            if (index + 1) in self.completed_tasks:
                checkmark_surface = self.font.render("✔", True, (0, 255, 0))
                self.screen.blit(checkmark_surface, (rect.x + rect.width - 40, rect.y + 10))

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for index, rect in enumerate(self.button_rects):
                    if rect.collidepoint(event.pos) and (index + 1) not in self.completed_tasks:
                        return index + 1
        return 0
