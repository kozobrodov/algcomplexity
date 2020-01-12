#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('result.txt', 'r') as f:
    current_num = None
    for line_num, line in enumerate(f):
        number = int(line)
        if current_num:
            if number < current_num:
                print 'Test failed on line: ' + str(line_num)
                print str(number) + " < " + str(current_num)
                exit(1)
        current_num = number

    print 'Success! File is correctly sorted'