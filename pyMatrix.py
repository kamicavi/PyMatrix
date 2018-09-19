import random
import time
import os

usage = '''Usage:
    -f '<filepath>'   Read parameters from <filepath> (not currently implemented).
    -p              Prompts for parameters.
    -c <int>        Colour. <int> should be a valid colour escape code.
    -i <float>      The interval between lines.
    -s <float>      The frequency at which spaces are printed.
    -r <tuple>      ASCII character range to print. <tuple>[0] and [1] Should be between 32 and 255.
    -h              Prints this help.\n'''

if sys.argv.len() == 1:
    print(usage)
    
else:
    arguments = sys.argv
    i = 1
    
    for i in arguments:
        if arguments[i] == '-h':
            print(usage)
            
        if arguments[i] == '-p':
            while not colourValid:
                try:
                    colour = colours[raw_input('What colour would you like? (light grey, grey, red, green, blue, light blue, pink, white) ').lower()]
                    colourValid = True
                    
                except KeyError:
                    print('Not a valid colour.')
                    
            while not intervalValid:
                try:
                    interval = float(raw_input('What would you like the interval between lines to be? (seconds) '))
                    intervalValid = True
                    
                except TypeError:
                    print('The interval must be a decimal number.')
                
            while not spaceFreqValid:
                try:
                    spaceFreq =
colour = 92
interval = 0.052
spaceFreq = 0.8
charRange = (32,126)

colours = {
    'light grey'	:'89',
    'grey'		    :'90',
    'red' 		    :'91',
    'green'		    :'92',
    'yellow'	    :'93',
    'blue'		    :'94',
    'pink'		    :'95',
    'light blue'	:'96',
    'white'		    :'97'
}

os.popen('clear')

while True:
	width = os.popen('stty size').read().split(' ')[1]
	line = ""
	for i in range(int(width)):
		temp = random.randint(charRange)
		line = line + str(chr(temp))
	for i in range(int(int(width)/spaceFreq)):
		point = random.randint(0,int(width)-1)
		line = list(line)
		line[point] = ' '
		line = ''.join(line)
	print("\033[" + str(colour) + 'm' + str(line) + "\033[0m")
	time.sleep(interval)