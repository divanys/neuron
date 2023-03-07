import numpy as np
import re
from random import randint
import language as lg

"""
Микрообщение(?)
"""


input_n = 1
neuron = 10
out_n = 5

input_mess = input("Message: ")
p = re.compile(r"\w+")
string = p.findall(input_mess) 
# print(string)

keys = list(lg.message.keys())

for i in range(len(string)):
    if keys[0] == string[i]:
        ghbdtn = lg.message.get(keys[i])
        print(ghbdtn[randint(0, len(ghbdtn))])

# print(keys)