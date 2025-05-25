
import os
import time
import requests

# Hiển thị banner
banner = '''
\033[1;31m─────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m😎\033[1;31m] \033[1;37m=> \033[1;33mTOOL GOP DGVIKAKA
\033[1;31m[\033[1;37m🤑\033[1;31m] \033[1;37m=> \033[1;35mAD: \033[1;36mVANDAT
\033[1;31m[\033[1;37m😜\033[1;31m] \033[1;37m=> \033[1;32mLH mua Key Vip: \033[1;37m0785308626
\033[1;31m[\033[1;37m \033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mKETUTIEN
\033[1;31m─────────────────────────────────────────────────────────
'''
os.system('cls' if os.name == 'nt' else 'clear')
for x in banner:
    print(x, end='')
    time.sleep(0.001)
print('\x1b[1;31m(⁀ᗢ⁀)')    

# Tạo file nếu chưa có
if not os.path.exists('Authorization.txt'):
    with open('Authorization.txt', 'w') as f:
        f.write('')
if not os.path.exists('token.txt'):
    with open('token.txt', 'w') as f:
        f.write('')

# Đọc nội dung file
with open('Authorization.txt', 'r') as f:
    author = f.read().strip()
with open('token.txt', 'r') as f:
    token = f.read().strip()

# Nếu chưa có dữ liệu thì yêu cầu nhập
if author == '' or token == '':
    author = input('\033[1;32mNHẬP AUTHORIZATION: ')
    token = input('\033[1;32mNHẬP TOKEN: ')
    with open('Authorization.txt', 'w') as f:
        f.write(author)
    with open('token.txt', 'w') as f:
        f.write(token)
else:
    select = input('\x1b[1;97m║ Nhập AUTH mới để đổi (Enter để dùng lại): ')
    if select != '':
        author = select
        token = input('\033[1;32mNHẬP TOKEN: ')
        with open('Authorization.txt', 'w') as f:
            f.write(author)
        with open('token.txt', 'w') as f:
            f.write(token)

# Headers gửi request
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok'
}

# Vòng lặp chạy job
job_api_url = 'https://app.golike.net/api/advertising/pending'
confirm_api_url = 'https://app.golike.net/api/advertising/complete'

while True:
    try:
        # Gửi request lấy danh sách nhiệm vụ
        response = requests.get(job_api_url, headers=headers).json()

        if response.get('status') == False:
            print("\033[1;31m[!] Không có nhiệm vụ nào, đợi tí rồi thử lại...")
            time.sleep(5)
            continue

        job = response['data'][0]
        job_id = job['advertising_id']
        link = job['link']

        print(f"\033[1;36m[+] Nhận Job ID: {job_id} | Mở link: {link}")
        os.system(f"xdg-open {link}")  # Tự động mở link trên Android

        for i in range(10, 0, -1):
            print(f"\033[1;33m[~] Đang chờ {i}s để xác nhận...", end='\r')
            time.sleep(1)

        # Gửi request hoàn thành job
        confirm = requests.post(confirm_api_url, headers=headers, json={"advertising_id": job_id}).json()

        if confirm.get('status') == True:
            print(f"\033[1;32m[✓] Hoàn thành Job ID: {job_id} thành công!")
        else:
            print(f"\033[1;31m[x] Thất bại: {confirm.get('message')}")
        time.sleep(3)

    except Exception as e:
        print(f"\033[1;31m[LỖI]: {e}")
        time.sleep(10)
