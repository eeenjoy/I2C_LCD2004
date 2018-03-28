import smbus
from time import *

# LCD Address
#ADDRESS = 0x27
ADDRESS = 0x3F

# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00
# set init LCD BACKLIGHT ON or OFF
def lcd_backlight(lcdbl=1):
    if lcdbl == 0 :
        return LCD_NOBACKLIGHT
    return LCD_BACKLIGHT

En = 0b00000100 # Enable bit
Rw = 0b00000010 # Read/Write bit
Rs = 0b00000001 # Register select bit

class lcd(object):
    #initializes objects and lcd
    def __init__(self,lcd_bl,port=1):
        self.addr = ADDRESS
        self.bus = smbus.SMBus(port)
        self.lcd_bl = lcd_bl
        
        self.lcd_write(0x03)
        self.lcd_write(0x03)
        self.lcd_write(0x03)
        self.lcd_write(0x02)
                
        self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
        self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
        self.lcd_write(LCD_CLEARDISPLAY)   
        self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
        sleep(0.2)   

    def backlight(self,set_lcdbl):
        self.lcd_bl = set_lcdbl
    
    # clocks EN to latch command
    def lcd_strobe(self, data):
        self.write_cmd(data | En | lcd_backlight(self.lcd_bl))
        sleep(.0005)
        self.write_cmd(((data & ~En) | lcd_backlight(self.lcd_bl)))
        sleep(.0001)   

    def lcd_write_four_bits(self, data):
        self.write_cmd(data | lcd_backlight(self.lcd_bl))
        self.lcd_strobe(data)

    # write a command to lcd
    def lcd_write(self, cmd, mode=0):
        self.lcd_write_four_bits(mode | (cmd & 0xF0))
        self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))

    # put string function
    def lcd_display_string(self, string, raw=1, col=1):
        if raw == 1:
            self.lcd_write(0x80+col-1)
        if raw == 2:
            self.lcd_write(0xC0+col-1)
        if raw == 3:
            self.lcd_write(0x94+col-1)
        if raw == 4:
            self.lcd_write(0xD4+col-1)

        for char in string:
            self.lcd_write(ord(char), Rs)

    # clear lcd and set to home
    def lcd_clear(self):
        self.lcd_write(LCD_CLEARDISPLAY)
        self.lcd_write(LCD_RETURNHOME)

    # Write a single command
    def write_cmd(self, cmd):
        self.bus.write_byte(self.addr, cmd)
        sleep(0.0001)
