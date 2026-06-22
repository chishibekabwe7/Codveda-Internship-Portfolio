# API Integration - Cryptocurrency Price Tracker
# Codveda Internship - Level 2
# Author: Chishibe Kabwe

import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"

COINS = {
    "1": ("bitcoin", "Bitcoin (BTC)"),
    "2": ("ethereum", "Ethereum (ETH)"),
    "3": ("solana", "Solana (SOL)"),
    "4": ("binancecoin", "BNB"),
    "5": ("ripple", "XRP"),
}


def display_menu():
    print("=" * 45)
    print("        CRYPTOCURRENCY PRICE TRACKER")
    print("=" * 45)
    for key, (_, label) in COINS.items():
        print(f"{key}. {label}")
    print("6. View all")
    print("7. Exit")
    print("-" * 45)


def fetch_prices(coin_ids):
    params = {
        "ids": ",".join(coin_ids),
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Check your internet connection.\n")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection.\n")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: API returned an error response ({e}).\n")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An unexpected request error occurred ({e}).\n")
        return None
    except ValueError:
        print("Error: Could not parse the API response.\n")
        return None


def display_prices(data, coin_ids):
    if not data:
        return

    print("\n" + "-" * 45)
    print(f"{'Coin':<20}{'Price (USD)':<15}{'24h Change'}")
    print("-" * 45)

    for coin_id in coin_ids:
        label = next((name for cid, (key, name) in COINS.items() if key == coin_id), coin_id)

        if coin_id not in data:
            print(f"{label:<20}{'N/A':<15}{'N/A'}")
            continue

        price = data[coin_id].get("usd")
        change = data[coin_id].get("usd_24h_change")

        price_str = f"${price:,.2f}" if price is not None else "N/A"
        change_str = f"{change:+.2f}%" if change is not None else "N/A"

        print(f"{label:<20}{price_str:<15}{change_str}")

    print("-" * 45 + "\n")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()
        print()

        if choice in COINS:
            coin_id, _ = COINS[choice]
            data = fetch_prices([coin_id])
            display_prices(data, [coin_id])

        elif choice == "6":
            all_ids = [coin_id for coin_id, _ in COINS.values()]
            data = fetch_prices(all_ids)
            display_prices(data, all_ids)

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.\n")


if __name__ == "__main__":
    main()