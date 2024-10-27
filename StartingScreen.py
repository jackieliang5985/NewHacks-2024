import pygame

class Story:
    def __init__(self, screen, font, lines, delay=50, max_visible_lines=15):
        self.screen = screen
        self.font = font
        self.lines = lines
        self.delay = delay
        self.max_visible_lines = max_visible_lines  # Max lines to display on screen at once
        self.line_index = 0
        self.char_index = 0
        self.last_time = pygame.time.get_ticks()
        self.finished_lines = []
        self.scroll_offset = 0  # Track scroll position
        self.input_text = ""

    def update(self):
        # Check if it's time to reveal the next character
        if pygame.time.get_ticks() - self.last_time > self.delay:
            self.last_time = pygame.time.get_ticks()
            if self.line_index < len(self.lines):
                current_line = self.lines[self.line_index]
                self.char_index += 1
                if self.char_index > len(current_line):
                    # Move to the next line when current line is fully displayed
                    self.finished_lines.append(current_line)
                    self.line_index += 1
                    self.char_index = 0

                    # Scroll up if there are more lines than max_visible_lines
                    if len(self.finished_lines) > self.max_visible_lines:
                        self.scroll_offset += 1  # Move the view up one line

    def draw(self):
        y_offset = 20  # Initial y position for lines
        start_line = self.scroll_offset  # Start from the top of the scroll
        visible_lines = self.finished_lines[start_line:start_line + self.max_visible_lines]

        # Draw each visible line
        for i, line in enumerate(visible_lines):
            self.screen.blit(self.font.render(line, True, (0, 255, 0)), (50, y_offset + i * 30))

        # Display the current line's characters as they are typed
        if self.line_index < len(self.lines):
            current_text = self.lines[self.line_index][:self.char_index]
            self.screen.blit(self.font.render(current_text, True, (0, 255, 0)),
                             (30, y_offset + len(visible_lines) * 30))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(f"User input: {self.input_text}")
                # self.input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

    def draw_input(self):
        input_surface = self.font.render(f"> {self.input_text}", True, (0, 255, 0))
        self.screen.blit(input_surface, (50, 500))
