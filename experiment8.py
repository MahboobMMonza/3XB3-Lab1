from good_sorts import quicksort, mergesort
from bad_sorts import insertion_sort
from utilities import *



def run_experiment8() -> None:
    # Run a warmup routine on the sorting algorithms to reduce cache miss errors, etc
    print('Warming up')
    warmup_sorters([quicksort, mergesort, insertion_sort])
    # Run tests
    print('Starting tests')
    max_n, reps, bmk = 100, 100, 25
    print('Starting Quick Sort')
    quick_sizes, times_quick = incrementing_list_size_tests(max_n, reps, bmk, quicksort)
    print('Starting Merge Sort')
    merge_sizes, times_merge = incrementing_list_size_tests(max_n, reps, bmk, mergesort)
    print('Starting Insertion Sort')
    insertion_sizes, times_insertion = incrementing_list_size_tests(max_n, reps, bmk, insertion_sort)
    # Plot results in graph
    x_vals = quick_sizes
    y_vals = [times_quick, times_merge, times_insertion]
    legend_labels = ["Quick Sort", "Merge Sort", "Insertion Sort"]
    print('Creating plots')
    create_plot(x_vals,
                y_vals,
                legend_labels,
                "Average Run Times of Quick, Merge and Insertion Sorts on Small List Sizes",
                f"{bmk} increments up to sizes of {max_n} with {reps} repetitions per size",
                "List Sizes",
                "Average Time (s)",
                2)

if __name__ == '__main__':
    run_experiment8()
