#!/usr/bin/python 

import string
import random
lst = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(16)])
str = "".join(lst)

