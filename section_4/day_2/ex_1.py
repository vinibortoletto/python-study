def recursive_sum(n):
    if n == 0:
        return 0

    print(n)
    return n + recursive_sum(n - 1)


recursive_sum(10)
