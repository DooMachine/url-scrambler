import argparse
import sys
import os
from modules.scrambler.scrambler import Scrambler 

parser = argparse.ArgumentParser(description='Generate and check dns for scrambled urls of url')
parser.add_argument('--url','-u', metavar='instagram.com', type=str, help='url of website', required=True)
parser.add_argument('--output','-o', metavar='output.txt', type=str, help='output directory', required=True)
parser.add_argument('--checkdomain','-o', metavar='false', type=bool, help='Check For Domain Names ?')
parser.add_argument('--limit','-l',type=int)
scr = Scrambler()


args = vars(parser.parse_args())
outputpath = os.path.join(os.getcwd(),args['output'])
scrambleds = scr.Scramble_Word(args['url'])
print (scrambleds)

