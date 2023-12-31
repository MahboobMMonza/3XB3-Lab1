from bad_sorts import insertion_sort, bubble_sort, selection_sort
from utilities import *


def run_experiment1() -> None:
    # Run a warmup routine on the sorting algorithms to reduce cache miss errors, etc
    print('Warming up')
    warmup_sorters([insertion_sort, bubble_sort, selection_sort])
    # Run tests
    print('Starting tests')
    max_n, reps, bmk = 4000, 15, 10
    print('Starting Insertion Sort')
    insertion_sizes, times_insertion = incrementing_list_size_tests(max_n, reps, bmk, insertion_sort)
    print('Starting Bubble Sort')
    bubble_sizes, times_bubble = incrementing_list_size_tests(max_n, reps, bmk, bubble_sort)
    print('Starting Selection Sort')
    selection_sizes, times_selection = incrementing_list_size_tests(max_n, reps, bmk, selection_sort)
    # Plot results in graph
    x_vals = insertion_sizes
    y_vals = [times_insertion, times_bubble, times_selection]
    legend_labels = ["Insertion Sort", "Bubble Sort", "Selection Sort"]
    print('Creating plots')
    create_plot(x_vals,
                y_vals,
                legend_labels,
                "Average Run Times of Selection, Insertion and Bubble Sorts",
                f"{bmk} increments up to sizes of {max_n} with {reps} repetitions per size",
                "List Sizes",
                "Average Time (s)")


if __name__ == '__main__':
    run_experiment1()
