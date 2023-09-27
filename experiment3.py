import math

from bad_sorts import bubble_sort, insertion_sort, selection_sort
from utilities import *


def run_experiment3():
    swap_values = []
    bubble_times = []
    selection_times = []
    insertion_times = []

    reps = 15
    length = [100, 500, 1000, 2000]
    warmup_sorters([bubble_sort, selection_sort, insertion_sort])

    for size in length:
        swaps = size*math.log(size)/2
        swap_values.append(swaps)
        times_insertion = repeated_size_sorts(size, reps, insertion_sort,True, create_near_sorted_list)
        insertion_times.append(times_insertion)
        times_bubble = repeated_size_sorts(size, reps, bubble_sort,True, create_near_sorted_list)
        bubble_times.append(times_bubble)
        times_selection = repeated_size_sorts(size, reps, selection_sort,True, create_near_sorted_list)
        selection_times.append(times_selection)

    create_plot(swap_values, [insertion_times, bubble_times, selection_times],
                ['Quick Sort', 'Merge Sort', 'Heap Sort'],
                'Execution Time vs. Number of Swaps',
                f'{reps} runs per list length',
                'Number of Swaps', 'Average Execution Time (s)')


if __name__ == '__main__':
    run_experiment3()
