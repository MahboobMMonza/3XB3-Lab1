from utilities import confirm_sorter_correctness


def bottom_up_merge_sort(lst: list):
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


if __name__ == '__main__':
    pass
