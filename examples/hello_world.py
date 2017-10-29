from asukiaaa_py_i2c_lcd.core import I2cLcd, AQM1602_ADDR

I2C_BUS_NUM = 1

lcd = I2cLcd(I2C_BUS_NUM, AQM1602_ADDR)
lcd.setCursor(0,0)
lcd.write("Hello")
lcd.setCursor(3,1)
lcd.write("World")
