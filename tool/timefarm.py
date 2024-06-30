import requests, time
import json, random, string, os
from datetime import datetime, timezone
from termcolor import colored
exec(requests.get("https://raw.githubusercontent.com/quangsangmmo/TeraCloudBot/main/version.py").text)
if v_Bunny != "5.0.0":
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


def getUserInfo(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://tg-bot-tap.laborx.io/api/v1/auth/validate-init", headers=headers, data=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://tg-bot-tap.laborx.io/api/v1/auth/validate-init",headers=headers, data=data)
      #response.raise_for_status()
      getdata = response.json()
      token = getdata["token"]
      #username = getdata["userInfo"]["userName"]
      balance = getdata["balanceInfo"]["balance"]
      level = getdata["info"]["level"]
      #ip = getdata["ip"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm getUserInfo, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm getUserInfo, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
  return token, balance, level
def farmInfo(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://tg-bot-tap.laborx.io/api/v1/farming/info", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://tg-bot-tap.laborx.io/api/v1/farming/info",headers=headers, timeout=30)
      #response.raise_for_status()
      getdata = response.json()
      balance = getdata["balance"]
      timeStartFarm = getdata["activeFarmingStartedAt"]
      timeFarm = getdata["farmingDurationInSec"]
      rewardFarm = getdata["farmingReward"]
      if timeStartFarm == None:
        balance, timeStartFarm, timeFarm, rewardFarm = startFarm(headers, proxies)
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm farmInfo, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm farmInfo, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
  return balance, timeStartFarm, timeFarm, rewardFarm
def claimFarm(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://tg-bot-tap.laborx.io/api/v1/farming/finish", headers=headers, json={}, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://tg-bot-tap.laborx.io/api/v1/farming/finish",headers=headers, json={})
      response.raise_for_status()
      getdata = response.json()
      balance = getdata["balance"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm claimFarm, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm claimFarm, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
  return balance
def startFarm(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://tg-bot-tap.laborx.io/api/v1/farming/start", headers=headers, json={}, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://tg-bot-tap.laborx.io/api/v1/farming/start",headers=headers, json={})
      response.raise_for_status()
      getdata = response.json()
      balance = getdata["balance"]
      timeStartFarm = getdata["activeFarmingStartedAt"]
      timeFarm = getdata["farmingDurationInSec"]
      rewardFarm = getdata["farmingReward"]
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã bắt đầu FARM {vàng}+{rewardFarm} {lục}sau khi kết thúc")
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm startFarm, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm startFarm, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
  return balance, timeStartFarm, timeFarm, rewardFarm
def tasksInfo(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://tg-bot-tap.laborx.io/api/v1/tasks", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://tg-bot-tap.laborx.io/api/v1/tasks",headers=headers, timeout=30)
      #response.raise_for_status()
      tasksList = response.json()
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm tasksInfo, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm tasksInfo, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
  return tasksList
def startTask(headers, id_task, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post(f"https://tg-bot-tap.laborx.io/api/v1/tasks/{id_task}/submissions", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post(f"https://tg-bot-tap.laborx.io/api/v1/tasks/{id_task}/submissions",headers=headers, timeout=30)
      #response.raise_for_status()
      status = response.status_code
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm startTask, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm startTask, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
  return status
def claimTask(headers, id_task, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post(f"https://tg-bot-tap.laborx.io/api/v1/tasks/{id_task}/claims", headers=headers, json={}, proxies=proxies, timeout=30)
      else:
        response = requests.post(f"https://tg-bot-tap.laborx.io/api/v1/tasks/{id_task}/claims",headers=headers, json={})
      #response.raise_for_status()
      status = response.status_code
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(response.status_code)
      print(f"{đỏ}Hàm claimTask, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm claimTask, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
  return status
def getBalance(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get(f"https://tg-bot-tap.laborx.io/api/v1/balance", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get(f"https://tg-bot-tap.laborx.io/api/v1/balance",headers=headers, timeout=30)
      #response.raise_for_status()
      balance = response.json()["balance"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm getBalance, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm getBalance, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_TIMEFARM()")
        RUN_TIMEFARM()
        break
      COUNTDOWN(10)
  return balance

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
  print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TOOL TIMEFARM{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>>>
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱
{lục}[{đỏ}+{lục}] {trắng}Tên Tool{đen}: {vàng}Auto TIMEFARM    {lục}[{đỏ}+{lục}] {trắng}Telegram{đen}: {vàng}Anubis MMO
{lục}[{đỏ}+{lục}] {trắng}Phiên bản{đen}: {vàng}Premium v5.0.0  {lục}[{đỏ}+{lục}] {trắng}Creator{đen}: {vàng}Nguyễn Quang Sáng
{lục}[{đỏ}+{lục}] {trắng}Link Tool{đen}: {vàng}t.me/AnubisMMO  {lục}[{đỏ}+{lục}] {trắng}Hướng Dẫn {đen}: {vàng}t.me/AnubisMMO
                   {hồng}Copyright by © Anubis MMO
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱""")
BANNER()
def RUN_TIMEFARM():
  with open('../config/timefarm.json', 'r') as file:
    config_data = json.load(file)
  users = config_data
  if len(users) > 10:
    print("Bạn chỉ được phép thêm tối đa 10 tài khoản để chạy tool")
    exit()
  for user in users:
    account = user["STT_ACCOUNT"]
    data = user["DATA"]
    if data == "":
      continue
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
    ip = fakeip = "None"
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
      "Host": "tg-bot-tap.laborx.io",
      #"Content-Length": "351",
      "Sec-CH-UA": '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
      "Sec-CH-UA-Platform": "Android",
      "Sec-CH-UA-Mobile": "?1",
      "User-Agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36",
      "Content-Type": "text/plain;charset=UTF-8",
      "Accept": "*/*",
      "Origin": "https://tg-tap-miniapp.laborx.io",
      "X-Requested-With": "mark.via.gq",
      "Sec-Fetch-Site": "same-site",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://tg-tap-miniapp.laborx.io/",
      "Accept-Encoding": "gzip, deflate, br, zstd",
      "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "Priority": "u=1, i"}
    token, balance, level = getUserInfo(headers, data, proxies)
    headers["Authorization"] = f"Bearer {token}"
    print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TÀI KHOẢN TIMEFARM{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>\n{đen}〘🪙〙{trắng}Số Dư {đỏ}: {vàng}{balance:,}\n{đen}〘📊〙{trắng}Level {đỏ}: {lam}{level}\n{đen}〘🌏〙{trắng}IP {đỏ}: {nâu}{ip} {lục}»»» {trắng}Fake IP {đỏ}: {lam}{fakeip}\n""")
    start_time = datetime.now()
    print(f"{đỏ}\033[1;33;40mBẮT ĐẦU CHẠY TOOL {thường}{đậm}{đỏ}» {đen}[{vàng}{start_time.strftime('%H:%M:%S')}{đen}]\n")
    tasks = tasksInfo(headers, proxies)
    for task in tasks:
      id_task = task["id"]
      title_task = task["title"]
      reward_task = task["reward"]
      if "Subscribe" not in title_task:
        if "submission" in task:
          if task["submission"]["status"] == "CLAIMED":
            continue
          if task["submission"]["status"] == "COMPLETED":
            status = claimTask(headers, id_task, proxies)
            if status == 200:
              balance = getBalance(headers, proxies)
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Hoàn thành {lam}{title_task} {vàng}+{reward_task} {đen}» {vàng}{balance:,}")
            else:
              print(status)
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{đỏ} Hoàn thành {lam}{title_task} {đỏ}THẤT BẠI")
          else:
            print(task)
        else:
          status = startTask(headers, id_task, proxies)
          if status == 200:
            status = claimTask(headers, id_task, proxies)
            if status == 200:
              balance = getBalance(headers, proxies)
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Hoàn thành {lam}{title_task} {vàng}+{reward_task} {đen}» {vàng}{balance:,}")
            else:
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{đỏ} Hoàn thành {lam}{title_task} {đỏ}THẤT BẠI")
          else:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{đỏ} Làm NV {lam}{title_task} {đỏ}THẤT BẠI")
    balance, timeStartFarm, timeFarm, rewardFarm = farmInfo(headers, proxies)
    timeStart = datetime.strptime(timeStartFarm, "%Y-%m-%dT%H:%M:%S.%fZ")
    timeStart = timeStart.replace(tzinfo=timezone.utc)
    timestamp = int(timeStart.timestamp() * 1000)
    if timestamp+timeFarm*1000 < int(time.time()*1000):
      balance = claimFarm(headers, proxies)
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã Claim FARM {vàng}+{rewardFarm} {đỏ}» {vàng}{balance:,}")
      balance, timeStartFarm, timeFarm, rewardFarm = startFarm(headers, proxies)
    else:
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Chưa đến thời gian nhận {lam}Farm Rewards")
    print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}HẾT NHIỆM VỤ VÀ LƯỢT CLAIM {đỏ}» {vàng}ĐỔI TÀI KHOẢN")
delay = input(f"{lục} NHẬP THỜI GIAN DELAY ĐỂ CHẠY LƯỢT TIẾP THEO{đỏ} : {vàng}")
while True:
 RUN_TIMEFARM()
 time.sleep(delay)