# Tutorial 
# https://www.pandorabots.com/botmaster/en/tutorial?ch=1
# http://www.tutorialspoint.com/aiml/aiml_quick_guide.htm

import aiml
import os
import sys
from subprocess import call
import itertools

kernel = aiml.Kernel()

# call(['rm', '-r', 'train.brn'])
# if os.path.isfile('train.brn') :
# 	kernel.bootstrap(brainFile = 'train.brn')
# else :
# 	kernel.bootstrap(learnFiles = 'train.xml', commands = 'Hi')
# 	kernel.saveBrain('train.brn')
kernel.learn('train.xml')

# f = open('in.txt', 'r')
# lines = f.read().split('\n')

# for question in lines:
question = '# What # ontological engineering #'
print (question, '  =>  ', kernel.respond(question))
