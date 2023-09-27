from bad_sorts import bubble_sort, insertion_sort, selection_sort
from utilities import *


def run_experiment3():
    bubble_times = []
    selection_times = []
    insertion_times = []
    reps = 25
    length = 500
    # Fast way to calculate integer log_2 of a number
    log_len = length.bit_length() - 1
    # Get 50% of the swaps needed from statistically random swaps value
    # since this is the interesting range
    max_swaps = (length * log_len // 2) * 50 // 100
    step_size = 40
    num_swaps = [x for x in range(0, max_swaps + 1, step_size)]
    warmup_sorters([bubble_sort, selection_sort, insertion_sort])

    for swaps in num_swaps:
        times_insertion = repeated_size_sorts(length, reps, insertion_sort, swaps)
        insertion_times.append(sum(times_insertion) / reps)
        times_bubble = repeated_size_sorts(length, reps, bubble_sort, swaps)
        bubble_times.append(sum(times_bubble) / reps)
        times_selection = repeated_size_sorts(length, reps, selection_sort, swaps)
        selection_times.append(sum(times_selection) / reps)

    create_plot(num_swaps, [insertion_times, bubble_times, selection_times],
                ['Insertion Sort', 'Bubble Sort', 'Selection Sort'],
                'Average Execution Times of Bubble, Insertion and Selection Sorts on a Nearly Sorted List',
                f'{max_swaps // step_size + 1} increments of up to {max_swaps} swaps on a list size of' +
                f' {length} with {reps} repetitions per swap count',
                'Number of Swaps',
                'Average Execution Time (s)',
                2)


if __name__ == '__main__':
    run_experiment3()
