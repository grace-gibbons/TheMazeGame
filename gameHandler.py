"""
File: gameHandler.py
Last Modified: 7/1/1014

Handles updating and gathering information during a run of the game
"""

import directions as DIR

class GameHandler():
    def __init__(self, size, x, y):
        """
        Initialize the GameHandler
        
        size - The size of the maze
        x - Current x coordinate of the player
        y - Current y coordinate of the player
        """
        self.size = size
        self.x = x
        self.y = y
        self.treasure = 0
        self.moves = 0 
    
    
    def move(self, input_handler, matrix, maze_gen):
        """
        Move the player through the maze and update the matrix
        
        input_handler - Handles gathering input through the controller
        matrix - The matrix grid
        maze_gen - Stores maze data
        """
        direction = input_handler.get_input()
        
        if direction == DIR.left_dir and maze_gen.maze[self.x][self.y].has_left_connection():
            if self.x > 0:
                self.x -= 1
            else:
                self.x = self.size - 1
        
            matrix.light(self.x, self.y)
        elif direction == DIR.right_dir and maze_gen.maze[self.x][self.y].has_right_connection():
            if self.x < self.size - 1:
                self.x += 1
            else:
                self.x = 0
            
            matrix.light(self.x, self.y)
        elif direction == DIR.up_dir and maze_gen.maze[self.x][self.y].has_top_connection():
            if self.y > 0:
                self.y -= 1
            else:
                self.y = self.size - 1
                
            matrix.light(self.x, self.y)
        elif direction == DIR.down_dir and maze_gen.maze[self.x][self.y].has_bottom_connection():
            if self.y < self.size - 1:
                self.y += 1
            else:
                self.y = 0
                
            matrix.light(self.x, self.y)
        else:
            return False
        self.moves += 1
        return True
    
    
    def __write_dirs(self, lcd, maze_gen):
        """
        Determine which directions the player can travel and write them to the LCD
        
        lcd - The LCD
        maze_gen - Stores maze data
        """
        lcd.write_row("Dirs: ", 1)
        
        if maze_gen.maze[self.x][self.y].has_left_connection():
            lcd.write_special(lcd.left_arrow_code)
        
        if maze_gen.maze[self.x][self.y].has_right_connection():
            lcd.write_special(lcd.right_arrow_code)
        
        if maze_gen.maze[self.x][self.y].has_bottom_connection():
            lcd.write_special(lcd.down_arrow_code)
        
        if maze_gen.maze[self.x][self.y].has_top_connection():
            lcd.write_special(lcd.up_arrow_code)
            
            
    def room_text(self, lcd, maze_gen):
        """
        Update the room text displayed to the LCD
        """
        lcd.clear()
        lcd.write("Room (" + str(self.x) + "," + str(self.y) + ")")
        
        if maze_gen.maze[self.x][self.y].has_treasure:
            lcd.write_cursor(" Coin!")
            maze_gen.maze[self.x][self.y].has_treasure = False
            self.treasure += 1
        
        self.__write_dirs(lcd, maze_gen)
            
        lcd.set_cursor((1, 12))
        lcd.write_cursor("C: " + str(self.treasure))


    def is_goal(self):
        """
        Check if the player has reached the destination room
        
        Returns true if player at goal and false otherwise
        """
        if self.x == self.size - 1 and self.y == 0:
            return True
        else:
            return False
        
        
        
