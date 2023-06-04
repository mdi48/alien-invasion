import pygame
import sys

class BlueSky:
    
    def __init__(self):
        pygame.init() #initializes
        self.screen = pygame.display.set_mode((1920, 1080)) #sets game resolution to 1080p

    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
                    
                        
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #exits if exit button is pressed
    
    def _update_screen(self):
        self.screen.fill(color="blue") #fills screen with blue colour
        
        pygame.display.flip() #displays the most recently filled screen 
        


game = BlueSky()
game.run_game()
        