import pygame
import sys


class BlueSky:
    
    def __init__(self):
        pygame.init() #initializes
        self.screen = pygame.display.set_mode((2560, 1440)) #sets game resolution to 1440p
        self.boss = BigBoss(self)

    
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
        self.screen.fill(color="white") #fills screen with blue colour
        self.boss.blitme()
        
        pygame.display.flip() #displays the most recently filled screen 
        
class BigBoss:
    
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        self.image = pygame.image.load("images/bigboss.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

        


nu = BlueSky()
nu.run_game()
        

    
    
    