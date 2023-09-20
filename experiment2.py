from bad_sorts import insertion_sort, bubble_sort, selection_sort
from utilities import *


# Selection sort arranging both min and max elements in one go
def selection_sort2(lst: list) -> None:
    left, right = 0, len(lst)
    while left < right:
        # Find the max and min between the left and right bounds
        min_idx, max_idx = left, left
        min_val, max_val = lst[min_idx], lst[max_idx]
        for i in range(left + 1, right):
            if lst[i] < lst[min_idx]:
                min_idx = i
                min_val = lst[i]
            elif lst[i] > lst[max_idx]:
                max_idx = i
                max_val = lst[i]

        # Swap the left value with the minimum in the range
        swap(lst, left, min_idx)
        # Check to see if the swapped (old) left bound value was the maximum, and if it was swap with max value
        # otherwise swap max value with right bound value
        if lst[min_idx] == max_val:
            swap(lst, right - 1, min_idx)
        else:
            swap(lst, right - 1, max_idx)

        left += 1
        right -= 1


# Bubble sort minimizing number of swap operations
def bubble_sort2(lst: list) -> None:
    for i in range(len(lst)):
        temp = lst[0]
        # Every time a bubbling occurs, the (i + 1)th largest element will become temp by the end of the loop
        for j in range(len(lst) - 1 - i):
            if temp < lst[j + 1]:
                # Shift elements left until the next element is larger than the current temp, at which point overwrite
                # the current index as temp and set temp to the next element
                lst[j] = temp
                temp = lst[j + 1]
            else:
                lst[j] = lst[j + 1]

        # temp will always be the (i + 1)th largest element found
        lst[- 1 - i] = temp


# Insertion sort minimizing number of swap operations
def insertion_sort2(lst: list) -> None:
    for i in range(1, len(lst)):
        # Copy the next unsorted value to be inserted to the left
        temp, j = lst[i], i
        # Shift all elements to the right until a value <= temp is found
        while j > 0 and lst[j - 1] > temp:
            lst[j] = lst[j - 1]
            j -= 1
        else:
            # Place temp sorted into the left side of the array
            # Either lst[j - 1] <= temp, in which case overwrite the copied value
            # Or the value is at the beginning of the list
            lst[j] = temp


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
