from typing import List, Tuple

def program5B(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Algorithm5, bottom-up DP.
    dp[i] = minimum total height to place sculptures i..n-1.
    """

    INF = 10**18
    dp = [0] * (n + 1)          # dp[n] = 0
    choice = [-1] * n           # best end index j for start i

    for i in range(n - 1, -1, -1):
        best = INF
        best_j = i
        width_sum = 0
        max_h = 0

        for j in range(i, n):
            width_sum += widths[j]
            if width_sum > W:
                break
            if heights[j] > max_h:
                max_h = heights[j]
            cost = max_h + dp[j + 1]
            if cost < best:
                best = cost
                best_j = j

        dp[i] = best
        choice[i] = best_j

    total_height = dp[0]
    # reconstruct grouping from choices
    groups: List[int] = []
    i = 0
    while i < n:
        j = choice[i]
        groups.append(j - i + 1)
        i = j + 1

    m = len(groups)
    return m, total_height, groups


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, groups = program5B(n, W, heights, widths)
    print(m)
    print(total_height)
    for g in groups:
        print(g)
