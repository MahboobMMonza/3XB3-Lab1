import math

from bad_sorts import bubble_sort,insertion_sort,selection_sort
from utilities import *

def run_experiment5():
    swap_values = []
    bubble_times = []
    selection_times = []
    insertion_times = []

    list_lengths = [100, 500, 1000, 5000, 10000]
    num_runs = 10
    warmup_sorters([bubble_sort, selection_sort, insertion_sort])

    for length in list_lengths:
        swaps = int(length * math.log(length) / 2)

        near_sorted_list =  create_near_sorted_list(length, length, swaps)

        bubble_time = sum(repeated_size_sorts(length, num_runs, bubble_sort)) / num_runs
        selection_time = sum(repeated_size_sorts(length, num_runs, selection_sort)) / num_runs
        insertion_time = sum(repeated_size_sorts(length, num_runs, insertion_sort)) / num_runs

        swap_values.append(swaps)
        bubble_times.append(bubble_time)
        selection_times.append(selection_time)
        insertion_times.append(insertion_time)

    create_plot(swap_values, [bubble_times, selection_times, insertion_times],
                ['Quick Sort', 'Merge Sort', 'Heap Sort'],
                'Execution Time vs. Number of Swaps',
                f'{num_runs} runs per list length',
                'Number of Swaps', 'Average Execution Time (s)')

if __name__ == '__main__':
    run_experiment5()
