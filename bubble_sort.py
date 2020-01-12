#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def sort(data):
    # Bubble sort implementation
    N = len(data)
    for i in range(0, N):
        for j in range(i, N):
            if data[i] > data[j]:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
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