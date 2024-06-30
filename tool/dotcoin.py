import requests, time
import json, random, string, os
from datetime import datetime, timezone
from termcolor import colored
exec(requests.get("https://raw.githubusercontent.com/quangsangmmo/TeraCloudBot/main/version.py").text)
if v_HamsterKombat != "5.0.0":
  print("Vui lòng cập nhật phiên bản mới nhất của tool")
  exit()
#KIÊỦ CHỮ
thường = "\033[0m"
đậm = "\033[1m"
mờ = "\033[2m"
nghiêng = "\033[3m"
gạch = "\033[4m"
#MÀU CHỮ
đỏ = "\033[91m"
vàng = "\033[93m"
lục = "\033[92m"
xanh = "\033[94m"
hồng = "\033[95m"
lam = "\033[96m"
trắng = "\033[97m"
đen = "\033[30m"
nâu = "\033[33m"
xám = "\033[90m"
#MÀU BACKGROUND 
đenBG = "\033[40m"
đỏBG = "\033[41m"
lụcBG = "\033[42m"
vàngBG = "\033[43m"
xanhBG = "\033[44m"
tímBG = "\033[45m"
lamBG = "\033[46m"
trắngBG = "\033[47m"
version = "2.0.4"
def COUNTDOWN(seconds):
  for i in range(seconds, 0, -1):
    print(f"Tiếp tục sau {i} giây", end="\r")
    time.sleep(1)
  print()
