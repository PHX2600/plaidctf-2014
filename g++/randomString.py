#!/usr/bin/python 

import string
import random
lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(30)]
str = "".join(lst)

