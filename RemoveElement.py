def removeElement_1(nums, val):
    """
    Brute force solution
    Don't preserve order
    """
    # count the frequency of the val
    val_freq = 0
    for num in nums:
        if num == val:
            val_freq += 1
    # print(val_freq)
    new_len = len(nums) - val_freq

    # remove the element from the list
    i = 0
    j = len(nums) - 1
    while val_freq > 0 and i < new_len:
        if nums[i] == val:
            print('index:', i)
            while j > 0 and nums[j] == val:
                j -= 1
            print('j:', j)
            # swap elements
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            val_freq -= 1
            j -= 1
        i += 1
        
    return new_len


def removeElement_2(nums, val):
    """
    Using one loop and two pointers
    Don't preserve order
    """

    # Remove the elment from the list
    i = 0
    j = len(nums) - 1
    count = 0

    while i < j:
        if nums[i] == val:
            while j > i and nums[j] == val:
                j -= 1
            print('i:', i, 'j:', j)
            # swap elements
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            count += 1
            print(nums)
        i += 1

    if count == 0:
        j = j + 1
    return j


def main():
    arr = [int(j) for j in input().split()]
    val = int(input())
    ans = removeElement_2(arr, val)
    print(ans)
    print(arr[:ans])


if __name__ == '__main__':
    main()
