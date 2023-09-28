from good_sorts import quicksort, heapsort, mergesort
from utilities import *


def run_experiment5():
    quick_times = []
    merge_times = []
    heap_times = []
    reps = 50
    length = 500
    log_len = length.bit_length() - 1
    max_swaps = (length * log_len // 2) * 50 // 100
    step_size = 60
    num_swaps = [x for x in range(0, max_swaps + 1, step_size)]
    warmup_sorters([quicksort, mergesort, heapsort])

    for swaps in num_swaps:
        times_heap = repeated_size_sorts(length, reps, heapsort, swaps)
        heap_times.append(sum(times_heap) / reps)
        times_quick = repeated_size_sorts(length, reps, quicksort, swaps)
        quick_times.append(sum(times_quick) / reps)
        times_merge = repeated_size_sorts(length, reps, mergesort, swaps)
        merge_times.append(sum(times_merge) / reps)

    create_plot(num_swaps, [heap_times, quick_times, merge_times],
                ['Heap Sort', 'Quick Sort', 'Merge Sort'],
                'Average Execution Times of Quick, Merge and Heap Sorts on a Nearly Sorted List',
                f'{max_swaps // step_size + 1} increments of up to {max_swaps} swaps on a list size of' +
                f' {length} with {reps} repetitions per swap count',
                'Number of Swaps',
                'Average Execution Time (s)',
                2)


if __name__ == '__main__':
    run_experiment5()
