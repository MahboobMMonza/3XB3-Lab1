"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import timeit

import matplotlib.pyplot as plt


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i - 1]:
            swap(L, i - 1, i)
            i -= 1
        else:
            return


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                swap(L, j, j + 1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n + 1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


def warmup():
    exp1_scaling_times(100, 100, 10, insertion_sort)
    exp1_scaling_times(100, 100, 10, bubble_sort)
    exp1_scaling_times(100, 100, 10, selection_sort)


def exp1_scaling_times(max_n: int, repetitions: int, benchmarks: int, sorter: callable) -> tuple[
    list[int], list[float]]:
    sizes = [(i + 1) * max_n // benchmarks for i in range(benchmarks)]
    times = [0.0] * benchmarks
    for i, size in enumerate(sizes):
        current_times = repeated_size_sorts(size, repetitions, sorter)
        times[i] = sum(current_times) / repetitions

    return sizes, times


def repeated_size_sorts(list_size: int, repetition: int, sorter: callable) -> list[float]:
    time = [0.0] * repetition

    for i in range(repetition):
        my_list = create_random_list(list_size, list_size)
        start = timeit.default_timer()
        sorter(my_list)
        end = timeit.default_timer()
        time[i] = end - start
    return time


if __name__ == '__main__':
    print("Warming up...")
    warmup()
    print("Running Tests")
    max_n, reps, bmk = 100, 20, 10
    insert_sizes, times_insertion = exp1_scaling_times(max_n, reps, bmk, insertion_sort)
    bubble_sizes, times_bubble = exp1_scaling_times(max_n, reps, bmk, bubble_sort)
    selection_sizes, times_selection = exp1_scaling_times(max_n, reps, bmk, selection_sort)
    plt.plot(insert_sizes, times_insertion, linewidth=2, label=r"Insertion Sort")
    plt.plot(bubble_sizes, times_bubble, linewidth=2, label=r"bubble Sort")
    plt.plot(selection_sizes, times_selection, linewidth=2, label=r"Selection Sort")
    plt.legend(fontsize=14)
    plt.show()
