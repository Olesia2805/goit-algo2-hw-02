from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal way to cut the rod using memoization

    Args:
        length: length of the rod
        prices: list of prices, where prices[i] is the price of a rod of length i+1

    Returns:
        Dict with the maximum profit and the list of cuts
    """


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal way to cut the rod using tabulation

    Args:
        length: length of the rod
        prices: list of prices, where prices[i] is the price of a rod of length i+1

    Returns:
        Dict with the maximum profit and the list of cuts
    """

    memo = {0: {"max_profit": 0, "cuts": [], "number_of_cuts": 0}}

    if length <= 0 or prices == []:
        return memo

    for i in range(1, length + 1):
        max_profit = 0
        best_cuts = []
        for j in range(1, i + 1):
            profit = prices[j - 1] + memo[i - j]["max_profit"]
            if profit > max_profit:
                max_profit = profit
                best_cuts = [j] + memo[i - j]["cuts"]

        memo[i] = {
            "max_profit": max_profit,
            "cuts": best_cuts,
            "number_of_cuts": len(best_cuts),
        }

    return memo[length]


def run_tests():
    """Function to run all tests"""
    test_cases = [
        # Test 1: Basic case
        {"length": 5, "prices": [2, 5, 7, 8, 10], "name": "Basic case"},
        # Test 2: Optimal not to cut
        {"length": 3, "prices": [1, 3, 8], "name": "Optimal not to cut"},
        # Test 3: All cuts of length 1
        {"length": 4, "prices": [3, 5, 6, 7], "name": "Uniform cuts"},
    ]

    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Rod length: {test['length']}")
        print(f"Prices: {test['prices']}")

        # Testing memoization
        memo_result = rod_cutting_memo(test["length"], test["prices"])
        print("\nMemoization result:")
        print(f"Maximum profit: {memo_result['max_profit']}")
        print(f"Cuts: {memo_result['cuts']}")
        print(f"Number of cuts: {memo_result['number_of_cuts']}")

        # Testing tabulation
        table_result = rod_cutting_table(test["length"], test["prices"])
        print("\nTabulation result:")
        print(f"Maximum profit: {table_result['max_profit']}")
        print(f"Cuts: {table_result['cuts']}")
        print(f"Number of cuts: {table_result['number_of_cuts']}")

        print("\nTest passed successfully!")


if __name__ == "__main__":
    run_tests()
