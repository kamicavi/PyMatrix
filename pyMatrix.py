import random
import time
import os
import sys

colour = 92
interval = 0.052
spaceFreq = 0.8
charRange = [32,126]

colours = {
	'light grey'	:'89',
	'grey'			:'90',
	'red' 			:'91',
	'green'			:'92',
	'yellow'		:'93',
	'blue'			:'94',
	'pink'			:'95',
	'light blue'	:'96',
	'white'			:'97'
}

usage = '''Usage:
	-f '<filepath>' Read parameters from <filepath>.
	-p			  	Prompts for parameters.
	-c <int>		Colour. <int> should be a valid colour escape code.
	-i <float>	  	The interval between lines.
	-s <float>	  	The frequency at which spaces are printed.
	-r <int>,<int>	ASCII character range to print. [0] and [1] Should be between 32 and 255.
	-h			  	Prints this help.
	-d				Use default parameters. (colour: 92/green, interval: 0.052, space frequency: 0.8, characters: 32,126)/n '''

def parseArgs(args):
	i = 0

	for arg in args:
		if arg == '-h':
			print(usage)
			quit()

		elif arg == '-f':
			file = open(args[i + 1],'r').read()
			del args[i + 1]
			fileArgs = file.split(' ')
			parseArgs(fileArgs)

		elif arg == '-p':
			colourValid = False
			intervalValid = False
			spaceFreqValid = False
			charRangeValid = False

			while not colourValid:
				try:
					colour = input('What colour would you like? (light grey, grey, red, green, blue, light blue, pink, white, or a colour escape code.) ').lower()

					try:
						int(colour)

					except ValueError:
						colour = colours[colour]

					colourValid = True

				except KeyError:
					print('Not a valid colour.')

			while not intervalValid:
				try:
					interval = float(input('What would you like the interval between lines to be? (seconds) (suggested: 0.052) '))
					intervalValid = True

				except ValueError:
					print('The interval must be a decimal number.')

			while not spaceFreqValid:
				try:
					spaceFreq = float(input('What would you like the of spaces to be? (suggested: 0.8) '))
					spaceFreqValid = True

				except ValueError:
					print('The frequency must be a decimal number')

			while not charRangeValid:
				try:
					charRange = input('What would characters would you like to include? (all basic ASCII characters are 32,126) ').split(',')
					charRangeValid = True

				except ValueError:
					print('The character range should be two ASCII values, seperated by a comma.')

		elif arg == '-c':
			colour = args[i + 1]
			del args[i + 1]

			try:
				int(colour)

			except ValueError:
				try:
					colour = colours[colour]

				except KeyError:
					print('Not valid colour.')

			colourValid = True

		elif arg == '-i':
			interval = float(args[i + 1])
			del args[i + 1]

		elif arg == '-s':
			spaceFreq = float(args[i + 1])
			del args[i + 1]

		elif arg == '-r':
			charRange = args[i + 1].split(',')
			del args[i + 1]

		i += 1



if len(sys.argv) == 1:
	print(usage)
	quit()

else:
	arguments = sys.argv
	parseArgs(arguments)


charRange = [int(i) for i in charRange]

os.popen('clear')

while True:
	width = os.popen('stty size').read().split(' ')[1]
	line = ""

	for i in range(int(width)):
		temp = random.randint(*charRange)
		line = line + str(chr(temp))

	for i in range(int(int(width)/spaceFreq)):
		point = random.randint(0,int(width)-1)
		line = list(line)
		line[point] = ' '
		line = ''.join(line)

	print("\033[" + str(colour) + 'm' + str(line) + "\033[0m")
	time.sleep(interval)