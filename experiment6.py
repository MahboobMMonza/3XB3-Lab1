from better_good_sorts import dual_quicksort
from good_sorts import quicksort
from utilities import *


def run_experiment6() -> None:
    name = 'Quick Sort'
    sorters = [quicksort, dual_quicksort]
    legend_labels = [name.lower().replace(' ', ''),
                     'dual_' + name.lower().replace(' ', '')]
    compare_plot_sorters(sorters, legend_labels, name, 100000, 20, 20, 2.25)


if __name__ == '__main__':
    run_experiment6()
