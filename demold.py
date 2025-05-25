import os
import requests
import time
from colorama import Fore, Style
from art import *
from tabulate import tabulate
import json

# Khởi tạo session và user agent
ses = requests.Session()
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

headers = {
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://app.golike.net/',
    'User-Agent': User_Agent,
    'Content-Type': 'application/json;charset=utf-8'
}

# Xử lý Authorization
if os.path.exists('user.txt'):
    use_old = input("Bạn có muốn dùng Authorization cũ không? (y/n): ")
    if use_old.lower() == 'y':
        with open('user.txt', 'r') as f:
            headers["Authorization"] = f.read().strip()
    else:
        auth = input("Nhập Authorization mới: ")
        with open('user.txt', 'w') as f:
            f.write(auth)
        headers["Authorization"] = auth
else:
    auth = input("Nhập Authorization lần đầu: ")
    with open('user.txt', 'w') as f:
        f.write(auth)
    headers["Authorization"] = auth

# Hàm banner
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.CYAN}{Style.BRIGHT}╔════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║       SCODE Golike Linkedin v1.0       ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║   Created by: NGUYỄN VĂN ĐẠT         ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚════════════════════════════════════╝{Style.RESET_ALL}")
    print()

# Hàm đếm ngược
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        print(f"\r{Fore.YELLOW}⏳ Đợi: {remaining_time}s...{Style.RESET_ALL}", end="")
        time.sleep(1)
    print()

# Hàm hiển thị menu
def LIST():
    print(f"{Fore.YELLOW}📋 MENU CHÍNH{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] Chạy tool LinkedIn")
    print(f"[2] Xóa Authorization hiện tại{Style.RESET_ALL}")

# Hàm chính LinkedIn
def LINKEDIN():
    checkaccount = requests.get('https://gateway.golike.net/api/linkedin-account', headers=headers).json()
    user_linkedin1 = []
    account_id1 = []

    i = 1
    banner()
    print(f"{Fore.YELLOW}📋 DANH SÁCH TÀI KHOẢN LINKEDIN{Style.RESET_ALL}")
    for data in checkaccount['data']:
        usernametk = data['name']
        user_linkedin1.append(usernametk)
        account_id1.append(data['id'])
        print(f"{Fore.GREEN}[{i}] {usernametk} - Hoạt động{Style.RESET_ALL}")
        i += 1

    choose = int(input(f"{Fore.YELLOW}➤ Chọn tài khoản (1-{len(user_linkedin1)}): {Style.RESET_ALL}"))
    user_tiktok = user_linkedin1[choose - 1]
    account_id = account_id1[choose - 1]

    ck_file = f'COOKIELINKEDIN{account_id}.txt'
    if os.path.exists(ck_file):
        with open(ck_file, 'r') as f:
            COOKIELINK = f.read()
    else:
        COOKIELINK = input(f"{Fore.GREEN}Nhập Cookie LinkedIn cho {user_tiktok}:{Style.RESET_ALL} ")
        with open(ck_file, 'w') as f:
            f.write(COOKIELINK)

    SL = int(input("Số lượng job cần chạy: "))
    DELAY = int(input("Delay giữa các job (giây): "))
    
    dem = 0
    tong = 0
    for i in range(SL):
        url2 = f'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs?account_id={account_id}&data=null'
        try:
            checkurl2 = ses.get(url2, headers=headers).json()
        except:
            print("Lỗi kết nối hoặc lỗi API")
            break

        if checkurl2['status'] == 200:
            ads_id = checkurl2['data']['id']
            object_id = checkurl2['data']['object_id']
            typejob = checkurl2['data']['type']
            countdown(DELAY)

            if typejob == 'follow':
                headers_follow = {
                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                    'cookie': COOKIELINK,
                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                    'user-agent': User_Agent,
                }
                _ = requests.get(checkurl2['data']['link'], headers=headers_follow)
                json_data2 = {'account_id': account_id, 'ads_id': ads_id}
                url_complete = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                check = requests.post(url_complete, headers=headers, json=json_data2).json()

                if check['success']:
                    dem += 1
                    prices = check['data']['prices']
                    tong += prices
                    print(f"{Fore.GREEN}[{dem}] ✔ Follow +{prices} VNĐ | Tổng: {tong}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}✖ Job thất bại{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Không có job nào được lấy hoặc lỗi!{Style.RESET_ALL}")
            break

    print(f"{Fore.YELLOW}Hoàn thành {dem} job, tổng: {tong} VNĐ{Style.RESET_ALL}")

# Bắt đầu
banner()
url1 = 'https://gateway.golike.net/api/users/me'
try:
    checkurl1 = ses.get(url1, headers=headers).json()
    if checkurl1['status'] == 200:
        print(f"{Fore.GREEN}✅ Đăng nhập thành công!{Style.RESET_ALL}")
        time.sleep(1)
        username = checkurl1['data']['username']
        coin = checkurl1['data']['coin']
        print(f"Tên tài khoản: {username} | Số dư: {coin} VNĐ")
        LIST()
        choose = int(input("Chọn chức năng (1-2): "))
        if choose == 1:
            LINKEDIN()
        elif choose == 2:
            os.remove('user.txt')
            print(f"{Fore.GREEN}Đã xóa Authorization{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}❌ Đăng nhập thất bại!{Style.RESET_ALL}")
except:
    print(f"{Fore.RED}Lỗi khi gửi yêu cầu tới API!{Style.RESET_ALL}")
