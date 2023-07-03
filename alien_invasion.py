import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet 
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    
    def __init__(self):
        """Initialize tha game, and create game resources."""
        # Initializes game.
        pygame.init()
        
        #Initializes settings.
        self.settings = Settings()
        
        # Sets screen resolution of game so it plays in fullscreen.
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
        
        # Because we don't know your monitor resolution ahead of time, we update these settings after
        # the screen has been created, using width and height attributes of the screen's rect to 
        # update the settings object. It works by checking the width and height of the monitor when
        # it is in fullscreen mode, because that is what the monitor resolution will be.
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        # Sets the window caption.
        pygame.display.set_caption("Alien Invasion")
        
        # Initializes an instance of a ship.
        self.ship = Ship(self)
        
        # Initializes somewhere to store bullets.
        self.bullets = pygame.sprite.Group()
        
        # Initializes somewhere to store aliens.
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                # Quits game.
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                # Events if a key is pressed.
                self.check_keydown_events(event)
                                
            
            elif event.type == pygame.KEYUP:
                # Events if a key stops being pressed.
                self.check_keyup_events(event)
                        
    
    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
                    
        if event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True
            
        elif event.key == pygame.K_q:
            # Exits the game if Q key is pressed.
            sys.exit()
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Stops right movement.
            self.ship.moving_right = False
                    
        if event.key == pygame.K_LEFT:
            # Stops left movement.
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            # Creates a new bullet.
            new_bullet = Bullet(self)
        
            # Adds that new bullet to the group of bullets.
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
            
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()        
        


    def _check_bullet_alien_collisions(self):
        """Respond the bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
        
        
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
          then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!")

                             
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Fills screen with colour.
        self.screen.fill(self.settings.bg_colour) 
        
        # Makes character/object visible
        self.ship.blitme() 
        
        # Draws bullets in the bullets group
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Draws aliens in the aliens group.
        self.aliens.draw(self.screen)
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()





pygame.quit()

if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()