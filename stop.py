import board
import busio
import time
import Adafruit_PCA9685
import adafruit_bno055

STOP = 320
esc = Adafruit_PCA9685.PCA9685()
esc.set_pwm_freq(50)
esc.set_all_pwm(0, STOP)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

esc.set_all_pwm(0, STOP) 
