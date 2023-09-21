from good_sorts import mergesort
from better_good_sorts import bottom_up_merge_sort
from utilities import *


def run_experiment7() -> None:
    sorter_names = ['Merge Sort']
    old_sorters = [mergesort]
    new_sorters = [bottom_up_merge_sort]
    for name, old_sort, new_sort in zip(sorter_names, old_sorters, new_sorters):
        sorters = [old_sort, new_sort]
        legend_labels = [name.lower().replace(' ', ''), 'bottom_up_' + name.lower().replace(' ', '')]
        compare_plot_sorters(sorters, legend_labels, name, 100000, 20, 20, 2)


if __name__ == '__main__':
    # print(confirm_sorter_correctness(insertion_sort2))
    # print(confirm_sorter_correctness(bubble_sort2))
    # print(confirm_sorter_correctness(selection_sort2))
    run_experiment7()
