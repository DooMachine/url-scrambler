import argparse
import sys
import os
from modules.scrambler.scrambler import Scrambler 
from modules.dnssearch.dnssearch import DomainNameCheck 

parser = argparse.ArgumentParser(description='Generate and check domain names for scrambled urls of url')
parser.add_argument('--url','-u', metavar='instagram.com', type=str, help='url of website', required=True)
parser.add_argument('--output','-o', metavar='output.txt', type=str, help='output directory', required=True)
parser.add_argument('--checkdomains','-cd', metavar='false', nargs='*', type=bool, help='Check For Domain Names ?')
parser.add_argument('--distance','-d',type=int)



args = vars(parser.parse_args())
outputpath = os.path.join(os.getcwd(),args['output'])

levensteinlimit = 3
if 'distance' in args:
    levensteinlimit = args['distance']
scr = Scrambler()
full_hostname = args['url'].split('.')

scrambleds = scr.Scramble_Word(full_hostname[0],levensteinlimit)
if (args['checkdomains'] is not None):
    dn_checker = DomainNameCheck()
    dn_obj = dn_checker.Check_Domains(scrambleds,full_hostname[1])
    dn_checker.Dump_To(outputpath,dn_obj)
else:
    with open(outputpath,'w+') as f:
        for dname in scrambleds:
            f.write(dname+'.'+full_hostname[1]+'\n')
        f.truncate()
        f.close()

print("Generated "+str(len(scrambleds))+"domain names")
print("Output dumped to "+ outputpath)