import random
import timeit

import matplotlib.pyplot as plt


def warmup_sorters(sorters: list[callable]):
    for sorter in sorters:
        incrementing_list_size_tests(1000, 20, 10, sorter)


# Function runs repeated_size_sorts to execute sorting algorithms on list sizes of upto size max_n
def incrementing_list_size_tests(max_n: int,
                                 repetitions: int,
                                 benchmarks: int,
                                 sorter: callable) -> tuple[list[int], list[float]]:
    sizes = [(i + 1) * max_n // benchmarks for i in range(benchmarks)]
    # list to store execution times
    times = [0.0] * benchmarks
    for i, size in enumerate(sizes):
        # measure execution times for a given input size and sorting algorithm
        current_times = repeated_size_sorts(size, repetitions, sorter)

        # Calculate the average execution time for this input size
        times[i] = sum(current_times) / repetitions
    return sizes, times


# Function to repeatedly measure the execution time of a sorting algorithm for a specific input size
def repeated_size_sorts(list_size: int, repetitions: int, sorter: callable) -> list[float]:
    time = [0.0] * repetitions

    for i in range(repetitions):
        my_list = create_random_list(list_size, list_size)
        start = timeit.default_timer()
        sorter(my_list)
        end = timeit.default_timer()
        time[i] = end - start
    return time


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def create_plot(x_vals: list,
                y_vals: list[list],
                legend_labels: list[str],
                title: str,
                description: str,
                x_label: str,
                y_label: str,
                scale: int = 1,
                ) -> None:
    height, width = plt.figure().get_figheight(), plt.figure().get_figwidth()
    plt.figure(figsize=(scale * width, scale * height))
    for yv, legend in zip(y_vals, legend_labels):
        plt.plot(x_vals, yv, linewidth=2, label=legend, marker='o')

    plt.xlabel(x_label)
    plt.xticks(x_vals)
    plt.ylabel(y_label)
    plt.suptitle(title, fontsize=14)
    plt.title(description, fontsize=10)
    plt.legend(fontsize=10)
    plt.show()


def confirm_sorter_correctness(sorter: callable) -> bool:
    max_n, benchmarks, reps = 5000, 5, 5
    for r in range(reps):
        for length in range(max_n // benchmarks, max_n, max_n // benchmarks):
            lst = create_random_list(length, 10000000)
            ans = sorted(lst)
            sorter(lst)
            if lst != ans:
                return False

    return True


def compare_plot_sorters(sorters: list[callable, 2],
                         legend_labels: list[str, 2],
                         sort_name: str,
                         max_n: int = 4000,
                         repetitions: int = 15,
                         benchmarks: int = 10) -> None:
    title = f'Average Run Times of {sort_name} Implementations'
    print(f'Running {title} Tests')
    print('Warming up')
    warmup_sorters(sorters)
    y_vals = []
    x_vals = None
    for sorter, label in zip(sorters, legend_labels):
        print(f'Starting {label}')
        x_vals, time = incrementing_list_size_tests(max_n, repetitions, benchmarks, sorter)
        y_vals.append(time)

    print('Creating plots')
    create_plot(x_vals,
                y_vals,
                legend_labels,
                title,
                f"{benchmarks} increments up to sizes of {max_n} with {repetitions} repetitions per size",
                "List Sizes",
                "Average Time (s)")


if __name__ == '__main__':
    pass
