from bad_sorts import insertion_sort, bubble_sort, selection_sort
from better_bad_sorts import *
from utilities import *


def run_experiment2() -> None:
    sorter_names = ['Insertion Sort', 'Bubble Sort', 'Selection Sort']
    old_sorters = [insertion_sort, bubble_sort, selection_sort]
    new_sorters = [insertion_sort2, bubble_sort2, selection_sort2]
    for name, old_sort, new_sort in zip(sorter_names, old_sorters, new_sorters):
        sorters = [old_sort, new_sort]
        legend_labels = [name.lower().replace(' ', '_'), name.lower().replace(' ', '_') + '2']
        compare_plot_sorters(sorters, legend_labels, name)


if __name__ == '__main__':
    # print(confirm_sorter_correctness(insertion_sort2))
    # print(confirm_sorter_correctness(bubble_sort2))
    # print(confirm_sorter_correctness(selection_sort2))
    run_experiment2()
