import pygame
from functools import partial
from Button import Button
class Menu:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.rect = pygame.Rect(0, 400, 160*4, 144*4)
        self.state = 0
        self.mainButtons = [
            Button(160*2, 400, 150, 40, "Luchar", partial(self.change_menu_state, newState=1)),
            Button(160*2, 500, 150, 40, "Pokemon", partial(self.change_menu_state, newState=2)),
            Button(160*3, 400, 150, 40, "Mochila", partial(self.change_menu_state, newState=3)),
            Button(160*3, 500, 150, 40, "Huir", partial(self.change_menu_state, newState=self.state))
        ]
    
    def handle_event(self, event, game):
        pass

    def change_menu_state(self, newState):
        if (self.state != newSate):
            self.state = newState
    
    def render(self, game):
        pygame.draw.rect(game.screen, (0,0,0), self.rect, 4)
        if self.state == 0:
            for button in self.mainButtons:
                button.render(game)
        elif self.state == 1:
            pass