import random
import time
import os

colour = raw_input('What colour would you like? (light grey, grey, red, green, blue, light blue, pink, white) ').lower()
interval = float(raw_input('What would you like the interval between lines to be? (seconds) '))

colours = {
'light grey'	:'89',
'grey'		    :'90',
'red' 		    :'91',
'green'		    :'92',
'yellow'	    :'93',
'blue'		    :'94',
'pink'		    :'95',
'light blue'	:'96',
'white'		    :'97'}
while True:
	width = os.popen('stty size').read().split(' ')[1]
	line = ""
	for i in range(int(width)):
		temp = random.randint(32,126)
		line = line + str(chr(temp))
	for i in range(int(int(width)/2)):
		point = random.randint(0,int(width)-1)
		line = list(line)
		line[point] = ' '
		line = ''.join(line)
	print("\033[" + str(colours[colour]) + 'm' + str(line) + "\033[0m")
	time.sleep(interval)
