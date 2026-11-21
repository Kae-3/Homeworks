def find_one_odd_number(nums: list[int]) -> int:
    xor_all = 0
    for n in nums:
        xor_all ^= n
    return xor_all


def find_two_odd_numbers(nums: list[int]) -> tuple[int, int]:
    # Step 1: XOR all numbers. Pairs cancel out, leaving (num1 ^ num2).
    xor_both = 0
    for n in nums:
        xor_both ^= n

    # Step 2: Isolate the rightmost set bit where num1 and num2 differ.
    rightmost_set_bit = xor_both & -xor_both

    # Step 3: Partition elements by that bit and XOR each group separately.
    group_a = 0
    group_b = 0
    for n in nums:
        if n & rightmost_set_bit:
            group_a ^= n
        else:
            group_b ^= n

    return group_a, group_b


# Case 1: Single number occurring an odd number of times
single_case = [4, 2, 7, 4, 2]
print("Single odd number:", find_one_odd_number(single_case))

# Case 2: Two numbers occurring an odd number of times
pair_case = [12, 5, 9, 12, 8, 5, 8, 15]
odd1, odd2 = find_two_odd_numbers(pair_case)
print("Two odd numbers:", odd1, "and", odd2)