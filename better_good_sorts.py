def bottom_up_mergesort(lst: list) -> None:
    size = len(lst)
    temp = [0] * size
    step = 2
    while (step // 2) < len(lst):
        for i in range(0, size, step):
            left, right = i, min(i + step, size)
            mid = left + (step // 2)
            if mid >= right:
                continue
            lp, rp, j = left, mid, left
            # Copy to temp
            temp[left:right] = lst[left:right]
            # do merge
            while lp < mid and rp < right:
                if temp[lp] < temp[rp]:
                    lst[j] = temp[lp]
                    lp += 1
                else:
                    lst[j] = temp[rp]
                    rp += 1
                j += 1

            if lp < mid:
                lst[j:right] = temp[lp:mid]
            else:
                lst[j:right] = temp[rp:right]

        step *= 2


def dual_quicksort(lst: list) -> None:
    # Add left and right bounds for partition to the stack, right bound is excluded
    stack = [(0, len(lst))]
    # Instead of making recursive partition calls, use a stack to hold the arguments and a while loop to
    # partition along the arguments
    while stack:
        # Get the partition bounds (right bound is exclusive)
        left, right = stack.pop()
        # Choose pivot locations as left and right endpoints, and swap them if right point is smaller than left
        if lst[left] > lst[right - 1]:
            lst[left], lst[right - 1] = lst[right - 1], lst[left]
        left_pivot_value, right_pivot_value = lst[left], lst[right - 1]
        # Set the left and right bounds for the partition
        left_bound, right_bound = left + 1, right - 1
        # Create "buckets" for values based on their relation to the pivots
        less, between, greater = [], [], []
        # Do partition on the sublist from after the left pivot to before the right pivot
        for value in lst[left_bound:right_bound]:
            # Iterate each value in the sublist, and add them to the correct bucket depending on if they are < left
            # pivot, > right pivot, or between the pivots
            if value < left_pivot_value:
                less.append(value)
            elif value > right_pivot_value:
                greater.append(value)
            else:
                between.append(value)

        # Rewrite the elements in the sublist back as they were ordered in the partitioning
        # [ values < left_pivot ], left_pivot, [ values between both pivots ], right_pivot, [ values > right_pivot]
        lst[left:left + len(less)] = less
        lst[left + len(less)] = left_pivot_value
        # Add 1 every time a pivot is placed
        lst[left + len(less) + 1:left + len(less) + len(between) + 1] = between
        lst[left + len(less) + len(between) + 1] = right_pivot_value
        # Add 1 every time a pivot is placed (now it should be +2)
        lst[left + len(less) + len(between) + 2:right] = greater
        # Partition the left sublist if it isn't a singular element
        if len(less) > 1:
            stack.append((left, left + len(less)))
        # Partition the between sublist if it isn't a singular element
        if len(between) > 1:
            stack.append((left + len(less) + 1, left + len(less) + len(between) + 1))
        # Partition the right sublist if it isn't a singular element
        if len(greater) > 1:
            stack.append((left + len(less) + len(between) + 2, right))
