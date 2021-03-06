#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def sort(data):
    # Implement your sorting algorithm here
    # `data` contains array of integer numbers
    # This function must return sorted array
    return data


def sort_data():
    data = []
    with open('data.txt', 'r') as f:
        for line in f:
            if line:
                data.append(int(line))

    start_time = time.time()
    sorted_data = sort(data)
    execution_time = time.time() - start_time

    with open('result.txt', 'w') as f:
        for i in sorted_data:
            f.write(str(i))
            f.write('\n')

    print 'Sorting execution time: ' + str(int(execution_time)) + ' seconds'

if __name__ == '__main__':
    sort_data()