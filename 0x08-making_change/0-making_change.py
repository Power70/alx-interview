#!/usr/bin/python3
"""
    This function takes in a list of coins and an amount and returns
    the minimum number of coins needed to make the amount.
"""


def makeChange(coin, amount):
    """
    This function takes in a list of coins and an amount and returns
    the minimum number of coins needed to make the amount.
    """
    if (amount < 1):
        return 0
    if all(c > amount for c in coin):
        return -1
    array = [(amount + 1)] * (amount + 1)
    # print(array)
    # print(len(array))
    array[0] = 0
    for A in range(1, (len(array))):
        # print("New iteration")
        for i in range(len(coin)):
            # print("New coin")
            # print(f"This is A : {A}")
            if (A < coin[i]):
                continue
            step = A - coin[i]
            new_min = array[step] + 1
            # print(f"This is min :{min}")
            # print(f"This is new_min :{new_min}")
            if array[A] == (amount + 1):
                array[A] = new_min
            elif new_min < array[A]:
                array[A] = new_min
        # print(f"\n{array}\n")
    if array[amount] > amount:
        return -1
    return array[amount]
    # print(f"This is best for amount :{array[amount]}")
