from good_sorts import quicksort, heapsort, mergesort
from utilities import *


def run_experiment5():
    reps = 50
    length = 800
    log_len = length.bit_length() - 1
    # Go up to 3% the number of swaps from statistically random list
    max_swaps = (length * log_len // 2) * 3 // 100
    bmk = 36
    warmup_sorters([quicksort, mergesort, heapsort])
    print('Starting Quick Sort')
    quick_times = incrementing_swaps_tests(max_swaps, length, reps, bmk, quicksort)[1]
    print('Starting Merge Sort')
    merge_times = incrementing_swaps_tests(max_swaps, length, reps, bmk, mergesort)[1]
    print('Starting Heap Sort')
    swaps, heap_times = incrementing_swaps_tests(max_swaps, length, reps, bmk, heapsort)

    create_plot(swaps, [heap_times, quick_times, merge_times],
                ['Heap Sort', 'Quick Sort', 'Merge Sort'],
                'Average Execution Times of Quick, Merge and Heap Sorts on a Nearly Sorted List',
                f'{bmk + 1} increments of up to {max_swaps} swaps on a list size of' +
                f' {length} with {reps} repetitions per swap count',
                'Number of Swaps',
                'Average Execution Time (s)',
                2.2)


if __name__ == '__main__':
    run_experiment5()
