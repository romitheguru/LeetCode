def solve_1(arr):
    n = len(arr)
    # brute force solution
    result = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                add = arr[i] + arr[j] + arr[k]
                if add == 0:
                    result.append([arr[i], arr[j], arr[k]])

    return result


def main():
    arr = [int(i) for i in input().split()]
    output = solve_1(arr)
    print(output)


if __name__ == '__main__':
    main()
