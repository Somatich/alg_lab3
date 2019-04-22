#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
from matplotlib import pyplot as plt
from tqdm import tqdm
from statistics import mean
import random
from search import linear_search, binary_search


def generate_sorted_data(sz):
    """
    Возвращает массив чисел без повторов, отсортированный в порядке
    возрастания
    """
    a = [1]
    for i in range(sz - 1):
        a.append(a[i] + random.randint(1, 10))
    return a


def measure_search_time(search_alg, sz, repeats):
    """
    Возвращает результат замеров скорости выполнения поиска в массиве длины sz.
    """
    data = generate_sorted_data(sz)
    results = []
    for i in range(repeats):
        v = random.choice(data)
        start = timer()
        search_alg(data, v)
        end = timer()
        results.append(end - start)
    return mean(results)


def main():
    sizesl = []
    avg_timel = []
    for sz in tqdm(range(10, 50000, 1000)):
        sizesl.append(sz)
        avg_timel.append(measure_search_time(linear_search, sz, 500))
    sizesb = []
    avg_timeb = []    
    for sz in tqdm(range(10, 50000, 1000)):
        sizesb.append(sz)
        avg_timeb.append(measure_search_time(binary_search, sz, 500))
    
    plt.plot(sizesl, avg_timel)
    plt.plot(sizesb, avg_timeb)
    plt.show()


if __name__ == "__main__":
    main()