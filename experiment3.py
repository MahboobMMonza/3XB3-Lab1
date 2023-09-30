from bad_sorts import bubble_sort, insertion_sort, selection_sort
from utilities import *


def run_experiment3():
    reps = 50
    length = 500
    # Fast way to calculate integer log_2 of a number
    log_len = length.bit_length() - 1
    # Get 50% of the swaps needed from statistically random swaps value
    # since this is the interesting range
    max_swaps = (length * log_len // 2) * 50 // 100
    bmk = 25
    warmup_sorters([bubble_sort, selection_sort, insertion_sort])

    insertion_times = incrementing_swaps_tests(max_swaps, length, reps, bmk, insertion_sort)[1]
    bubble_times = incrementing_swaps_tests(max_swaps, length, reps, bmk, bubble_sort)[1]
    swaps, selection_times = incrementing_swaps_tests(max_swaps, length, reps, bmk, selection_sort)

    create_plot(swaps, [insertion_times, bubble_times, selection_times],
                ['Insertion Sort', 'Bubble Sort', 'Selection Sort'],
                'Average Execution Times of Bubble, Insertion and Selection Sorts on a Nearly Sorted List',
                f'{bmk + 1} increments of up to {max_swaps} swaps on a list size of' +
                f' {length} with {reps} repetitions per swap count',
                'Number of Swaps',
                'Average Execution Time (s)',
                2)


if __name__ == '__main__':
    run_experiment3()
