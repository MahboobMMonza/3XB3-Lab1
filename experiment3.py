import math

from utilities import *
from bad_sorts import insertion_sort, bubble_sort, selection_sort


def run_experiment3(length, max_value, num_swaps, repetitions) -> None:
    # Run a warmup routine on the sorting algorithms to reduce cache miss errors, etc
    print('Warming Up')
    warmup_sorters([insertion_sort, bubble_sort, selection_sort])

    swap_values = []
    insertion_times = []
    bubble_times = []
    selection_times = []

    # Run tests
    for swaps in num_swaps:
        swap_values.append(swaps)
        insertion_avg = 0
        bubble_avg = 0
        selection_avg = 0

        print(f'Starting tests for {swaps} swaps')
        for _ in range(repetitions):
            near_sorted_list = create_near_sorted_list(length, max_value, swaps)

            # Plot results in graph
            _,time_insertion = time_measure(insertion_sort, near_sorted_list)
            insertion_avg += time_insertion

            _,time_bubble = time_measure(bubble_sort, near_sorted_list)
            bubble_avg += time_bubble

            _, time_selection = time_measure(selection_sort, near_sorted_list)
            selection_avg = time_selection

        insertion_avg /= repetitions
        bubble_avg /= repetitions
        selection_avg /= repetitions

        insertion_times.append(insertion_avg)
        bubble_times.append(bubble_avg)
        selection_times.append(selection_avg)

    x_vals = swap_values
    y_vals = [insertion_times, bubble_times, selection_times]
    legend_labels = ["Insertion Sort", "Bubble Sort", "Selection Sort"]
    print('Creating plots')
    create_plot(x_vals,
                y_vals,
                legend_labels,
                "Average Run Times on Near Sorted Lists",
                f"List Length: {length}, Max Value: {max_value}, Repetitions: {repetitions}",
                "Number of Swaps",
                "Average Time (s)")
    print('Graph created')


if __name__ == '__main__':
    length = 1000
    max_value = 4000
    num_swaps = [0,100,500,1000,2000]
    repetitions = 15
    run_experiment3(length,max_value,num_swaps,repetitions)
