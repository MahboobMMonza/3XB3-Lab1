from utilities import confirm_sorter_correctness


def bottom_up_mergesort(lst: list):
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


def dual_pivot_quicksort(lst: list):
    # Add left and right bounds for partition to the stack, right bound is excluded
    stack = [(0, len(lst))]
    # Instead of making recursive partition calls, use a stack to hold the arguments and a while loop to
    # partition along the arguments
    while stack:
        # Partition bounds
        left, right = stack.pop()
        # base cases of <= 1 difference between left and right, as well as when left and right span just 2 elements
        if right - left <= 1:
            continue
        elif right - left == 2 and lst[right - 1] < lst[left]:
            lst[left], lst[right - 1] = lst[right - 1], lst[left]
            continue
        # Choose pivot locations as left and right endpoints, and swap them if right point is smaller than left
        if lst[left] > lst[right - 1]:
            lst[left], lst[right - 1] = lst[right - 1], lst[left]
        # Do partition
        cur_idx, left_bound, right_bound = left + 1, left, right - 1
        while cur_idx < right_bound:
            # Current value is less than the left pivot
            if lst[cur_idx] < lst[left]:
                left_bound += 1
                lst[left_bound], lst[cur_idx] = lst[cur_idx], lst[left_bound]
                cur_idx += 1
            elif lst[cur_idx] >= lst[right - 1]:
                # Whenever there is a swap with the right bound, don't change the iterator value because the swapped
                # value needs to be checked
                right_bound -= 1
                lst[right_bound], lst[cur_idx] = lst[cur_idx], lst[right_bound]
            else:
                cur_idx += 1

        if left != left_bound:
            lst[left_bound], lst[left] = lst[left], lst[left_bound]
        if right - 1 != right_bound:
            lst[right_bound], lst[right - 1] = lst[right - 1], lst[right_bound]
        # partition(right_bound + 1, right_bound)
        stack.append((right_bound + 1, right))
        # partition(left, left_bound)
        stack.append((left, left_bound))
        # partition(left_bound + 1, right_bound)
        stack.append((left_bound + 1, right_bound))


if __name__ == '__main__':
    pass
