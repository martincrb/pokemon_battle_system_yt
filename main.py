# -*- coding: utf-8 -*-

from Game import *

def main():
    game = Game()
    while not game.stopped:
        #Main pokemon battle loop
        #First ask for the commands
        game.process()
        game.render()
        
if __name__ == "__main__":
    main()