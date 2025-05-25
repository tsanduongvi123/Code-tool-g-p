import os import requests import time from colorama import Fore, Style from art import * from tabulate import tabulate

=== Cài đặt tự động nếu thiếu ===

try: import requests import time import os from art import * from colorama import Fore, Style import json import random from time import sleep import sys from tabulate import tabulate except ImportError: os.system("pip install requests tabulate art colorama")

=== Hàm đếm ngược ===

def countdown(time_sec): for remaining_time in range(time_sec, -1, -1): colors = [ f"{Fore.CYAN}OFFTO {Fore.YELLOW}OL 🍉 {Fore.GREEN}VIP Tool{Style.RESET_ALL}", f"{Fore.MAGENTA}OFFTO {Fore.CYAN}OL 🍉 {Fore.GREEN}VIP Tool{Style.RESET_ALL}", f"{Fore.YELLOW}OFFTO {Fore.BLUE}OL 🍉 {Fore.GREEN}VIP Tool{Style.RESET_ALL}", ] for color in colors: print(f"\r{color} | Đếm ngược: {Fore.YELLOW}{remaining_time}s{Style.RESET_ALL}", end="") time.sleep(0.12) print(f"\r{Fore.GREEN}Đang xử lý công việc...{Style.RESET_ALL}", end="\r") time.sleep(1) print("\r" + " " * 50 + "\r", end="")

=== Banner ===

def banner(): os.system('cls' if os.name == 'nt' else 'clear') print(f"{Fore.CYAN}{Style.BRIGHT}╔════════════════════════════════════════════════╗{Style.RESET_ALL}") print(f"{Fore.CYAN}║       SCODE Golike Linkedin v1.0       ║{Style.RESET_ALL}") print(f"{Fore.CYAN}║   Created by: NGUYỄN VĂN ĐẠT         ║{Style.RESET_ALL}") print(f"{Fore.CYAN}╚═══════════════════════════════════════════════╝{Style.RESET_ALL}\n")

=== Load token vào headers ===

def load_token(): token = None if os.path.exists("user.txt"): with open("user.txt", "r") as f: token = f.read().strip() use_old = input(f"{Fore.YELLOW}Dùng lại token cũ không? (y/n): {Style.RESET_ALL}").strip().lower() if use_old != "y": token = input(f"{Fore.GREEN}Nhập Authorization Token mới (Bearer ...): {Style.RESET_ALL}").strip() with open("user.txt", "w") as f: f.write(token) else: token = input(f"{Fore.GREEN}Nhập Authorization Token (Bearer ...): {Style.RESET_ALL}").strip() with open("user.txt", "w") as f: f.write(token) return token

=== Hiển thị menu ===

def LIST(): print(f"{Fore.YELLOW}📋 MENU CHÍNH{Style.RESET_ALL}") print(f"{Fore.CYAN}═══════════════════════════════════════════{Style.RESET_ALL}") print(f"{Fore.GREEN}[1] Chạy tool LinkedIn{Style.RESET_ALL}") print(f"{Fore.GREEN}[2] Nhập lại Authorization Token{Style.RESET_ALL}") print(f"{Fore.CYAN}═══════════════════════════════════════════{Style.RESET_ALL}")

=== Tool LinkedIn ===

def LINKEDIN(headers): checkaccount = requests.get('https://gateway.golike.net/api/linkedin-account', headers=headers).json() user_linkedin1 = [] account_id1 = [] i = 1

banner()
print(f"{Fore.YELLOW}📋 DANH SÁCH TÀI KHOẢN LINKEDIN{Style.RESET_ALL}")
print(f"{Fore.CYAN}═══════════════════════════════════════════{Style.RESET_ALL}")
for data in checkaccount['data']:
    usernametk = data['name']
    user_linkedin1.append(usernametk)
    account_id1.append(data['id'])
    print(f"{Fore.GREEN}[{i}] {Fore.WHITE}Tài khoản: {Fore.YELLOW}{usernametk} {Fore.GREEN}- Trạng thái: Hoạt động{Style.RESET_ALL}")
    i += 1
