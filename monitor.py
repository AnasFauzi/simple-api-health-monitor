import sys
import time
import requests


def check_url(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = (time.time() - start_time) * 1000

        print(f"\nURL: {url}")
        print("Status: ONLINE")
        print(f"HTTP Status: {response.status_code}")
        print(f"Response Time: {response_time:.0f} ms")

    except requests.RequestException as error:
        print(f"\nURL: {url}")
        print("Status: OFFLINE")
        print(f"Error: {error}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python monitor.py <URL>")
        sys.exit(1)

    check_url(sys.argv[1])
