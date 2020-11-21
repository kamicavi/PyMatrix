#!/usr/bin/env python3

import random
import time
import os
import sys

#sets defaults
colour = 92
interval = 0.052
spaceFreq = 0.8
charRange = [32,126]

#dictionary of colour names and escape codes
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

#help message
usage = '''Usage:
	-f '<filepath>' Read parameters from <filepath>.
	--file
	-p			  	Prompts for parameters.
	--prompt
	-c <int>		Colour. <int> should be a valid colour escape code.
	--colour
	--color
	-i <float>	  	The interval between lines.
	--int
	--interval
	-s <float>	  	The frequency at which spaces are printed.
	--spaces
	-r <int>,<int>	ASCII character range to print. [0] and [1] Should be between 32 and 255.
	--range
	--chars
	-h			  	Prints this help.
	--help			
	-d				Use default parameters. (colour: 92/green, interval: 0.052, space frequency: 0.8, characters: 32,126)
	--default\n '''

#Argument parser
def parseArgs(args):
	global colour, interval, spaceFreq, charRange
	i = 0

	#iterates over arguments and acts on them
	for arg in args:
		if arg == '-h' or arg == '--help':
			#help
			print(usage)
			quit()

		elif arg == '-f' or arg == '--file':
			#gets filename and reads
			file = open(args[i + 1],'r').read()
			del args[i + 1]
			#splits file into arguments and parses
			fileArgs = file.split(' ')
			parseArgs(fileArgs)

		elif arg == '-p' or arg == '--prompt':
			colourValid = False
			intervalValid = False
			spaceFreqValid = False
			charRangeValid = False

			#iterates over each question until user inputs a valid answer
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
					spaceFreq = float(input('What would you like the frequency of spaces to be? (suggested: 0.8) '))
					spaceFreqValid = True

				except ValueError:
					print('The frequency must be a decimal number')

			while not charRangeValid:
				try:
					charRange = input('What would characters would you like to include? (all basic ASCII characters would be 32,126) ').split(',')
					charRangeValid = True

				except ValueError:
					print('The character range should be two ASCII values, seperated by a comma.')

		elif arg == '-c' or arg == '--color' or arg == '--colour':
			#gets colour
			colour = args[i + 1]
			del args[i + 1]

			try: # trys for escape code
				int(colour)

			except ValueError:
				try: # trys for colour name
					colour = colours[colour]

				except KeyError:
					print('Not a valid colour.')
					quit()

			colourValid = True

		elif arg == '-i' or arg == '--int' or arg == '--interval':
			interval = float(args[i + 1]) # gets interval
			del args[i + 1]
			# error handling not implemented

		elif arg == '-s' or arg == '--spaces':
			spaceFreq = float(args[i + 1])
			del args[i + 1]
			# error handling not implemented

		elif arg == '-r' or arg == '--range' or arg == '--chars':
			charRange = args[i + 1].split(',')
			del args[i + 1]
			# error handling not implemented

		elif arg == '-d' or arg == '--default':
			pass

		i += 1


def main():
	global charRange
	if len(sys.argv) == 1:
		#if user inputs no arguments, print help and quit
		print(usage)
		quit()

	else:
		arguments = sys.argv
		parseArgs(arguments) # otherwise, parse arguments


	charRange = [int(i) for i in charRange]

	os.popen('clear') # clears terminal window

	while True:
		width = os.popen('stty size').read().split(' ')[1] #get terminal width
		line = ""

		for i in range(int(width)):
			temp = random.randint(*charRange)
			line = line + str(chr(temp)) #adds characters to line until it is as wide as terminal

		for i in range(int(int(width)/spaceFreq)): # replaces spaceFreq number of characters with spaces
			point = random.randint(0,int(width)-1)
			line = list(line)
			line[point] = ' '
			line = ''.join(line)

		print("\033[" + str(colour) + 'm' + str(line) + "\033[0m") # joins colour escape codes and prints
		time.sleep(interval) # waits

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: #exit handling
        print('\nThanks for using PyMatrix. Bye!')
        sys.exit(0)