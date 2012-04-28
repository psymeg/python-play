#####
#
# File name : ex14.py
#
# Notes : Prompting and Passing
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

script, user_name = argv
prompt ='>'

print "Hi %s, Im the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like Australia, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking Australia.
You live in %r. Hope that is a nice place.
And you have a %r computer. Nice.
""" %(likes, lives, computer)
