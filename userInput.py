"""
File: userInput.py
Last Modified: 7/1/1014

Detects input from a game controller
"""

from time import sleep
import directions as DIR

import pygame

class InputHandler():
    def __init__(self):
        """
        Initialize the game controller
        """
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        
    
    def get_input(self):
        """
        Get input direction based on button press or hat values
        """
        pygame.event.get()
        
        # Buttons
        if self.controller.get_button(0):
            sleep(0.25)
            return DIR.down_dir
        elif self.controller.get_button(1):
            sleep(0.25)
            return DIR.left_dir
        elif self.controller.get_button(2):
            sleep(0.25)
            return DIR.right_dir
        elif self.controller.get_button(3):
            sleep(0.25)
            return DIR.up_dir
        # Hat input
        elif self.controller.get_hat(0)[0] < 0:
            sleep(0.25)
            return DIR.left_dir
        elif self.controller.get_hat(0)[0] > 0:
            sleep(0.25)
            return DIR.right_dir
        elif self.controller.get_hat(0)[1] < 0:
            sleep(0.25)
            return DIR.down_dir
        elif self.controller.get_hat(0)[1] > 0:
            sleep(0.25)
            return DIR.up_dir
        else:
            return -1
        
        
    def is_quit(self):
        """
        Check if the quit button has been pressed
        
        Returns true for quit, false otherwise
        """
        pygame.event.get()
        
        if self.controller.get_button(8):
            return True
        