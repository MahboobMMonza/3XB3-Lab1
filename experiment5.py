import math

from good_sorts import quicksort, mergesort,heapsort
from utilities import *

def run_experiment5():
    swap_values = []
    quick_times = []
    merge_times = []
    heap_times = []

    list_lengths = [100, 500, 1000, 5000, 10000]
    num_runs = 10;
    warmup_sorters([quicksort, mergesort, heapsort])

    for length in list_lengths:
        swaps = int(length * math.log(length) /2)

        near_sorted_list =  create_near_sorted_list(length,length,swaps)

        quick_time = sum(repeated_size_sorts(length,num_runs,quicksort)) / num_runs
        merge_time = sum(repeated_size_sorts(length, num_runs, mergesort)) / num_runs
        heap_time = sum(repeated_size_sorts(length, num_runs, heapsort)) / num_runs

        swap_values.append(swaps)
        quick_times.append(quick_time)
        merge_times.append(merge_time)
        heap_times.append(heap_time)

    create_plot(swap_values, [quick_times, merge_times, heap_times],
                    ['Quick Sort', 'Merge Sort', 'Heap Sort'],
                    'Execution Time vs. Number of Swaps',
                    f'{num_runs} runs per list length',
                    'Number of Swaps', 'Average Execution Time (s)')
if __name__ == '__main__':
    run_experiment5()