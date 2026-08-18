import sys
import time
import requests


def check_url(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = (time.time() - start_time) * 1000

        if 200 <= response.status_code < 300:
            status = "ONLINE"
        elif 300 <= response.status_code < 400:
            status = "REDIRECT"
        elif 400 <= response.status_code < 500:
            status = "CLIENT ERROR"
        else:
            status = "SERVER ERROR"

        print(f"\nURL: {url}")
        print(f"Status: {status}")
        print(f"HTTP Status: {response.status_code}")
        print(f"Response Time: {response_time:.0f} ms")

    except requests.Timeout:
        print(f"\nURL: {url}")
        print("Status: OFFLINE")
        print("Error: Request timed out")

    except requests.ConnectionError:
        print(f"\nURL: {url}")
        print("Status: OFFLINE")
        print("Error: Could not connect to the server")

    except requests.RequestException as error:
        print(f"\nURL: {url}")
        print("Status: OFFLINE")
        print(f"Error: {error}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python monitor.py <URL>")
        sys.exit(1)

    check_url(sys.argv[1])
