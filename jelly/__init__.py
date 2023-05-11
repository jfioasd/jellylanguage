from sys import stderr

from .interpreter import *

def main(code, args, end):
	for index in range(min(7, len(args))):
		atoms['³⁴⁵⁶⁷⁸⁹'[index]].call = lambda literal = args[index]: literal

	try:
		return stringify(jelly_eval(code, args[:2]))
	except KeyboardInterrupt:
		if stderr.isatty():
			sys.stderr.write('\n')
		return 130
