#####
#
# File name : ex15.py
#
# Notes : Reading Files
#
#
#
# Creation Date : 28-04-2012
#
# Last Modified :
#
# Created by : Simon Gibson
#
#####

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file: %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">>>")

txt_again = open(file_again)

print txt_again.read()
