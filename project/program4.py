from typing import List, Tuple

def program4(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Algorithm4: Θ(n^3) DP with dp[k][j].
    dp[k][j] = minimum total height to place sculptures 0..j using exactly k platforms.
    """

    if n == 0:
        return 0, 0, []

    INF = 10**18

    # cost[i][j] = height of one platform containing sculptures i..j, or INF if too wide
    cost = [[INF] * n for _ in range(n)]
    for i in range(n):
        width_sum = 0
        max_h = 0
        for j in range(i, n):
            width_sum += widths[j]
            if width_sum > W:
                break
            if heights[j] > max_h:
                max_h = heights[j]
            cost[i][j] = max_h

    # dp[k][j] for k = 1..n, j = 0..n-1
    dp = [[INF] * n for _ in range(n + 1)]

    # base: one platform
    for j in range(n):
        dp[1][j] = cost[0][j]

    # transitions
    for k in range(2, n + 1):
        for j in range(k - 1, n):
            best = INF
            for i in range(k - 2, j):
                if cost[i + 1][j] == INF:
                    continue
                val = dp[k - 1][i] + cost[i + 1][j]
                if val < best:
                    best = val
            dp[k][j] = best

    # choose best number of platforms
    best_total = INF
    best_k = 1
    for k in range(1, n + 1):
        if dp[k][n - 1] < best_total:
            best_total = dp[k][n - 1]
            best_k = k

    # reconstruct
    groups: List[int] = []
    k = best_k
    j = n - 1
    while k > 1:
        for i in range(k - 2, j):
            if cost[i + 1][j] == INF:
                continue
            if dp[k - 1][i] + cost[i + 1][j] == dp[k][j]:
                groups.append(j - (i + 1) + 1)   # sculptures on this platform
                j = i
                k -= 1
                break
    groups.append(j + 1)  # first platform
    groups.reverse()

    m = len(groups)
    total_height = best_total
    return m, total_height, groups


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, groups = program4(n, W, heights, widths)
    print(m)
    print(total_height)
    for g in groups:
        print(g)
