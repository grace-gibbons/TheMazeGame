"""
File: mazeGame.py
Last Modified: 7/1/1014

Runs The Maze Game, a game where the player must make it to the end of a maze, utilizing the Raspberry Pi and other hardware
Refer to the README for further details 
"""

from mazeGenerator import MazeGenerator
from matrixDisplay import Matrix
from userInput import InputHandler
from lcdDisplay import LCDDisplay
from gameHandler import GameHandler

import RPi.GPIO as IO

if __name__ == "__main__":
    # Starting maze location
    start_x = 0
    start_y = 7

    # Size of the maze
    size = 8
    
    IO.setwarnings(False)
    IO.setmode(IO.BCM) #Allows us to use Rpi GPIO pin numbers
    
    lcd = LCDDisplay()
    
    input_handler = InputHandler()
    
    # Main Game Loop
    while True:
        # Create some 8x8 maze, 
        maze_gen = MazeGenerator(size)
        maze_gen.create_graph()
        maze_gen.generate_maze()
        #maze_gen.draw_maze() # For debbuging/testing use
        
        # Initialize the matrix
        matrix = Matrix()
        matrix.light(start_x, start_y)
        
        # Create/Reset handler
        game_handler = GameHandler(size, start_x, start_y)
        
        #Begin Game
        lcd.clear()
        lcd.write("The Maze Game")
        lcd.write_row("Press any Button", 1)

        #Press any button to continue
        while True:
            # Quit command
            if input_handler.is_quit():
                lcd.close()
                matrix.reset()
            
            if input_handler.get_input() == -1:
                continue
            else:
                break
        
        # Game Loop
        while True:
            # Display room info on lcd
            game_handler.room_text(lcd, maze_gen)
            
            if game_handler.is_goal():
                break
            
            # Get input, break when input to update lcd
            while True:
                moved = game_handler.move(input_handler, matrix, maze_gen)
                if moved:
                    break
                
        # Display room info on lcd
        lcd.clear()
        lcd.write("You Win! Coins:" + str(game_handler.treasure))
        lcd.write_row("Moves: " + str(game_handler.moves), 1)
        
        #Press any button to continue
        while True:
            if input_handler.get_input() == -1:
                continue
            else:
                break 
    
                
    
    
    
