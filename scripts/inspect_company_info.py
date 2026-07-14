from pprint import pprint

import yfinance as yf


def main():
    ticker = yf.Ticker("TCS.NS")

    info = ticker.info

    print("\n" + "=" * 80)
    print("Yahoo Finance Company Information")
    print("=" * 80)

    print(f"\nTotal fields: {len(info)}\n")

    pprint(sorted(info.keys()))


if __name__ == "__main__":
    main()