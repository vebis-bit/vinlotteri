import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


class Button():
    """Creat)e a button, then blit the surface in the while loop"""

    def __init__(self, parent, text,  pos, font, bg="black", feedback="text"):
        self.parent = parent
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text when you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="green")

    def click2(self,event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.parent.chose_the_winner()


