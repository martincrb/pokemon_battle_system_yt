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
            Button(160*2, 450, 150, 40, "Pokemon", partial(self.change_menu_state, newState=2)),
            Button(160*3, 400, 150, 40, "Mochila", partial(self.change_menu_state, newState=3)),
            Button(160*3, 450, 150, 40, "Huir", partial(self.change_menu_state, newState=4))
        ]
        self.attackButtons = []
    
    def handle_event(self, event, game):
        for button in self.mainButtons:
            button.handle_event(event, game)
        if self.state == 1:
            #Build and store attack buttons if first time
            if len(self.attackButtons) == 0:
                for idx, attack in enumerate(game.pokemon1.attacks):
                    functionTurn = partial(game.makeTurn, index=idx)
                    self.attackButtons.append(
                        Button(idx*160, 400, 150, 40, attack.name, functionTurn)
                    )
            for button in self.attackButtons:
                button.handle_event(event, game)

    def change_menu_state(self, newState):
        if (self.state == 1 and newState != 1):
            #ANY button clicked when LUCHAR MODE is ON, go BACK
            self.state = 0
            for button in self.mainButtons:
                button.enable()
        else:
            self.state = newState   
            for button in self.mainButtons:
                button.disable()    
    
    def render(self, game):
        #pygame.draw.rect(game.screen, (0,0,0), self.rect, 4)
        for button in self.mainButtons:
            button.render(game)
        if self.state == 1:
            #Draw attack buttons
            for button in self.attackButtons:
                button.render(game)