import neopixel
import machine
import time
import uos
import ustruct

bright = 5
ledsCount = 8
speed = 15
speed = 1/speed
wait = 1

np = neopixel.NeoPixel(machine.Pin(4), ledsCount)

def random_color(max_value):	
	i = ustruct.unpack('i', uos.urandom(1))
	random = int((i[0]/255) * max_value)
	return random

while True:
	color_r = random_color(bright)
	color_g = random_color(bright)
	color_b = random_color(bright)
	for pixel in range(ledsCount):
		np[pixel] = (color_r, color_g, color_b)
		np.write()
		time.sleep(speed)

	time.sleep(wait)

	for pixel in range(ledsCount):
		np[pixel] = (0,0,0)
		np.write()
		time.sleep(speed)

	time.sleep(wait)
