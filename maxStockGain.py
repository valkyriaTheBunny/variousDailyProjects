def maxStockGain(prices: list[int], fee: int) -> int:
    hold = -prices[0]
    cash = 0

    for price in prices:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)

    return cash

def test_maxStockGain():
    assert maxStockGain([1, 3, 2, 8, 4, 10], 2) == 9

def main() -> None:
    print(maxStockGain([4, 2, 6, 9, 7, 3, 1, 11], 3))

if __name__ == "__main__":
    main()
