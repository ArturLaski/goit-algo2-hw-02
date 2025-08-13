from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """Znajduje optymalny sposób cięcia pręta metodą memoizacji"""

    memo = {}

    def cut_rod(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0, []
        max_profit = -1
        best_cuts = []
        for i in range(n):
            profit, cuts = cut_rod(n - (i + 1))
            if profit + prices[i] > max_profit:
                max_profit = profit + prices[i]
                best_cuts = cuts + [i + 1]
        memo[n] = max_profit, best_cuts
        return max_profit, best_cuts

    max_profit, cuts = cut_rod(length)
    num_cuts = len(cuts) - 1 if cuts else 0
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": num_cuts
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """Znajduje optymalny sposób cięcia pręta metodą tabulacji"""

    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        max_profit = -1
        best_cuts = []
        for j in range(i):
            if dp[i - (j + 1)] + prices[j] > max_profit:
                max_profit = dp[i - (j + 1)] + prices[j]
                best_cuts = cuts[i - (j + 1)] + [j + 1]
        dp[i] = max_profit
        cuts[i] = best_cuts

    num_cuts = len(cuts[length]) - 1 if cuts[length] else 0
    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": num_cuts
    }


def run_tests():
    """Funkcja uruchamiająca testy dla obu metod"""

    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Przypadek bazowy"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Optymalnie nie ciąć"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Równomierne cięcia"
        }
    ]

    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Długość pręta: {test['length']}")
        print(f"Ceny: {test['prices']}")

        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nWynik memoizacji:")
        print(f"Maksymalny zysk: {memo_result['max_profit']}")
        print(f"Cięcia: {memo_result['cuts']}")
        print(f"Liczba cięć: {memo_result['number_of_cuts']}")

        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nWynik tabulacji:")
        print(f"Maksymalny zysk: {table_result['max_profit']}")
        print(f"Cięcia: {table_result['cuts']}")
        print(f"Liczba cięć: {table_result['number_of_cuts']}")

        print("\nSprawdzenie zakończone pomyślnie!")


if __name__ == "__main__":
    run_tests()
