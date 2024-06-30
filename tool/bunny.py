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

  while True:
    try:
      if proxies:
        response = requests.get("https://api.bunnyapp.io/", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api.bunnyapp.io/", headers=headers, timeout=30)
      response.raise_for_status()
      getdata = response.json()
      username = getdata["user"]["nickname"]
      balance = getdata["user"]["coins"]
      energy = getdata["energy"]
      clan = getdata["clan"]
      dame = getdata["user"]["upgrades"]["multitap"]["value"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm PROFILE, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm PROFILE, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)

  return username, balance, energy, clan, dame

def CLICK(headers, data, proxies=None):
  error_count = 0
  max_retries = 10

  while True:
    try:
      if proxies:
        response = requests.post("https://api.bunnyapp.io/taps", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.bunnyapp.io/taps", headers=headers, json=data, timeout=30)
      response.raise_for_status()
      getdata = response.json()
      balance = getdata["coins"]
      energy = getdata["energy"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm CLICK, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm CLICK, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)

  return balance, energy

def ACTIVE_BOOST(headers, type_boost, proxies=None):
  error_count = 0
  max_retries = 10

  while True:
    try:
      if proxies:
        response = requests.post(f"https://api.bunnyapp.io/boosts/action/{type_boost}", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post(f"https://api.bunnyapp.io/boosts/action/{type_boost}", headers=headers, timeout=30)
      response.raise_for_status()
      getdata = response.json()
      status = getdata["status"]
      energy = getdata["energy"]
      break
    except requests.exceptions.RequestException as e:
      getdata = response.json()
      status = getdata["status"]
      if status == "error" and getdata.get("error_message") == "mega_boost_already_activated":
        status = "success"
        energy = 0
        break
      error_count += 1
      print(f"{đỏ}Hàm ACTIVE_BOOST, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm ACTIVE_BOOST, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)

  return energy, status

def BOOSTS(headers, proxies=None):
  error_count = 0
  max_retries = 10

  while True:
    try:
      if proxies:
        response = requests.get("https://api.bunnyapp.io/boosts", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api.bunnyapp.io/boosts", headers=headers, timeout=30)
      response.raise_for_status()
      getdata = response.json()
      type0 = getdata["actions"][0]["type"]
      type1 = getdata["actions"][1]["type"]
      if type0 == "MEGA_BOOST" or type1 == "RESET_ENERGY":
        countTurbo = getdata["actions"][0]["count"]
        countFullEnergy = getdata["actions"][1]["count"]
      else:
        countTurbo = getdata["actions"][1]["count"]
        countFullEnergy = getdata["actions"][0]["count"]
      tapConfig = getdata["upgrades"][0]
      energyConfig = getdata["upgrades"][1]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm BOOSTS, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm BOOSTS, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)

  return countTurbo, countFullEnergy, tapConfig, energyConfig

def DAILY(headers, proxies=None):
  error_count = 0
  max_retries = 10

  while True:
    try:
      if proxies:
        response = requests.post("https://api.bunnyapp.io/daily/claim", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.bunnyapp.io/daily/claim", headers=headers, timeout=30)
      response.raise_for_status()
      getdata = response.json()
      status = getdata["status"]
      if status == "success":
        reward_amount = getdata["reward_amount"]
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Điểm danh thành công {vàng}+{reward_amount}")
      break
    except requests.exceptions.RequestException as e:
      try:
        getdata = response.json()
        status = getdata["status"]
        if status == "error":
          reward_amount = 0
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ Điểm danh thất bại hoặc đã điểm danh trước đó")
          break
      except: pass
      error_count += 1
      print(f"{đỏ}Hàm DAILY, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm DAILY, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)

  return reward_amount, status

def MEGA_CLICK(headers, data, proxies=None):
  error_count = 0
  max_retries = 10

  while True:
    try:
      if proxies:
        response = requests.post("https://api.bunnyapp.io/taps/mega", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.bunnyapp.io/taps/mega", headers=headers, json=data, timeout=30)
      response.raise_for_status()
      getdata = response.json()
      balance = getdata["coins"]
      energy = getdata["energy"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm MEGA_CLICK, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm MEGA_CLICK, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)

  return balance, energy

def LEVEL_UP(headers, typeUpgrade, key_level, proxies=None):
  error_count = 0
  max_retries = 10

  while True:
    try:
      if proxies:
        response = requests.post(f"https://api.bunnyapp.io/boosts/upgrade/{typeUpgrade}/{key_level}", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post(f"https://api.bunnyapp.io/boosts/upgrade/{typeUpgrade}/{key_level}", headers=headers, timeout=30)
      response.raise_for_status()
      getdata = response.json()
      balance = getdata["user"]["coins"]
      energy = getdata["energy"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm LEVEL_UP, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm LEVEL_UP, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_BUNNY()")
        RUN_BUNNY()
        break
      COUNTDOWN(10)

  return balance, energy

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
  print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TOOL BUNNY{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>>>
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱
{lục}[{đỏ}+{lục}] {trắng}Tên Tool{đen}: {vàng}Auto BUNNY       {lục}[{đỏ}+{lục}] {trắng}Telegram{đen}: {vàng}Anubis MMO
{lục}[{đỏ}+{lục}] {trắng}Phiên bản{đen}: {vàng}Premium v5.0.0  {lục}[{đỏ}+{lục}] {trắng}Creator{đen}: {vàng}Nguyễn Quang Sáng
{lục}[{đỏ}+{lục}] {trắng}Link Tool{đen}: {vàng}t.me/AnubisMMO  {lục}[{đỏ}+{lục}] {trắng}Hướng Dẫn {đen}: {vàng}t.me/AnubisMMO
                   {hồng}Copyright by © Anubis MMO
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱""")
BANNER()
def RUN_BUNNY():
  with open('../config/bunny.json', 'r') as file:
    config_data = json.load(file)
  users = config_data
  if len(users) > 10:
    print("Bạn chỉ được phép thêm tối đa 10 tài khoản để chạy tool")
    exit()
  for user in users:
    account = user["STT_ACCOUNT"]
    cookie = user["COOKIE"]
    if cookie == "":
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
      "Host": "api.bunnyapp.io",
      "sec-ch-ua": '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
      "accept-language": "en",
      "sec-ch-ua-mobile": "?1",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.54 Mobile Safari/537.36",
      "sec-ch-ua-platform": '"Android"',
      "accept": "*/*",
      "origin": "https://bunnyapp.io",
      "x-requested-with": "mark.via.gx",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://bunnyapp.io/",
      "accept-encoding": "gzip, deflate, br, zstd",
      "cookie": cookie,
      "priority": "u=1, i"
    }
    
    username, balance, energy, clan, dame= PROFILE(headers, proxies)
    countTurbo, countFullEnergy, tapConfig, energyConfig = BOOSTS(headers, proxies)
    print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TÀI KHOẢN BUNNY{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>\n{đen}〘👤〙{trắng}UserName {đỏ}: {lục}{username}\n{đen}〘🪙〙{trắng}Số Dư {đỏ}: {vàng}{balance:,}\n{đen}〘📊〙{trắng}Thông số Game{đỏ}: {lục}+{dame}{đen}/{lục}click {vàng}{energy}⚡ {lam}{countTurbo} {countFullEnergy}\n{đen}〘📧〙{trắng}Thông tin Clan{đỏ}: {xanh}{clan['title']}\n{đen}〘🌏〙{trắng}IP {đỏ}: {nâu}{ip} {lục}»»» {trắng}Fake IP {đỏ}: {lam}{fakeip}\n""")
    start_time = datetime.now()
    print(f"{đỏ}\033[1;33;40mBẮT ĐẦU CHẠY TOOL {thường}{đậm}{đỏ}» {đen}[{vàng}{start_time.strftime('%H:%M:%S')}{đen}]\n")
    reward_amount, status = DAILY(headers, proxies)
    def UPGRADE(balance, tapConfig, energyConfig):
      while balance > tapConfig["cost"] or balance > energyConfig["cost"]:
        if tapConfig["cost"] <= energyConfig["cost"]:
          typeUpgrade = tapConfig["type"]
          level = tapConfig["level"]
          key_level = level*2+1
          price = tapConfig["cost"]
        else:
          typeUpgrade = energyConfig["type"]
          level = energyConfig["level"]
          key_level = level*2+2
          price = energyConfig["cost"]
        balance, energy = LEVEL_UP(headers,typeUpgrade, key_level, proxies)
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Nâng cấp {hồng}{typeUpgrade} {trắng}({lam}{level+1}{trắng}) {lục}• {đỏ}-{price} {đen}» {vàng}{balance:,}\n")
        countTurbo, countFullEnergy, tapConfig, energyConfig = BOOSTS(headers, proxies)
      return balance, tapConfig, energyConfig
    #print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}NÂNG CẤP BOOST")
    #balance, tapConfig, energyConfig = UPGRADE(balance, tapConfig, energyConfig)
    #print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {đỏ}HẾT TIỀN NÂNG CẤP BOOST\n")
    username, balance, energy, clan, dame= PROFILE(headers, proxies)
    while True:
      if energy > 0:
        for i in range(0,energy):
          newbalance, energy = CLICK(headers, {"coins":1000*dame}, proxies)
          collectAmount = newbalance - balance
          balance = newbalance
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đen}╔═{đỏ}[{vàng}{now_time}{đỏ}] {trắng}Đã CLICK {vàng}+{collectAmount} {đỏ}• {lam}{energy} energy {đỏ}»", end=" ")
          print(f"{vàng}{newbalance:,}\n{đen}╚⫸{hồng}Tải tool miễn phí tại Channel Telegram{đỏ}: {lục}@AnubisMMO\n")
          #balance, tapConfig, energyConfig = UPGRADE(balance, tapConfig, energyConfig)
          username, balance, energy, clan, dame= PROFILE(headers, proxies)
      else:
        countTurbo, countFullEnergy, tapConfig, energyConfig = BOOSTS(headers, proxies)
        if countFullEnergy > 0:
          #print(countFullEnergy)
          energy, status = ACTIVE_BOOST(headers, "RESET_ENERGY", proxies)
          if status == "success":
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã kích hoạt Full Energy {đỏ}• {lam}{energy} energy\n")
          else:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Đã kích hoạt Full Energy THẤT BẠI")
        else:
          if countTurbo > 2:
            for i in range(2,countTurbo):
              energy, status = ACTIVE_BOOST(headers, "MEGA_BOOST", proxies)
              if status == "success":
                now_time = datetime.now().strftime("%H:%M:%S")
                print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã kích hoạt Turbo", end=" ")
                newbalance, energy = MEGA_CLICK(headers, {"coins":1000*dame*10},proxies)
                score = newbalance - balance
                balance = newbalance
                print(f"{vàng}+{score} {đỏ}» {vàng}{newbalance:,}")
                #balance, tapConfig, energyConfig = UPGRADE(balance, tapConfig, energyConfig)
                username, balance, energy, clan, dame= PROFILE(headers, proxies)
              else:
                now_time = datetime.now().strftime("%H:%M:%S")
                print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Đã kích hoạt Turbo THẤT BẠI")
          print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}HẾT LƯỢT CLICK, HẾT BOOST {đỏ}» {vàng}ĐỔI TÀI KHOẢN")
          break
delay = input(f"{lục} NHẬP THỜI GIAN DELAY ĐỂ CHẠY LƯỢT TIẾP THEO{đỏ} : {vàng}")
while True:
 RUN_BUNNY()
 time.sleep(delay)