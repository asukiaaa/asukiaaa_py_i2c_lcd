from asukiaaa_py_i2c_lcd.I2cLcd import I2cLcd

I2C_BUS_NUM = 1
I2C_LCD_ADDR = 0x3e

lcd = I2cLcd(I2C_BUS_NUM, I2C_LCD_ADDR)
lcd.setCursor(0,0)
lcd.write("Hello")
lcd.setCursor(3,1)
lcd.write("World")
