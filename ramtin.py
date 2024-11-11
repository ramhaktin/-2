import tkinter as tk
from tkinter import simpledialog
import requests
import threading
import time

# تابع ارسال درخواست HTTP
def send_http_requests(ip, port=80):
    url = f"http://{ip}:{port}"
    for _ in range(3):
        try:
            response = requests.get(url)
            print(f"Request sent to {url}, Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error occurred: {e}")
        time.sleep(1)  # فاصله 1 ثانیه بین درخواست‌ها

# تابع برای درخواست IP و پورت
def get_ip_and_port():
    root = tk.Tk()
    root.withdraw()  # پنجره اصلی نمایش داده نمی‌شود، فقط دیالوگ‌ها نمایش داده می‌شوند

    # نمایش دیالوگ برای وارد کردن IP
    ip = simpledialog.askstring("IP Request", "Please enter the IP:")
    if ip:
        # نمایش دیالوگ برای وارد کردن پورت (پورت پیش‌فرض 80)
        port = simpledialog.askinteger("Port Request", "Please enter the port (default 80):", initialvalue=80)
        port = port or 80  # اگر پورت وارد نشد، پورت پیش‌فرض 80 در نظر گرفته می‌شود

        print(f"Sending requests to {ip}:{port}")
        
        # ایجاد یک رشته جداگانه برای ارسال درخواست‌ها بدون مسدود کردن ترمینال
        threading.Thread(target=send_http_requests, args=(ip, port)).start()

if __name__ == "__main__":
    get_ip_and_port()
