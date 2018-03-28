//----------------------------------------
// IDE: Arduino 1.8.0
// Connection:
// I2C_LCD2004 ------ arduino uno
//    VCC ---------------- 5V
//    GND ---------------- GND
//    SDA ---------------- A4
//    SCL ---------------- A5
//---------------------------------------
// include the library code
#include <LiquidCrystal_I2C.h>

//LiquidCrystal_I2C lcd(0x27,20,4);
LiquidCrystal_I2C lcd(0x3F,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup() 
{
    lcd.init();  //initialize the lcd
    lcd.backlight();  //open the backlight 
    
    lcd.setCursor ( 0, 0 );            // go to the top left corner
    lcd.print("      Eeeenjoy       "); // write this string on the top row
    lcd.setCursor ( 0, 1 );            // go to the 2nd row
    lcd.print("    Hello, World!    ");    
    lcd.setCursor ( 0, 2 );            
    lcd.print("   IIC/I2C LCD2004   "); 
    lcd.setCursor ( 0, 3 );            
    lcd.print("   20 cols, 4 rows   "); 
}

void loop() 
{

}

