import time
import requests
import os

# Nhập thông tin cần thiết
AUTHORIZATION = input("(⁀ᗢ⁀)\nNHẬP AUTHORIZATION: ").strip()
TOKEN = input("NHẬP TOKEN: ").strip()
try:
    DELAY = int(input("NHẬP THỜI GIAN DELAY GIỮA CÁC JOB (GIÂY): ").strip())
except:
    DELAY = 10

# Headers mặc định
HEADERS = {
    "Authorization": AUTHORIZATION,
    "Content-Type": "application/json"
}

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print("=" * 40)
    print("         Tool Gop DGVIKAKA")
    print("           0785308626")
    print("        ad: Duong Vi")
    print("=" * 40)

def get_job():
    url = "https://gateway.golike.net/api/tasks/assignment/receive"
    data = {
        "access_token": TOKEN,
        "app_id": "tiktok",
        "type": "follow"
    }
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        return response.json()
    except Exception as e:
        print(f"[LỖI KẾT NỐI]: {e}")
        return None

def main():
    banner()
    while True:
        job = get_job()
        if not job:
            print("[!] KHÔNG NHẬN ĐƯỢC JOB. ĐỢI...")
            time.sleep(DELAY)
            continue

        if job.get("status_code") != 200:
            print(f"[!] LỖI: {job.get('message', 'Không xác định')}")
            time.sleep(DELAY)
            continue

        data = job.get("data", {})
        link = data.get("link")
        if not link:
            print("[!] KHÔNG CÓ LINK TRONG JOB")
            time.sleep(DELAY)
            continue

        print(f"[+] NHẬN JOB MỚI: {link}")
        print("[*] MỞ LINK TRONG GOLIKE - TỰ MỞ TIKTOK ĐỂ FOLLOW")
        os.system(f'am start -a android.intent.action.VIEW -d "{link}"')
        print(f"[...] CHỜ {DELAY} GIÂY TRƯỚC KHI NHẬN JOB TIẾP THEO")
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
