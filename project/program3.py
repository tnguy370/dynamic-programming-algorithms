from typing import List, Tuple

def program3(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Algorithm3: Naive exhaustive search.
    Try every possible way to place cuts between sculptures.
    """

    best_cost = float("inf")
    best_groups: List[int] = []

    def dfs(i: int, cur_width: int, cur_max: int, cur_cost: int, groups: List[int]) -> None:
        """
        i         = index of next sculpture to place (0..n)
        cur_width = current width on this platform
        cur_max   = tallest height on this platform
        cur_cost  = sum of heights of platforms already finished
        groups    = list of sculpture counts per platform so far
        """
        nonlocal best_cost, best_groups

        if i == n:
            total = cur_cost + cur_max        # finish last platform
            if total < best_cost:
                best_cost = total
                best_groups = groups.copy()
            return

        w = widths[i]
        h = heights[i]

        # Option 1: keep sculpture i on current platform
        if cur_width + w <= W:
            g1 = groups.copy()
            g1[-1] += 1
            dfs(i + 1,
                cur_width + w,
                max(cur_max, h),
                cur_cost,
                g1)

        # Option 2: start a new platform with sculpture i
        if w <= W:
            g2 = groups.copy()
            g2.append(1)
            dfs(i + 1,
                w,
                h,
                cur_cost + cur_max,
                g2)

    if n == 0:
        return 0, 0, []

    # first sculpture starts the first platform
    dfs(i=1,
        cur_width=widths[0],
        cur_max=heights[0],
        cur_cost=0,
        groups=[1])

    m = len(best_groups)
    total_height = best_cost
    return m, total_height, best_groups


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, groups = program3(n, W, heights, widths)
    print(m)
    print(total_height)
    for g in groups:
        print(g)