print(f"{Fore.CYAN}═══════════════════════════════════════════{Style.RESET_ALL}")

choose = int(input(f"{Fore.YELLOW}➤ Nhập số thứ tự tài khoản (1-{len(user_linkedin1)}): {Style.RESET_ALL}"))
os.system('cls' if os.name == 'nt' else 'clear')
if 1 <= choose <= len(user_linkedin1):
    user_tiktok = user_linkedin1[choose - 1]
    account_id = account_id1[choose - 1]

    checkfile = os.path.isfile(f'COOKIELINKEDIN{account_id}.txt')
    if not checkfile:
        banner()
        COOKIELINK = input(f"{Fore.GREEN}🔑 Nhập Cookie LinkedIn cho {user_tiktok}: {Style.RESET_ALL}")
        with open(f'COOKIELINKEDIN{account_id}.txt', 'w') as f:
            f.write(COOKIELINK)
    else:
        with open(f'COOKIELINKEDIN{account_id}.txt', 'r') as f:
            COOKIELINK = f.read()

    banner()
    print(f"{Fore.YELLOW}🔧 CÀI ĐẶT CÔNG VIỆC{Style.RESET_ALL}")
    job_num = int(input(f"{Fore.GREEN}📌 Số lượng job cần thực hiện: {Style.RESET_ALL}"))
    DELAY = int(input(f"{Fore.GREEN}⏱ Thời gian delay (giây): {Style.RESET_ALL}"))

    print(f"{Fore.CYAN}═══════════════════════════════════════════{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🚀 Bắt đầu thực hiện công việc{Style.RESET_ALL}")
    dem = 0
    tong = 0
    for i in range(job_num):
        url2 = f'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs?account_id={account_id}&data=null'
        checkurl2 = requests.get(url2, headers=headers).json()
        if checkurl2['status'] == 200:
            ads_id = checkurl2['data']['id']
            object_id = checkurl2['data']['object_id']
            type_job = checkurl2['data']['type']
            countdown(DELAY)

            if type_job == 'follow':
                headers_follow = {
                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                    'cookie': COOKIELINK,
                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                    'user-agent': headers['User-Agent'],
                }
                requests.get(checkurl2['data']['link'], headers=headers_follow)
                json_data2 = {'account_id': account_id, 'ads_id': ads_id}
                url_complete = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                check = requests.post(url_complete, headers=headers, json=json_data2).json()

                if check['success']:
                    dem += 1
                    prices = check['data']['prices']
                    tong += prices
                    now = time.localtime()
                    timestamp = f"{now.tm_hour:02d}:{now.tm_min:02d}:{now.tm_sec:02d}"
                    print(f"{Fore.GREEN}[{dem}] {Fore.YELLOW}{timestamp} {Fore.GREEN}✔ {type_job.capitalize()} +{prices} | Tổng: {Fore.YELLOW}{tong} VNĐ{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}✖ Thất bại - Bỏ qua job{Style.RESET_ALL}")

    print(f"{Fore.CYAN}═══════════════════════════════════════════{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🌟 HOÀN THÀNH: {dem} job thành công | Tổng tiền: {tong} VNĐ{Style.RESET_ALL}")

=== Chạy chương trình ===

banner() token = load_token() headers = { 'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8', 'Referer': 'https://app.golike.net/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', "Authorization": token, 'Content-Type': 'application/json;charset=utf-8' }

while True: banner() LIST() choose = input(f"{Fore.YELLOW}➤ Chọn chức năng (1-2): {Style.RESET_ALL}").strip() if choose == "1": LINKEDIN(headers) break elif choose == "2": token = input(f"{Fore.GREEN}Nhập Authorization Token mới (Bearer ...): {Style.RESET_ALL}").strip() with open("user.txt", "w") as f: f.write(token) headers["Authorization"] = token print(f"{Fore.GREEN}Đã cập nhật token mới.{Style.RESET_ALL}") time.sleep(2) else: print(f"{Fore.RED}Lựa chọn không hợp lệ.{Style.RESET_ALL}") time.sleep(2)

