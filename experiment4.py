from good_sorts import quicksort, mergesort, heapsort
from utilities import *


def run_experiment4() -> None:
    # Run a warmup routine on the sorting algorithms to reduce cache miss errors, etc
    print('Warming up')
    warmup_sorters([quicksort, mergesort, heapsort])
    # Run tests
    print('Starting tests')
    max_n, reps, bmk = 40000, 25, 20
    print('Starting Quick Sort')
    quick_sizes, times_quick = incrementing_list_size_tests(max_n, reps, bmk, quicksort)
    print('Starting Merge Sort')
    merge_sizes, times_merge = incrementing_list_size_tests(max_n, reps, bmk, mergesort)
    print('Starting Heap Sort')
    heap_sizes, times_heap = incrementing_list_size_tests(max_n, reps, bmk, heapsort)
    # Plot results in graph
    x_vals = quick_sizes
    y_vals = [times_quick, times_merge, times_heap]
    legend_labels = ["Quick Sort", "Merge Sort", "Heap Sort"]
    print('Creating plots')
    create_plot(x_vals,
                y_vals,
                legend_labels,
                "Average Run Times of Quick, Merge and Heap Sorts",
                f"{bmk} increments up to sizes of {max_n} with {reps} repetitions per size",
                "List Sizes",
                "Average Time (s)",
                2)


if __name__ == '__main__':
    run_experiment4()
