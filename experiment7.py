from better_good_sorts import bottom_up_mergesort
from good_sorts import mergesort
from utilities import *


def run_experiment7() -> None:
    name = 'Merge Sort'
    sorters = [mergesort, bottom_up_mergesort]
    legend_labels = [name.lower().replace(' ', ''),
                     'bottom_up_' + name.lower().replace(' ', '')]
    compare_plot_sorters(sorters, legend_labels, name, 100000, 20, 20, 2.25)


if __name__ == '__main__':
    run_experiment7()
