import sys
import time

import requests


def check_url(url):
    try:
        start_time = time.time()

        response = requests.get(url, timeout=10)

        response_time = (time.time() - start_time) * 1000

        print(f"URL: {url}")

        if response.status_code < 400:
            print("Status: ONLINE")
        elif response.status_code < 500:
            print("Status: CLIENT ERROR")
        else:
            print("Status: SERVER ERROR")

        print(f"HTTP Status: {response.status_code}")
        print(f"Response Time: {response_time:.0f} ms")

    except requests.RequestException as error:
        print(f"URL: {url}")
        print("Status: OFFLINE")
        print(f"Error: {error}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python monitor.py <URL>")
        sys.exit(1)

    check_url(sys.argv[1])
