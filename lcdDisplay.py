"""
File: lcdDisplay.py
Last Modified: 7/1/1014

Handles communication with the LCD
"""

from RPLCD.i2c import CharLCD
from time import sleep

class LCDDisplay():
    def __init__(self):
        """
        Initialize the LCD and related data
        """
        self.rows = 2
        self.cols = 16
        self.lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=self.cols, rows=self.rows, dotsize=8)
        
        self.lcd.clear()
        self.lcd.backlight_enabled=True
        
        # Custom Char, Up Arrow
        self.up_arrow = (
            0b00000,
            0b00100,
            0b01110,
            0b10101,
            0b00100,
            0b00100,
            0b00100,
            0b00000,
        )
        self.up_arrow_code = 0
        self.lcd.create_char(self.up_arrow_code, self.up_arrow)
        
        # Custom Char, Down Arrow
        self.down_arrow = (
            0b00000,
            0b00100,
            0b00100,
            0b00100,
            0b10101,
            0b01110,
            0b00100,
            0b00000,
        )
        self.down_arrow_code = 1
        self.lcd.create_char(self.down_arrow_code, self.down_arrow)
        
        # Codes for pre-existing left and right arrows
        self.left_arrow_code = 0x7F
        self.right_arrow_code = 0x7E
    
    
    def clear(self):
        """
        Clear the LCD
        """
        self.lcd.clear()
    
    
    def write(self, text):
        """
        Write to the top left of the LCD
        
        text - The text to write
        """
        self.lcd.home()
        self.lcd.write_string(text)
        
        
    def write_cursor(self, text):
        """
        Write to the LCD at the current cursor position
        
        text - The text to write
        """
        self.lcd.write_string(text)
        
    
    def write_row(self, text, row):
        """
        Write to the specified row of the LCD
        
        text - The text to write
        row - The row (for a 16x2 display, either 0 or 1)
        """
        self.lcd.cursor_pos = (row, 0)
        self.lcd.write_string(text)
        
        
    def set_cursor(self, pos):
        """
        Set the position of the cursor
        
        pos - The position of the cursor (r, c)
        """
        self.lcd.cursor_pos = pos
        
    
    def write_special(self, code):
        """
        Write a special character to the LCD at the current cursor position
        
        code - The numerical code of the character
        """
        self.lcd.write(code)
        
   
    def close(self):
        """
        Close the LCD
        """
        self.lcd.close(clear=True)
    
