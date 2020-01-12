#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange


with open('data.txt', 'w') as f:
    for i in range(0, 10000000):
        random_number = randrange(10000)
        f.write(str(random_number))
        f.write('\n')