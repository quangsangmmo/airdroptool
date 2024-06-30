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
def PROFILE(headers, proxies=None):
  error_count = 0
  max_retries = 10
  headers.pop("content-type",None)
  while True:
    try:
      if proxies:
        response = requests.get("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/user/profile", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/user/profile",headers=headers, timeout=30)
      #response.raise_for_status()
      getdata = response.json()
      username = getdata["username"]
      dame = getdata["energyPerTap"]
      energyLeft = getdata["energyLeft"]
      energyMax = getdata["energyMax"]
      energyPerSecond = getdata["energyPerSecond"]
      balance = getdata["score"]
      isTurboAvailable = getdata["isTurboAvailable"]
      nameSquad = getdata["squad"]["name"]
      members = getdata["squad"]["totalMembers"]
      scoreSquad = getdata["squad"]["totalEarnedScore"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(response.text)
      print(f"Hàm PROFILE, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_WORMFARE()")
        RUN_WORMFARE()
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm PROFILE, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm PROFILE, Key error: {e}")
      break
  return username, dame, energyLeft, energyMax, energyPerSecond, balance, nameSquad, members, scoreSquad, isTurboAvailable
def QUEST(headers, proxies=None):
  error_count = 0
  max_retries = 10
  headers.pop("content-type",None)
  while True:
    try:
      if proxies:
        response = requests.get("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest",headers=headers, timeout=30)
      #response.raise_for_status()
      tasks = response.json()
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(response.text)
      print(f"Hàm PROFILE, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_WORMFARE()")
        RUN_WORMFARE()
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm PROFILE, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm PROFILE, Key error: {e}")
      break
  return tasks
def CLICK(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  headers["content-type"] = "application/json"
  while True:
    try:
      if proxies:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/save-clicks", headers=headers, timeout=30, json=data, proxies=proxies)
      else:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/save-clicks", headers=headers, timeout=30, json=data)
      #response.raise_for_status()
      getdata = response.json()
      energyLeft = getdata["energyLeft"]
      balance = getdata["score"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      #print(response.text)
      print(f"Hàm CLICK, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_WORMFARE()")
        RUN_WORMFARE()
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm CLICK, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm CLICK, Key error: {e}")
      break
  return energyLeft, balance
def CHECK_QUEST(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  headers["content-type"] = "application/json"
  while True:
    try:
      if proxies:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest/check-completion", headers=headers, timeout=30, json=data, proxies=proxies)
      else:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest/check-completion", headers=headers, timeout=30, json=data)
      #response.raise_for_status()
      getdata = response.json()
      success = getdata["success"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(response.text)
      print(f"Hàm CHECK_QUEST, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_WORMFARE()")
        RUN_WORMFARE()
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm CHECK_QUEST, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm CHECK_QUEST, Key error: {e}")
      break
  return success
def CLAIM_QUEST(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  headers["content-type"] = "application/json"
  while True:
    try:
      if proxies:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest/claim-reward", headers=headers, timeout=30, json=data, proxies=proxies)
      else:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest/claim-reward", headers=headers, timeout=30, json=data)
      #response.raise_for_status()
      getdata = response.json()
      success = getdata["success"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(response.text)
      print(f"Hàm CHECK_QUEST, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_WORMFARE()")
        RUN_WORMFARE()
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm CHECK_QUEST, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm CHECK_QUEST, Key error: {e}")
      break
  return success
def SHOP(headers, proxies=None):
  error_count = 0
  max_retries = 10
  headers.pop("content-type",None)
  while True:
    try:
      if proxies:
        response = requests.get("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/shop", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/shop",headers=headers, timeout=30)
      #response.raise_for_status()
      getdata = response.json()
      countFullEnergy = getdata["dailyBoosts"][0]["availableCount"]
      countTurbo = getdata["dailyBoosts"][1]["availableCount"]
      RecoveryConfig = getdata["availableBoost"][1]
      TapConfig = getdata["availableBoost"][2]
      MaxEnergyConfig = getdata["availableBoost"][0]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(response.text)
      print(f"Hàm SHOP, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_WORMFARE()")
        RUN_WORMFARE()
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm SHOP, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm SHOP, Key error: {e}")
      break
  return countFullEnergy, countTurbo, RecoveryConfig, TapConfig, MaxEnergyConfig
def BUY_BOOST(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  headers["content-type"] = "application/json"
  while True:
    try:
      if proxies:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/buy-boost", headers=headers, timeout=30, json=data, proxies=proxies)
      else:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/buy-boost", headers=headers, timeout=30, json=data)
      #response.raise_for_status()
      getdata = response.json()
      balance = getdata["score"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(response.text)
      print(f"Hàm BUY_BOOST, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_WORMFARE()")
        RUN_WORMFARE()
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm BUY_BOOST, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm BUY_BOOST, Key error: {e}")
      break
  return balance
def ACTIVE_BOOST(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  headers["content-type"] = "application/json"
  while True:
    try:
      if proxies:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/activate-daily-boost", headers=headers, timeout=30, json=data, proxies=proxies)
      else:
        response = requests.post("https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/activate-daily-boost", headers=headers, timeout=30, json=data)
      #response.raise_for_status()
      getdata = response.json()
      countTurbo = getdata[1]["availableCount"]
      countFullEnergy = getdata[0]["availableCount"]
      status_code = response.status_code
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(response.text)
      print(f"Hàm ACTIVE_BOOST, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_WORMFARE()")
        RUN_WORMFARE()
        break
      COUNTDOWN(10)
    except ValueError:
      print(f"Hàm ACTIVE_BOOST, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm ACTIVE_BOOST, Key error: {e}")
      break
  return countTurbo, countFullEnergy, status_code

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
  print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TOOL WORMFARE{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>>
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱
{lục}[{đỏ}+{lục}] {trắng}Tên Tool{đen}: {vàng}Auto WORMFARE    {lục}[{đỏ}+{lục}] {trắng}Telegram{đen}: {vàng}Anubis MMO
{lục}[{đỏ}+{lục}] {trắng}Phiên bản{đen}: {vàng}Premium v5.0.0  {lục}[{đỏ}+{lục}] {trắng}Creator{đen}: {vàng}Nguyễn Quang Sáng
{lục}[{đỏ}+{lục}] {trắng}Link Tool{đen}: {vàng}t.me/AnubisMMO  {lục}[{đỏ}+{lục}] {trắng}Hướng Dẫn {đen}: {vàng}t.me/AnubisMMO
                   {hồng}Copyright by © Anubis MMO
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱""")
BANNER()
def RUN_WORMFARE():
  with open('../config/wormface.json', 'r') as file:
    config_data = json.load(file)
  users = config_data
  if len(users) > 10:
    print("Bạn chỉ được phép thêm tối đa 10 tài khoản để chạy tool")
    exit()
  for user in users:
    account = user["STT_ACCOUNT"]
    authorization = user["AUTHORIZATION"]
    if authorization == "":
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
      "Host":"elcevb3oz4.execute-api.eu-central-1.amazonaws.com",
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "gzip, deflate, br, zstd",
      "Accept-Language": "en-US,en;q=0.9",
      "Authorization": authorization,
      "Referer": "https://clicker.wormfare.com/",
      "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
      "Sec-Ch-Ua-Mobile": "?1",
      "Sec-Ch-Ua-Platform": '"Android"',
      "origin":"https://clicker.wormfare.com",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "cross-site",
      "User-Agent": user_agent,
      "priority":"u=1, i",
      "X-Api-Key": "9m60AhO1I9JmrYIsWxMnThXbF3nDW4GHFA1rde5PKzJmRA9Dv6LZ2YXSM6vvwigC"}
    username, dame, energyLeft, energyMax, energyPerSecond, balance, nameSquad, members, scoreSquad, isTurboAvailable = PROFILE(headers, proxies)
    countFullEnergy, countTurbo, RecoveryConfig, TapConfig, MaxEnergyConfig = SHOP(headers, proxies)
    timestamp = int(time.time() * 1000)
    energyLeft, newbalance = CLICK(headers, {"startTimestamp":timestamp,"amount":dame,"isTurbo":False}, proxies)
    print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TÀI KHOẢN WORMFARE{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>\n{đen}〘👤〙{trắng}UserName {đỏ}: {lục}{username} {vàng}{isTurboAvailable}\n{đen}〘🪙〙{trắng}Số Dư {đỏ}: {vàng}{balance:,}\n{đen}〘📊〙{trắng}Thông số Game{đỏ}: {vàng}+{dame}{đen}/{vàng}click {đỏ}[{lam}{energyLeft}{đen}/{lam}{energyMax}{đỏ}] {vàng}{countTurbo} {countFullEnergy}\n{đen}〘📧〙{trắng}Thông tin Squad{đỏ}: {xanh}{nameSquad} {đen}| {vàng}{scoreSquad} {đen}| {hồng}{members}👥\n{đen}〘🌏〙{trắng}IP {đỏ}: {nâu}{ip} {lục}»»» {trắng}Fake IP {đỏ}: {lam}{fakeip}\n""")
    start_time = datetime.now()
    print(f"{đỏ}\033[1;33;40mBẮT ĐẦU CHẠY TOOL {thường}{đậm}{đỏ}» {đen}[{vàng}{start_time.strftime('%H:%M:%S')}{đen}]\n")
    tasks = QUEST(headers, proxies)
    list_task = ["_JoinDiscordQuest","_JoinInstagramQuest","_JoinTwitterQuest","_JoinTikTokQuest","_JoinYoutubeQuest","_WatchWormfareVideoQuest"]
    for task in tasks:
      taskID = task["id"]
      if taskID in list_task and task["isRewardClaimed"] == False:
        if len(task["tasks"]) > 1:
          for i in task["tasks"]:
            data = {"questId":taskID,"taskId":i['id']}
            success = CHECK_QUEST(headers, data, proxies)
            #print(success)
        else:
          data = {"questId":taskID}
          success = CHECK_QUEST(headers, data, proxies)
        if success == True:
          success = CLAIM_QUEST(headers, data, proxies)
          if success == True:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Hoàn thành {lam}{taskID} {vàng}+{task['rewardAmount']}")
          else:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Claim phần thưởng {lam}{taskID} {đỏ}THẤT BẠI")
        else:
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Check nhiệm vụ {lam}{taskID} {đỏ}THẤT BẠI")
    print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}NÂNG CẤP BOOST")
    def UPGRADE(balance, TapConfig, RecoveryConfig, MaxEnergyConfig):
      while balance > RecoveryConfig["priceInScore"]or balance > MaxEnergyConfig["priceInScore"]:
        """
        if TapConfig["priceInScore"] <= RecoveryConfig["priceInScore"] and TapConfig["priceInScore"] <= MaxEnergyConfig["priceInScore"]:
          typeUpgrade = TapConfig["type"]
          level = TapConfig["level"] + 1
          price = TapConfig["priceInScore"]
          """
        if MaxEnergyConfig["priceInScore"] <= RecoveryConfig["priceInScore"] and MaxEnergyConfig["priceInScore"] <= TapConfig["priceInScore"]:
          typeUpgrade = MaxEnergyConfig["type"]
          level = MaxEnergyConfig["level"] + 1
          price = MaxEnergyConfig["priceInScore"]
        else:
          typeUpgrade = RecoveryConfig["type"]
          level = RecoveryConfig["level"] + 1
          price = RecoveryConfig["priceInScore"]
        balance = BUY_BOOST(headers, {"type":typeUpgrade}, proxies)
        nameUpgrade = typeUpgrade.replace('_',' ').upper()
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Nâng cấp {hồng}{nameUpgrade} {trắng}({lam}{level}{trắng}) {lục}• {đỏ}-{price} {đen}» {vàng}{balance:,}")
        countFullEnergy, countTurbo, RecoveryConfig, TapConfig, MaxEnergyConfig = SHOP(headers, proxies)
      return balance, TapConfig, RecoveryConfig, MaxEnergyConfig
    #balance, TapConfig, RecoveryConfig, MaxEnergyConfig = UPGRADE(balance, TapConfig, RecoveryConfig, MaxEnergyConfig)
    print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {đỏ}HẾT TIỀN NÂNG CẤP BOOST")
    
    if isTurboAvailable == True:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã kích hoạt Turbo", end=" ")
        timestamp = int(time.time() * 1000)
        amount = 1000*5*dame
        time.sleep(7)
        energyLeft, newbalance = CLICK(headers, {"startTimestamp":timestamp,"amount":amount,"isTurbo":True}, proxies)
        score = newbalance - balance
        balance = newbalance
        print(f"{vàng}+{score} {đỏ}» {vàng}{newbalance:,}")
        #exit()
        if score == 5000*5*dame:
          exit()
    
    username, dame, energyLeft, energyMax, energyPerSecond, balance, nameSquad, members, scoreSquad, isTurboAvailable = PROFILE(headers, proxies)
    while True:
      if energyLeft/dame > 10:
        if energyLeft/dame > 50:
          countTap = random.randint(50,int(energyLeft/dame))
        else:
          countTap = int(energyLeft/dame)
        timestamp = int(time.time() * 1000)
        time.sleep(3)
        amount = dame*countTap
        energyLeft, newbalance = CLICK(headers, {"startTimestamp":timestamp,"amount":amount,"isTurbo":False}, proxies)
        collectAmount = newbalance - balance
        balance = newbalance
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đen}╔═{đỏ}[{vàng}{now_time}{đỏ}] {trắng}Đã CLICK {lục}{countTap} {trắng}lần {vàng}+{collectAmount} {đỏ}»", end=" ")
        print(f"{vàng}{newbalance:,}\n{đen}╚⫸{hồng}Tải tool miễn phí tại Channel Telegram{đỏ}: {lục}@AnubisMMO\n")
      else:
        countFullEnergy, countTurbo, RecoveryConfig, TapConfig, MaxEnergyConfig = SHOP(headers, proxies)
        if countFullEnergy > 0:
          countTurbo, countFullEnergy, status_code = ACTIVE_BOOST(headers, {"type":"full_energy"}, proxies)
          if status_code == 200:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã kích hoạt Full Energy", end=" ")
            username, dame, energyLeft, energyMax, energyPerSecond, balance, nameSquad, members, scoreSquad, isTurboAvailable = PROFILE(headers, proxies)
            print(f"{đỏ}[{lam}{energyLeft}{đen}/{lam}{energyMax}{đỏ}]\n")
          else:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Đã kích hoạt Full Energy THẤT BẠI")
        else:
          if countTurbo > 0:
            for i in range(0,countTurbo):
              countTurbo, countFullEnergy, status_code = ACTIVE_BOOST(headers, {"type":"turbo"}, proxies)
              if status_code == 200:
                now_time = datetime.now().strftime("%H:%M:%S")
                print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã kích hoạt Turbo", end=" ")
                timestamp = int(time.time() * 1000)
                amount = 5000*5*dame
                time.sleep(7)
                energyLeft, newbalance = CLICK(headers, {"startTimestamp":timestamp,"amount":amount,"isTurbo":True}, proxies)
                score = newbalance - balance
                balance = newbalance
                print(f"{vàng}+{score} {đỏ}» {vàng}{newbalance:,}")
                if score >= 5000*5*dame:
                  exit()
                #balance, TapConfig, RecoveryConfig, MaxEnergyConfig = UPGRADE(balance, TapConfig, RecoveryConfig, MaxEnergyConfig)
              else:
                now_time = datetime.now().strftime("%H:%M:%S")
                print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Đã kích hoạt Turbo THẤT BẠI")
          print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}HẾT LƯỢT CLICK, HẾT BOOST {đỏ}» {vàng}ĐỔI TÀI KHOẢN")
          break
delay = input(f"{lục} NHẬP THỜI GIAN DELAY ĐỂ CHẠY LƯỢT TIẾP THEO{đỏ} : {vàng}")
while True:
 RUN_WORMFARE()
 time.sleep(delay)