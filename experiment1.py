from bad_sorts import insertion_sort, bubble_sort, selection_sort
from utilities import *


def run_experiment1():
    # Set parameters for the experiment
    print('Warming up')
    warmup_sorters([insertion_sort, bubble_sort, selection_sort])
    print('Starting tests')
    max_n, reps, bmk = 5000, 100, 10
    insertion_sizes, times_insertion = incrementing_list_size_tests(max_n, reps, bmk, insertion_sort)
    bubble_sizes, times_bubble = incrementing_list_size_tests(max_n, reps, bmk, bubble_sort)
    selection_sizes, times_selection = incrementing_list_size_tests(max_n, reps, bmk, selection_sort)
    # Plot results in graph
    x_vals = [insertion_sizes, bubble_sizes, selection_sizes]
    y_vals = [times_insertion, times_bubble, times_selection]
    legend_labels = ["Insertion Sort", "Bubble Sort", "Selection Sort"]
    print('Creating plots')
    create_plot(x_vals, y_vals, "List Sizes", "Average Time (s)", legend_labels)


if __name__ == '__main__':
    run_experiment1()
