import SURFLibrary 
from SURFLibrary.functions import cf_functions

left = cf_functions.motor(2)

left.set(330)
time.sleep(1)
left.set(320)
