class Settings:
    
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_colour = (230,230,230)
        
        # Ship settings.
        # Moves position by 1.5 pixels.
        self.ship_speed = 1.5 
        
        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3