def iso_to_timestamp(iso_datetime_str):
  dt = datetime.strptime(iso_datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
  timestamp = dt.timestamp()*1000
  timestamp_utc = time.time()*1000
  return timestamp, timestamp_utc

def PROFILE(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/get_user_info", headers=headers, json={}, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/get_user_info", headers=headers, json={}, timeout=30)
      response.raise_for_status()
      getdata = response.json()
      username = getdata["first_name"]
      level = getdata["level"]
      energy = getdata["daily_attempts"]
      energyMax = getdata["limit_attempts"]
      balance = getdata["balance"]
      dame = getdata["multiple_clicks"]
      clan = getdata["group"]
      try_luck = getdata["gamex2_times"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm PROFILE, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_DOTCOIN()")
        RUN_DOTCOIN()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm PROFILE, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_DOTCOIN()")
        RUN_DOTCOIN()
        break
      COUNTDOWN(10)

  return username, balance, energy, clan, dame, energyMax, level, try_luck
def CLICK(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  headers["Content-Length"] = str(len(str(data).replace(" ","")))
  while True:
    try:
      if proxies:
        response = requests.post("https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/save_coins", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/save_coins", headers=headers, json=data, timeout=30)
      response.raise_for_status()
      success = response.json()["success"]
      #print(response.text)
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm CLICK, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_DOTCOIN()")
        RUN_DOTCOIN()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm CLICK, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_DOTCOIN()")
        RUN_DOTCOIN()
        break
      COUNTDOWN(10)

  return success
def LEVEL_UP(headers, data, typeUpgrade, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post(f"https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/{typeUpgrade}", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post(f"https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/{typeUpgrade}", headers=headers, json=data, timeout=30)
      response.raise_for_status()
      success = response.json()["success"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm LEVEL_UP, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_DOTCOIN()")
        RUN_DOTCOIN()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm LEVEL_UP, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_DOTCOIN()")
        RUN_DOTCOIN()
        break
      COUNTDOWN(10)
  return success
def TRY_LUCK(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post(f"https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/try_your_luck", headers=headers, json={"coins":150000}, proxies=proxies, timeout=30)
      else:
        response = requests.post(f"https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/try_your_luck", headers=headers, json={"coins":150000}, timeout=30)
      response.raise_for_status()
      #print(response.json())
      success = response.json()["success"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm TRY_LUCK, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_DOTCOIN()")
        RUN_DOTCOIN()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm TRY_LUCK, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_DOTCOIN()")
        RUN_DOTCOIN()
        break
      COUNTDOWN(10)
  return success

def BANNER():
  #os.system("clear")
  banner = f"""    ___                __    _         ______            __
   /   |  ____  __  __/ /_  (_)____   /_  __/___  ____  / /
  / /| | / __ \/ / / / __ \/ / ___/    / / / __ \/ __ \/ / 
 / ___ |/ / / / /_/ / /_/ / (__  )    / / / /_/ / /_/ / /  
/_/  |_/_/ /_/\__,_/_.___/_/____/    /_/  \____/\____/_/   

"""
  colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
  gradient_step = 1 / len(banner)
  for i, char in enumerate(banner):
    color_index = int(i * gradient_step * len(colors))
    color = colors[color_index]
    print(colored(char, color), end='')
  print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TOOL DOTCOIN{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>>
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱
{lục}[{đỏ}+{lục}] {trắng}Tên Tool{đen}: {vàng}Auto DOTCOIN     {lục}[{đỏ}+{lục}] {trắng}Telegram{đen}: {vàng}Anubis MMO
{lục}[{đỏ}+{lục}] {trắng}Phiên bản{đen}: {vàng}Premium v5.0.0  {lục}[{đỏ}+{lục}] {trắng}Creator{đen}: {vàng}Nguyễn Quang Sáng
{lục}[{đỏ}+{lục}] {trắng}Link Tool{đen}: {vàng}t.me/AnubisMMO  {lục}[{đỏ}+{lục}] {trắng}Hướng Dẫn {đen}: {vàng}t.me/AnubisMMO
                   {hồng}Copyright by © Anubis MMO
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱""")
BANNER()
def RUN_DOTCOIN():
  with open('../config/dotcoin.json', 'r') as file:
    config_data = json.load(file)
  users = config_data
  if len(users) > 10:
    print("Bạn chỉ được phép thêm tối đa 10 tài khoản để chạy tool")
    exit()
  for user in users:
    account = user["STT_ACCOUNT"]
    data_dotcoin = user["DATA"]
    if data_dotcoin == "":
      continue
    authorization = data_dotcoin[0]
    user_id = data_dotcoin[1]
    with open('../config/setting.json', 'r') as file:
      config_acc = json.load(file)[account]
    proxy_list = config_acc["proxy"]
    user_agent = config_acc["user-agent"]
    if proxy_list != "":
      proxy_list = proxy_list.split(":")
      proxy = f"http://{proxy_list[2]}:{proxy_list[3]}@{proxy_list[0]}:{proxy_list[1]}"
      proxies = {
      'http': proxy,
      'https': proxy,}
    else:
      proxies = ""
    def getIP(proxies):
      ip = fakeip = "None"
      url_ip = ["https://api.ipify.org","https://ipinfo.io/ip","https://ipv4.icanhazip.com/","https://api.ipgeolocation.io/getip"]
      while ip == fakeip == "None" or ip == fakeip == " " or fakeip == ip == "":
        try:
          urlGetIP = random.choice(url_ip)
          ip = requests.get(urlGetIP, timeout=30)
          fakeip = requests.get(urlGetIP,proxies=proxies, timeout=30)
        except:
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ} Lấy ip thất bại...\n")
          ip = fakeip = "None"
      try:
        ip = ip.json()["ip"]
        fakeip = fakeip.json()["ip"]
      except:
        ip = ip.text
        fakeip = fakeip.text
      return ip, fakeip
    ip, fakeip = getIP(proxies)

    headers = {
      "Content-Length": "2",
      "X-Client-Info": "postgrest-js/1.9.2",
      "Sec-CH-UA": '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
      "Sec-CH-UA-Mobile": "?1",
      "Authorization": authorization,
      "User-Agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36",
      "Content-Type": "application/json",
      "Content-Profile": "public",
      "Apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8",
      "X-Telegram-User-Id": user_id,
      "Sec-CH-UA-Platform": '"Android"',
      "Accept": "*/*",
      "Origin": "https://dot.dapplab.xyz",
      "X-Requested-With": "mark.via.gq",
      "Sec-Fetch-Site": "cross-site",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://dot.dapplab.xyz/",
      "Accept-Encoding": "gzip, deflate, br, zstd",
      "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "Priority": "u=1, i"}
    
    username, balance, energy, clan, dame, energyMax, level, try_luck = PROFILE(headers, proxies)
    print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TÀI KHOẢN DOTCOIN{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>\n{đen}〘👤〙{trắng}UserName {đỏ}: {lục}{username}\n{đen}〘🪙〙{trắng}Số Dư {đỏ}: {vàng}{balance:,}\n{đen}〘📊〙{trắng}Thông số Game{đỏ}: {lục}+{dame}{đen}/{lục}click {vàng}{energy}{đỏ}/{vàng}{energyMax}⚡\n{đen}〘📧〙{trắng}Thông tin Clan{đỏ}: {xanh}{clan}\n{đen}〘🌏〙{trắng}IP {đỏ}: {nâu}{ip} {lục}»»» {trắng}Fake IP {đỏ}: {lam}{fakeip}\n""")
    start_time = datetime.now()
    print(f"{đỏ}\033[1;33;40mBẮT ĐẦU CHẠY TOOL {thường}{đậm}{đỏ}» {đen}[{vàng}{start_time.strftime('%H:%M:%S')}{đen}]\n")
    if try_luck > 0:
      success = TRY_LUCK(headers, proxies)
      if success == True:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Đã nhận được {150000:,} từ {vàng}Dotcoin Game x2\n")
    def UPGRADE(balance, dame, energy, energyMax):
      success = LEVEL_UP(headers, {"lvl":dame}, "add_multitap", proxies)
      if success == True:
        username, newbalance, energy, clan, dame, energyMax, level = PROFILE(headers, proxies)
        price = balance - newbalance
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Đã nâng cấp {hồng}Multitap {trắng}({lam}{dame-1}{trắng}) {đỏ}-{price} {đen}» {vàng}{newbalance:,}\n")
        balance = newbalance
      success = LEVEL_UP(headers, {"lvl":energyMax-9}, "add_attempts", proxies)
      if success == True:
        username, newbalance, energy, clan, dame, energyMax, level = PROFILE(headers, proxies)
        price = balance - newbalance
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Đã nâng cấp {hồng}Daily Attempts {trắng}({lam}{energyMax-10}{trắng}) {đỏ}-{price} {đen}» {vàng}{newbalance:,}\n")
        balance = newbalance
      return balance, dame, energy, energyMax
    #balance, dame, energy, energyMax = UPGRADE(balance, dame, energy, energyMax)
    while True:
      if energy > 0:
        for i in range(0,energy):
          #print()
          success = CLICK(headers, {"coins":20000}, proxies)
          if success == True:
            username, newbalance, energy, clan, dame, energyMax, level, try_luck = PROFILE(headers, proxies)
            collectAmount = newbalance - balance
            balance = newbalance
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đen}╔═{đỏ}[{vàng}{now_time}{đỏ}] {trắng}Đã CLICK {vàng}+{collectAmount} {đỏ}• {lam}{energy} energy {đỏ}»", end=" ")
            print(f"{vàng}{newbalance:,}\n{đen}╚⫸{hồng}Tải tool miễn phí tại Channel Telegram{đỏ}: {lục}@AnubisMMO\n")
            #balance, dame, energy, energyMax = UPGRADE(balance, dame, energy, energyMax)
          else:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ} Click thất bại!")
      else:
        print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}HẾT LƯỢT CLICK, HẾT BOOST {đỏ}» {vàng}ĐỔI TÀI KHOẢN")
        break
delay = input(f"{lục} NHẬP THỜI GIAN DELAY ĐỂ CHẠY LƯỢT TIẾP THEO{đỏ} : {vàng}")
while True:
 RUN_DOTCOIN()
 time.sleep(delay)