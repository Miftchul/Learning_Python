import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    data = response.json()
    if "rates" in data and target_currency in data["rates"]:
        return data["rates"][target_currency]
    else:
        raise ValueError("Invalid currency code or API error.")

def main():
    print("Currency Converter")
    base = input("From currency (e.g. USD): ").upper()
    target = input("To currency (e.g. IDR): ").upper()
    amount = float(input(f"Amount in {base}: "))

    try:
        rate = get_exchange_rate(base, target)
        converted = amount * rate
        print(f"{amount:.2f} {base} = {converted:.2f} {target} (Rate: {rate:.4f})")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()