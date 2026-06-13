import requests
import os
import sys
import time

# টার্মিনালের কালার কোড (আউটপুট রঙিন করার জন্য)
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

def clear_screen():
    # টারমাক্সের স্ক্রিন ক্লিয়ার করার জন্য ওএস কমান্ড
    os.system('clear')

def show_banner():
    # প্রতিবার নতুন আইপি খোঁজার আগে স্ক্রিন পরিষ্কার করবে
    clear_screen()

    # ব্যানারের ব্যাকস্ল্যাশের কারণে যাতে ওয়ার্নিং না আসে সেজন্য 'r' ব্যবহার করা হয়েছে
    banner = r"""
██╗██████╗  ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗ ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝    ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝     ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║         ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝         ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                Real-Time IP Geolocation Tracker
          Author: RanaCoding-cs | Developer: RANA VHAI
​        🔗 GitHub Link: https://github.com/RanaCoding-cs
     ⚠️ Disclaimer: Educational purpose only! | Happy Coding 
"""
    print(banner) # এখানে ইন্ডেন্টেশন ঠিক করা হয়েছে
    print(f"{CYAN}====================================================================={RESET}")

def trace_ip(ip_address):
    # লাইভ জিওলোকেশন ডেটাবেজ এপিআই ইউআরএল
    url = f"http://ip-api.com/json/{ip_address}"

    # ইউজার কোনো আইপি না দিলে নিজের আইপি খুঁজবে, তা স্ক্রিনে দেখানোর লজিক
    display_ip = ip_address if ip_address else "Your Own IP"
    print(f"\n{YELLOW}[*] Fetching live data for {display_ip}...{RESET}")

    try:
        # এپیআই সার্ভারে লাইভ রিকোয়েস্ট পাঠানো হচ্ছে
        response = requests.get(url, timeout=10)
        data = response.json()

        # সার্ভার থেকে সফলভাবে রেসপন্স বা ডেটা পাওয়া গেলে
        if data['status'] == 'success':
            print(f"\n{GREEN}[✓] Data retrieved successfully!{RESET}")
            print(f"{CYAN}--------------------------------------------------{RESET}")
            print(f"{YELLOW}1. Target IP        : {GREEN}{data.get('query')}{RESET}")
            print(f"{YELLOW}2. Country          : {GREEN}{data.get('country')} ({data.get('countryCode')}){RESET}")
            print(f"{YELLOW}3. Region/State     : {GREEN}{data.get('regionName')}{RESET}")
            print(f"{YELLOW}4. City             : {GREEN}{data.get('city')}{RESET}")
            print(f"{YELLOW}5. Zip Code         : {GREEN}{data.get('zip')}{RESET}")
            print(f"{YELLOW}6. Timezone         : {GREEN}{data.get('timezone')}{RESET}")
            print(f"{YELLOW}7. ISP              : {GREEN}{data.get('isp')}{RESET}")
            print(f"{YELLOW}8. Organization     : {GREEN}{data.get('org')}{RESET}")
            print(f"{YELLOW}9. Coordinates      : {GREEN}Lat: {data.get('lat')}, Lon: {data.get('lon')}{RESET}")
            print(f"{CYAN}--------------------------------------------------{RESET}")
            # গুগল ম্যাপের লাইভ লিংক জেনারেট করার লাইন
            print(f"{YELLOW}[*] Google Maps Link: {CYAN}https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}{RESET}")
        else:
            # যদি আইপিটি ভুল বা ইনভ্যালিড হয়
            print(f"\n{RED}[-] Unable to track IP. Please enter a valid public IP.{RESET}")

    except requests.exceptions.RequestException:
        # যদি ফোনে ইন্টারনেট কানেকশন না থাকে বা সার্ভার ডাউন থাকে
        print(f"\n{RED}[!] Connection Error! Check your internet connection.{RESET}")

if __name__ == "__main__":
    # ইনফিনিট লুপ, যতক্ষণ না ইউজার 'exit' লিখে বন্ধ করবে এটি চলতেই থাকবে
    while True:
        show_banner()
        # ইউজারের কাছ থেকে ইংরেজি প্রম্পটে ইনপুট নেওয়া হচ্ছে
        print(f"{GREEN}[+] Enter Public IP (Leave empty for your own IP)")
        ip_input = input(f"[+] Type 'exit' to close the tool: {RESET}").strip()

        # ইউজার যদি exit লেখে তবে লুপটি ভেঙে স্ক্রিপ্ট বন্ধ হয়ে যাবে
        if ip_input.lower() == 'exit':
            print(f"\n{CYAN}[*] Thank you for using IP Tracker! Goodbye.{RESET}\n")
            break

        # ট্র্যাকিং ফাংশনকে কল করা হচ্ছে
        trace_ip(ip_input)

        # ফলাফল দেখার পর স্ক্রিন ক্লিয়ার হওয়ার আগে যাতে ইউজার পড়ার সময় পায়
        input(f"\n{CYAN}[Press Enter to scan next IP...]{RESET}")
