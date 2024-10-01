import requests
import threading
import os

# Clear console based on the system type
os.system('cls' if os.name == 'nt' else 'clear')  

# Configuration
timeout = 1  # Timeout in seconds
allow_redirects = True  # Allow redirects
urls_file = 'urls.txt'
http_codes_file = 'httpcodes.txt'

# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Initial configuration output
print(f"Current configuration:\n\nTimeout: {timeout} seconds\nAllow redirects: {allow_redirects}\nURLs: {urls_file}\nAllowed HTTP codes: {http_codes_file}\nANSI codes: {GREEN}Green {RED}Red {RESET}Reset\n\n------- STARTING -------")

# Check if the files exist
if not os.path.exists(urls_file):
    print(f"Error: {urls_file} file not found.")
    exit(1)
if not os.path.exists(http_codes_file):
    print(f"Error: {http_codes_file} file not found.")
    exit(1)

# Function to read URLs from a file
def read_urls(file_name):
    with open(file_name, 'r') as file:
        urls = file.read().split(',')
        return [url.strip() for url in urls if url.strip()]

# Function to read HTTP codes from a file
def read_http_codes(file_name):
    with open(file_name, 'r') as file:
        codes = file.read().split(',')
        return [int(code.strip()) for code in codes if code.strip().isdigit()]

# Function to check each URL
def check_url(url, http_codes, timeout=timeout):
    try:
        response = requests.head(f'http://{url}', allow_redirects=allow_redirects, timeout=timeout)
        if response.status_code in http_codes:
            return f"{GREEN}{response.status_code} found for {url}{RESET}", url
        else:
            return f"{GREEN}{response.status_code} OK for {url}{RESET}", url if 200 in http_codes else None
    except requests.exceptions.ConnectTimeout:
        return f"{RED}Error: {url} timeout{RESET}", None
    except requests.exceptions.RequestException as e:
        return f"{RED}Error: {url} ({e}){RESET}", None

# Function to run the URL checking in a separate thread
def run_check(url, http_codes, ok_urls):
    print(f"Checking domain: {url}")  # Print the domain being checked
    result, ok_url = check_url(url, http_codes)
    print(result)
    if ok_url:
        ok_urls.append(ok_url)

# Main logic
try:
    urls = read_urls(urls_file)
    http_codes = read_http_codes(http_codes_file)

    ok_urls = []  # List to store URLs with "OK" or expected status codes
    threads = []

    # Create a thread for each URL
    for url in urls:
        thread = threading.Thread(target=run_check, args=(url, http_codes, ok_urls))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

except KeyboardInterrupt:
    print("\nProcess interrupted by user.")

# Print summary of OK responses
print("------- DONE -------")
print("Successful URLs:")
for ok_url in ok_urls:
    print(f'{GREEN}{ok_url}{RESET}')
