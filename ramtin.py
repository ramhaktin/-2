import time
import requests
from termcolor import colored

def get_user_input():
    print("Welcome to the HTTP Request Tool!")
    ip_address = input("Please enter the IP address: ")
    while not ip_address:  # بررسی آی‌پی
        print(colored("Invalid IP address. Please try again.", "red"))
        ip_address = input("Please enter the IP address: ")

    website_url = input("Please enter the website URL: ")
    while not website_url:  # بررسی URL
        print(colored("Invalid URL. Please try again.", "red"))
        website_url = input("Please enter the website URL: ")

    port = input("Please enter the port: ")
    while not port.isdigit():  # بررسی پورت
        print(colored("Invalid port. Please enter a valid number.", "red"))
        port = input("Please enter the port: ")

    return ip_address, website_url, port

def send_http_requests(ip, url, port):
    full_url = f"http://{ip}:{port}/{url}"
    count = 0
    while True:
        for _ in range(999):  # ارسال 999 درخواست
            try:
                response = requests.get(full_url)
                # نمایش پاسخ به صورت سبز
                print(colored(f"Request {count + 1}: {full_url} | Status: {response.status_code}", "green"))
                count += 1
            except Exception as e:
                print(colored(f"Error: {e}", "red"))
        time.sleep(60)  # درخواست‌ها هر 1 دقیقه یک‌بار تکرار می‌شود

if __name__ == "__main__":
    ip, url, port = get_user_input()
    send_http_requests(ip, url, port)
