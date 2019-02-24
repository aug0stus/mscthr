"""
Copyright (C) 2018 August Feng <au.fengster@gmail.com>
"""

import random

#some voodoo magic shit happening here.
def random_items(msc_elements):
    msc_elements = list(msc_elements)
    #length = sum(1 for _ in msc_elements) #cool way of getting max items in generators.
    return random.choice(msc_elements)
