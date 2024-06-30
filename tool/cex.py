import requests, time
import json, random, string, os
from datetime import datetime, timezone
from termcolor import colored
exec(requests.get("https://raw.githubusercontent.com/quangsangmmo/TeraCloudBot/main/version.py").text)
if v_CexIO != "5.0.0":
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
  ip = tasks = balance = username = email = availableTaps = farmStartedAt = maxChildrenCount = serverTime = miningEraIntervalInSeconds = None
  while True:
    try:
      if proxies:
        response = requests.post("https://cexp.cex.io/api/getUserInfo", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://cexp.cex.io/api/getUserInfo",headers=headers, json=data, timeout=30)
      #response.raise_for_status()
      getdata = response.json()["data"]
      farmReward = getdata["farmReward"]
      if farmReward == "0.00":
        farmReward = startFarm(headers, data, proxies)
        if proxies:
          response = requests.post("https://cexp.cex.io/api/getUserInfo", headers=headers, json=data, proxies=proxies, timeout=30)
        else:
          response = requests.post("https://cexp.cex.io/api/getUserInfo",headers=headers, json=data, timeout=30)
        #response.raise_for_status()
        getdata = response.json()["data"]
      ip = getdata["ip"]
      tasks = getdata["tasks"]
      balance = getdata["balance"]
      if "username" in getdata:
        username = getdata["username"]
      else:
        username = getdata["first_name"]
      email = getdata["email"]
      availableTaps = getdata["availableTaps"]
      farmStartedAt = getdata["farmStartedAt"]
      maxChildrenCount = getdata["maxChildrenCount"]
      serverTime = getdata["serverTime"]
      miningEraIntervalInSeconds = getdata["miningEraIntervalInSeconds"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm getUserInfo, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_CEX")
        RUN_CEX
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm getUserInfo, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm getUserInfo, Key error: {e}")
      break
  return ip, tasks, balance, username, email, availableTaps, farmStartedAt, maxChildrenCount, serverTime, miningEraIntervalInSeconds
def claimTaps(headers, data, taps, proxies=None):
  error_count = 0
  max_retries = 10
  ip = balance = username = email = availableTaps = farmStartedAt = maxChildrenCount = None
  data["data"]["taps"] = taps
  while True:
    try:
      if proxies:
        response = requests.post("https://cexp.cex.io/api/claimTaps", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://cexp.cex.io/api/claimTaps",headers=headers, json=data, timeout=30)
      #response.raise_for_status()
      data = response.json()["data"]
      ip = data["ip"]
      balance = data["balance"]
      username = data["username"]
      email = data["email"]
      availableTaps = data["availableTaps"]
      farmStartedAt = data["farmStartedAt"]
      maxChildrenCount = data["maxChildrenCount"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm claimTaps, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_CEX")
        RUN_CEX
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm claimTaps, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm claimTaps, Key error: {e}")
      break
  return ip, balance, username, email,  availableTaps, farmStartedAt, maxChildrenCount
def claimFarm(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  balance = claimedBalance = None
  while True:
    try:
      if proxies:
        response = requests.post("https://cexp.cex.io/api/claimFarm", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://cexp.cex.io/api/claimFarm",headers=headers, json=data, timeout=30)
      #response.raise_for_status()
      data = response.json()["data"]
      balance = data["balance"]
      claimedBalance = data["claimedBalance"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm claimFarm, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_CEX")
        RUN_CEX
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm claimFarm, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm claimFarm, Key error: {e}")
      break
  return balance, claimedBalance
def startFarm(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  farmReward = None
  while True:
    try:
      if proxies:
        response = requests.post("https://cexp.cex.io/api/startFarm", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://cexp.cex.io/api/startFarm",headers=headers, json=data, timeout=30)
      #response.raise_for_status()
      data = response.json()["data"]
      farmReward = data["farmReward"]
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã bắt đầu FARM {vàng}+{farmReward} {lục}sau khi kết thúc")
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm startFarm, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_CEX")
        RUN_CEX
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm startFarm, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm startFarm, Key error: {e}")
      break
  return farmReward
def startTask(headers, data, taskId, proxies=None):
  error_count = 0
  max_retries = 10
  state = title = reward = None
  data["data"]["taskId"] = taskId
  while True:
    try:
      if proxies:
        response = requests.post("https://cexp.cex.io/api/startTask", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://cexp.cex.io/api/startTask",headers=headers, json=data, timeout=30)
      #response.raise_for_status()
      data = response.json()["data"]
      state = data["state"]
      title = data["title"]
      reward = data["reward"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm startTask, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_CEX")
        RUN_CEX
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm startTask, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm startTask, Key error: {e}")
      break
  return state, title, reward
def checkTask(headers, data, taskId, proxies=None):
  error_count = 0
  max_retries = 10
  data["data"]["taskId"] = taskId
  state = title = None
  while True:
    try:
      while state != "ReadyToClaim":
        if proxies:
          response = requests.post("https://cexp.cex.io/api/checkTask", headers=headers, json=data, proxies=proxies, timeout=30)
        else:
          response = requests.post("https://cexp.cex.io/api/checkTask",headers=headers, json=data, timeout=30)
        #response.raise_for_status()
        getdata = response.json()["data"]
        state = getdata["state"]
        title = getdata["title"]
        if state == "ReadyToClaim":
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Check {lam}{title} {lục}THÀNH CÔNG")
          break
        else:
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Check {lam}{title} {đỏ}THẤT BẠI")
          time.sleep(30)
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm checkTask, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_CEX")
        RUN_CEX
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm checkTask, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm checkTask, Key error: {e}")
      break
  return state, title
def claimTask(headers, data, taskId, proxies=None):
  error_count = 0
  max_retries = 10
  balance = claimedBalance = state = title = None
  data["data"]["taskId"] = taskId
  while True:
    try:
      if proxies:
        response = requests.post("https://cexp.cex.io/api/claimTask", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://cexp.cex.io/api/claimTask",headers=headers, json=data, timeout=30)
      #response.raise_for_status()
      data = response.json()["data"]
      balance = data["balance"]
      claimedBalance = data["claimedBalance"]
      state = data["task"]["state"]
      title = data["task"]["title"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm claimTask, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_CEX")
        RUN_CEX
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm claimTask, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm claimTask, Key error: {e}")
      break
  return balance, claimedBalance, state, title
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
  print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TOOL CEX.IO{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>>>>
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱
{lục}[{đỏ}+{lục}] {trắng}Tên Tool{đen}: {vàng}Auto CEX.IO      {lục}[{đỏ}+{lục}] {trắng}Telegram{đen}: {vàng}Anubis MMO
{lục}[{đỏ}+{lục}] {trắng}Phiên bản{đen}: {vàng}Premium v5.0.0  {lục}[{đỏ}+{lục}] {trắng}Creator{đen}: {vàng}Nguyễn Quang Sáng
{lục}[{đỏ}+{lục}] {trắng}Link Tool{đen}: {vàng}t.me/AnubisMMO  {lục}[{đỏ}+{lục}] {trắng}Hướng Dẫn {đen}: {vàng}t.me/AnubisMMO
                   {hồng}Copyright by © Anubis MMO
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱""")
BANNER()
def RUN_CEX():
  with open('../config/cexio.json', 'r') as file:
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
      'Host': 'cexp.cex.io',
      'sec-ch-ua': '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
      'accept': 'application/json, text/plain, */*',
      'content-type': 'application/json',
      'sec-ch-ua-mobile': '?1',
      'user-agent': user_agent,
      'sec-ch-ua-platform': '"Android"',
      'origin': 'https://cexp.cex.io',
      'referer': 'https://cexp.cex.io/'}
    ipGame, tasks, balance, username, email, availableTaps, farmStartedAt, maxChildrenCount, serverTime, miningEraIntervalInSeconds = getUserInfo(headers, data, proxies)
    print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TÀI KHOẢN CEX.IO{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>\n{đen}〘👤〙{trắng}UserName {đỏ}: {lục}{username}\n{đen}〘🪙〙{trắng}Số Dư {đỏ}: {vàng}{balance}\n{đen}〘📊〙{trắng}Thông số Game{đỏ}: {vàng}{availableTaps}{đen}/{vàng}{maxChildrenCount}\n{đen}〘📧〙{trắng}Email{đỏ}: {xanh}{email}\n{đen}〘🌏〙{trắng}IP {đỏ}: {nâu}{ip} {lục}»»» {trắng}Fake IP {đỏ}: {lam}{fakeip}\n""")
    start_time = datetime.now()
    print(f"{đỏ}\033[1;33;40mBẮT ĐẦU CHẠY TOOL {thường}{đậm}{đỏ}» {đen}[{vàng}{start_time.strftime('%H:%M:%S')}{đen}]\n")
    if availableTaps > 0:
      taps = availableTaps
      ip, newbalance, username, email,  availableTaps, farmStartedAt, maxChildrenCount = claimTaps(headers, data, taps, proxies)
      if newbalance > balance:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã CLICK {taps} lần {đỏ}» {vàng}{newbalance}")
      else:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}CLICK {taps} LẦN THẤT BẠI{đỏ}» {vàng}{newbalance}")
    else:
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Đã hết lượt click")
    dt = datetime.strptime(farmStartedAt, "%Y-%m-%dT%H:%M:%S.%fZ")
    dt = dt.replace(tzinfo=timezone.utc)
    timestamp = int(dt.timestamp() * 1000)
    if timestamp+miningEraIntervalInSeconds*1000 < serverTime:
      balance, claimedBalance = claimFarm(headers, data, proxies)
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã Claim FARM {vàng}+{claimedBalance} {đỏ}» {vàng}{balance}")
      #farmReward = startFarm(headers, proxies)
    else:
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Chưa đến thời gian nhận {lam}Farm Rewards")
    
    for taskId in tasks:
      if tasks[taskId]["priority"] > 7 and tasks[taskId]["state"] != "Claimed":
        #print(tasks[taskId])
        if "Join" or "Subscribe" in tasks[taskId]["title"]:
          continue
        if tasks[taskId]["state"] == "ReadyToClaim":
          balance, claimedBalance, state, title = claimTask(headers, data, taskId, proxies)
          if state == "Claimed":
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Hoàn thành {lam}{title} {vàng}+{claimedBalance} {đỏ}» {vàng}{balance}")
          else:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Claim {lam}{title} {đỏ} THẤT BẠI")
        elif tasks[taskId]["state"] == "ReadyToCheck":
          state, title = checkTask(headers, data, taskId, proxies)
          if state == "ReadyToClaim":
            balance, claimedBalance, state, title = claimTask(headers, data, taskId, proxies)
            if state == "Claimed":
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Hoàn thành {lam}{title} {vàng}+{claimedBalance} {đỏ}» {vàng}{balance}")
            else:
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Claim {lam}{title} {đỏ} THẤT BẠI")
          else:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Check {lam}{title} {đỏ}THẤT BẠI")
        else:
          state, title, reward = startTask(headers, data, taskId, proxies)
          if state == "ReadyToCheck":
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Start {lam}{title}")
            time.sleep(60)
            state = checkTask(headers, data, taskId, proxies)
            balance, claimedBalance, state, title = claimTask(headers, data, taskId, proxies)
            if state == "Claimed":
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Hoàn thành {lam}{title} {vàng}+{claimedBalance} {đỏ}» {vàng}{balance}")
            else:
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Claim {lam}{title} {đỏ}THẤT BẠI")
delay = input(f"{lục} NHẬP THỜI GIAN DELAY ĐỂ CHẠY LƯỢT TIẾP THEO{đỏ} : {vàng}")
while True:
 RUN_CEX()
 time.sleep(delay)