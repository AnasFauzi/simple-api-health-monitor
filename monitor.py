import sys
import time

import requests


def check_url(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = (time.time() - start_time) * 1000

        if response.status_code < 400:
            status = "ONLINE"
        elif response.status_code < 500:
            status = "CLIENT ERROR"
        else:
            status = "SERVER ERROR"

        print(f"URL: {url}")
        print(f"Status: {status}")
        print(f"HTTP Status: {response.status_code}")
        print(f"Response Time: {response_time:.0f} ms")
        print()

        return True

    except requests.RequestException as error:
        print(f"URL: {url}")
        print("Status: OFFLINE")
        print(f"Error: {error}")
        print()

        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python monitor.py <URL> [URL ...]")
        sys.exit(1)

    results = []

    for url in sys.argv[1:]:
        results.append(check_url(url))

    if not all(results):
        sys.exit(1)


if __name__ == "__main__":
    main()
