import i2c_lcd2004_driver as lcd_driver
from time import *

lcd = lcd_driver.lcd(0,1)
lcd.backlight(1) 
lcd.lcd_display_string("Eeenjoy", 1,7)
lcd.lcd_display_string("Hello, World!", 2, 5)
lcd.lcd_display_string("IIC/I2C LCD2004", 3, 4)
lcd.lcd_display_string("20 cols, 4 rows", 4, 4)

