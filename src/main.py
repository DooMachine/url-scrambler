import argparse
import sys
import os
from modules.scrambler.scrambler import Scrambler 
from modules.dnssearch.dnssearch import DomainNameCheck 

parser = argparse.ArgumentParser(description='Generate and check domain names for scrambled urls of url')
parser.add_argument('--url','-u', metavar='instagram.com', type=str, help='url of website', required=True)
parser.add_argument('--output','-o', metavar='output.txt', type=str, help='output directory', required=True)
parser.add_argument('--checkdomain','-cd', metavar='false', type=bool, help='Check For Domain Names ?')
parser.add_argument('--levensteinlimit','-ll',type=int)



args = vars(parser.parse_args())
outputpath = os.path.join(os.getcwd(),args['output'])

levensteinlimit = 1
if 'levensteinlimit' in args:
    limit = args['levensteinlimit']

scr = Scrambler()
full_hostname = args['url'].split('.')

scrambleds = scr.Scramble_Word(full_hostname[0],levensteinlimit)
dn_checker = DomainNameCheck()
dn_obj = dn_checker.Check_Domains(scrambleds,full_hostname[1])
dn_checker.Dump_To(outputpath,dn_obj)
print (scrambleds)
def validHostName(hostname):
    return

