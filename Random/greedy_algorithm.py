# Greedy Algorithm Example: Coin Change Problem
# This program demonstrates the greedy algorithm approach using the Coin Change problem.
# It selects the largest coin denomination at each step to minimize the number of coins used.

def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

def main():
    coins = [1, 5, 10, 25]
    amount = 63
    print(f"Coins used to make {amount}: {coin_change(coins, amount)}")

if __name__ == "__main__":
    main()