from bad_sorts import insertion_sort, bubble_sort, selection_sort
from better_bad_sorts import *
from utilities import *


def run_experiment2() -> None:
    sorter_names = ['Insertion Sort', 'Bubble Sort', 'Selection Sort']
    old_sorters = [insertion_sort, bubble_sort, selection_sort]
    new_sorters = [insertion_sort2, bubble_sort2, selection_sort2]
    for name, old_sort, new_sort in zip(sorter_names, old_sorters, new_sorters):
        sorters = [old_sort, new_sort]
        compare_plot_sorters(sorters, name)


def compare_plot_sorters(sorters: list[callable, 2], sort_name: str) -> None:
    title = f'Average Run Times of {sort_name} Implementations'
    print(f'Running {title} Tests')
    print('Warming up')
    warmup_sorters(sorters)
    max_n, reps, bmk = 4000, 15, 10
    legend_labels = [sort_name.lower().replace(' ', '_'),
                     sort_name.lower().replace(' ', '_') + '2']
    y_vals = []
    x_vals = None
    for sorter, label in zip(sorters, legend_labels):
        print(f'Starting {label}')
        x_vals, time = incrementing_list_size_tests(max_n, reps, bmk, sorter)
        y_vals.append(time)

    print('Creating plots')
    create_plot(x_vals,
                y_vals,
                legend_labels,
                title,
                f"{bmk} increments up to sizes of {max_n} with {reps} repetitions per size",
                "List Sizes",
                "Average Time (s)")


if __name__ == '__main__':
    # print(confirm_sorter_correctness(insertion_sort2))
    # print(confirm_sorter_correctness(bubble_sort2))
    # print(confirm_sorter_correctness(selection_sort2))
    run_experiment2()
