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
def ME_TELEGRAM(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/auth/me-telegram", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/auth/me-telegram", headers=headers, timeout=30)
      response.raise_for_status()
      getdata = response.json()["telegramUser"]
      try:
        username = getdata["username"]
      except:
        username = getdata["lastName"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm ME_TELEGRAM, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm ME_TELEGRAM, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return username
def CONFIG(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/config", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/config", headers=headers, timeout=30)
      response.raise_for_status()
      config = response.json()["clickerConfig"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm CONFIG, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm CONFIG, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return config
def SYNC(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/sync", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/sync", headers=headers, timeout=30)
      response.raise_for_status()
      getdata = response.json()["clickerUser"]
      id_user = getdata["id"]
      balance = int(getdata["balanceCoins"])
      level = getdata["level"]
      energy = getdata["availableTaps"]
      energyMax = getdata["maxTaps"]
      dame = getdata["earnPerTap"]
      recoveryEnergy = getdata["tapsRecoverPerSec"]
      exchangeId = getdata["exchangeId"]
      earnPerHour = getdata["earnPassivePerHour"]
      
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm SYNC, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm SYNC, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return id_user, balance, level, energy, energyMax, dame, recoveryEnergy, exchangeId, earnPerHour
def LIST_TASKS(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/list-tasks", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/list-tasks", headers=headers, timeout=30)
      response.raise_for_status()
      list_tasks = response.json()["tasks"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm LIST_TASKS, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm LIST_TASKS, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return list_tasks
def CHECK_TASK(headers, data, balance, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/check-task", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/check-task", headers=headers, json=data, timeout=30)
      response.raise_for_status()
      getdata = response.json()["task"]
      status = getdata["isCompleted"]
      rewardTask = getdata["rewardCoins"]
      nameTask = data["taskId"].replace("_"," ")
      if status == True:
        balance = response.json()["clickerUser"]["balanceCoins"]
        if data["taskId"] == "streak_days":
          days = getdata["days"]
          rewardTask = getdata["rewardsByDays"][days-1]["rewardCoins"]
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} HOÀN THÀNH {lam}{nameTask.upper()} {vàng}+{rewardTask} {đen}» {vàng}{int(balance):,}")
      else:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{đỏ} LÀM NHIỆM VỤ {lam}{nameTask.upper()} {đỏ}THẤT BẠI {đen}» {vàng}{balance:,}")
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm CHECK_TASK, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm CHECK_TASK, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return nameTask, rewardTask
def SELECT_EXCHANGE(headers, balance, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/select-exchange", headers=headers, json={"exchangeId":"okx"}, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/select-exchange", headers=headers, json={"exchangeId":"okx"})
      response.raise_for_status()
      getdata = response.json()["clickerUser"]
      exchangeId = getdata["exchangeId"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm SELECT_EXCHANGE, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm SELECT_EXCHANGE, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return exchangeId
def UPGRADE_INFO(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/upgrades-for-buy", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/upgrades-for-buy", headers=headers, timeout=30)
      response.raise_for_status()
      upgradesInfo = response.json()["upgradesForBuy"]
      dailyCombo = response.json()["dailyCombo"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm UPGRADE_INFO, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm UPGRADE_INFO, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return upgradesInfo, dailyCombo
def BUY_UPGRADE(headers, data, balance, upgradesInfo, dailyCombo, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/buy-upgrade", headers=headers, json=data,  proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/buy-upgrade", headers=headers, json=data, timeout=30)
      
      response.raise_for_status()
      balance = response.json()["clickerUser"]["balanceCoins"]
      upgradesInfo = response.json()["upgradesForBuy"]
      dailyCombo = response.json()["dailyCombo"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      try:
        if response.json()["error_code"] in ["UPGRADE_MAX_LEVEL","UPGRADE_COOLDOWN","INSUFFICIENT_FUNDS"]:
          #print(response.json())
          break
      except: pass
      try:
        print(response.text)
      except: pass
      print(f"{đỏ}Hàm BUY_UPGRADE, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm BUY_UPGRADE, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return balance, upgradesInfo, dailyCombo
def CLAIM_1M(headers, data, balance, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/claim-daily-cipher", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/claim-daily-cipher", headers=headers, json=data, timeout=30)
      #response.raise_for_status()
      if response.status_code == 200:
        getdata = response.json()["dailyCipher"]
        status = getdata["isClaimed"]
        if status == True:
          balance = response.json()["clickerUser"]["balanceCoins"]
          rewardCipher = getdata["bonusCoins"]
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} HOÀN THÀNH {lam}MÃ MORSE {vàng}+{rewardCipher} {đen}» {vàng}{int(balance):,}")
      else:
        if response.json()["error_code"] == "DAILY_CIPHER_DOUBLE_CLAIMED":
          pass
          #now_time = datetime.now().strftime("%H:%M:%S")
          #print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} NHIỆM VỤ {lam}MÃ MORSE {trắng}ĐÃ HOÀN THÀNH TRƯỚC ĐÓ {đen}» {vàng}{int(balance):,}")
        else:
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{đỏ} LÀM NHIỆM VỤ {lam}MÃ MORSE {đỏ}THẤT BẠI {đen}» {vàng}{int(balance):,}")
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm CLAIM_1M, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm CLAIM_1M, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return balance
def CLAIM_5M(headers, balance, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/claim-daily-combo", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/claim-daily-combo", headers=headers, timeout=30)
      #response.raise_for_status()
      if response.status_code == 200:
        getdata = response.json()["dailyCombo"]
        status = getdata["isClaimed"]
        if status == True:
          balance = response.json()["clickerUser"]["balanceCoins"]
          rewardCipher = getdata["bonusCoins"]
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} HOÀN THÀNH {lam}DAILY COMBO {vàng}+{rewardCipher} {đen}» {vàng}{int(balance):,}\n")
      else:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{đỏ} LÀM NHIỆM VỤ {lam}DAILY COMBO {đỏ}THẤT BẠI {đen}» {vàng}{balance:,}\n")
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm CLAIM_5M, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm CLAIM_5M, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return balance
def BOOSTS(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/boosts-for-buy", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/boosts-for-buy", headers=headers, timeout=30)
      response.raise_for_status()
      getdata = response.json()["boostsForBuy"]
      tapConfig = getdata[0]
      energyConfig = getdata[1]
      fullenergyConfig = getdata[2]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm BOOSTS, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm BOOSTS, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return tapConfig, energyConfig, fullenergyConfig
def LEVEL_UP(headers, typeUpgrade, balance, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      timestamp = int(time.time() * 1000)
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/buy-boost", headers=headers, json={"boostId":typeUpgrade,"timestamp":timestamp}, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/buy-boost", headers=headers, json={"boostId":typeUpgrade,"timestamp":timestamp})
      response.raise_for_status()
      getdata = response.json()["clickerUser"]
      balance = int(getdata["balanceCoins"])
      energy = getdata["availableTaps"]
      dame = getdata["earnPerTap"]
      energyMax = getdata["maxTaps"]
      getdata = response.json()["boostsForBuy"]
      tapConfig = getdata[0]
      energyConfig = getdata[1]
      fullenergyConfig = getdata[2]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm LEVEL_UP, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm LEVEL_UP, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return balance, energy, dame, tapConfig, energyConfig, fullenergyConfig, energyMax
def TAP(headers, data, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api.hamsterkombat.io/clicker/tap", headers=headers, json=data, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api.hamsterkombat.io/clicker/tap", headers=headers, json=data, timeout=30)
      response.raise_for_status()
      getdata = response.json()["clickerUser"]
      balance = int(getdata["balanceCoins"])
      energy = getdata["availableTaps"]
      break
    except requests.exceptions.RequestException as e:
      error_count += 1
      print(f"{đỏ}Hàm TAP, đang xảy ra lỗi. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}. Lỗi: {str(e)}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
    except (ValueError, KeyError) as e:
      error_count += 1
      print(f"{đỏ}Hàm TAP, Error: {str(e)}. Thử lại lần {vàng}{error_count}{đen}/{vàng}{max_retries}{đỏ}")
      if error_count >= max_retries:
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩{trắng} Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_HAMSTER()")
        RUN_HAMSTER()
        break
      COUNTDOWN(10)
  return balance, energy


def UPGRADE(balance, tapConfig, energyConfig, fullenergyConfig, energy, dame):
  while balance > energyConfig["price"]:
    typeUpgrade = energyConfig["id"]
    level = energyConfig["level"]
    price = energyConfig["price"]
    balance, energy, dame, tapConfig, energyConfig, fullenergyConfig, energyMax = LEVEL_UP(headers,typeUpgrade, proxies)
    now_time = datetime.now().strftime("%H:%M:%S")
    print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Nâng cấp {hồng}{typeUpgrade} {trắng}({lam}{level+1}{trắng}) {lục}• {đỏ}-{price} {đen}» {vàng}{balance:,}")
  return balance, tapConfig, energyConfig, fullenergyConfig, energy, dame

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
  print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TOOL HAMSTER{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>>
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱
{lục}[{đỏ}+{lục}] {trắng}Tên Tool{đen}: {vàng}Auto HAMSTER     {lục}[{đỏ}+{lục}] {trắng}Telegram{đen}: {vàng}Anubis MMO
{lục}[{đỏ}+{lục}] {trắng}Phiên bản{đen}: {vàng}Premium v5.0.0  {lục}[{đỏ}+{lục}] {trắng}Creator{đen}: {vàng}Nguyễn Quang Sáng
{lục}[{đỏ}+{lục}] {trắng}Link Tool{đen}: {vàng}t.me/AnubisMMO  {lục}[{đỏ}+{lục}] {trắng}Hướng Dẫn {đen}: {vàng}t.me/AnubisMMO
                   {hồng}Copyright by © Anubis MMO
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱""")
def RUN_HAMSTER():
  with open('../config/hamster.json', 'r') as file:
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
      #print(f"{đỏ}Authorization của acc {vàng}{chon_acc} {đỏ}đang trống, hãy lấy mã Authorization nhập vào bên dưới")
      #authorization = input(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}NHẬP MÃ AUTHORIZATION{đen}: {lam}")
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
    #proxies = "None"
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
      "Host":"api.hamsterkombat.io",
      "Connection":"keep-alive",
      "sec-ch-ua":'"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
      "sec-ch-ua-mobile":"?1",
      "Authorization":authorization,
      "User-Agent":"Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36",
      "sec-ch-ua-platform": '"Android"',
      "accept": "*/*",
      "origin": "http://hamsterkombat.io",
      "x-requested-with": "mark.via.gx",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "http://hamsterkombat.io",
      "accept-encoding": "gzip, deflate, br, zstd",
      "priority": "u=1, i"
    }
    username = ME_TELEGRAM(headers, proxies)
    config = CONFIG(headers, proxies)
    id_user, balance, level, energy, energyMax, dame, recoveryEnergy, exchangeId, earnPerHour = SYNC(headers, proxies)
    upgradesInfo, dailyCombo = UPGRADE_INFO(headers, proxies)
    print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TÀI KHOẢN HAMSTER{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>\n{đen}〘👤〙{trắng}UserName {đỏ}: {lục}{username}\n{đen}〘🪙〙{trắng}Số Dư {đỏ}: {vàng}{balance:,} {đen}| {vàng}+{earnPerHour:,}{đỏ}/{vàng}h\n{đen}〘📊〙{trắng}Thông số Game{đỏ}: {lục}+{dame}{đen}/{lục}click {đỏ}[{lam}{energy}{đen}/{lam}{energyMax}{đỏ}]\n{đen}〘🌏〙{trắng}IP {đỏ}: {nâu}{ip} {lục}»»» {trắng}Fake IP {đỏ}: {lam}{fakeip}\n""")
    start_time = datetime.now()
    print(f"{đỏ}\033[1;33;40mBẮT ĐẦU CHẠY TOOL {thường}{đậm}{đỏ}» {đen}[{vàng}{start_time.strftime('%H:%M:%S')}{đen}]\n")
    if dailyCombo["isClaimed"] == False:
      print(f"{trắng}Thẻ đã thu thập {vàng}{dailyCombo['upgradeIds']}\n")
    if exchangeId == None or exchangeId == "hamster":
      exchangeId = SELECT_EXCHANGE(headers, proxies)
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}ĐÃ CHỌN SÀN {lam}{exchangeId.upper()}")
    list_tasks = LIST_TASKS(headers, proxies)
    for task in list_tasks:
      if task["isCompleted"] == False and task["id"] != "invite_friends":
        nameTask, rewardTask = CHECK_TASK(headers, {"taskId":task["id"]}, balance, proxies)
    #Mật mã
    balance = CLAIM_1M(headers, {"cipher":"ETHER"}, balance, proxies)
    totalNoAvailable = 0
    totalIsAvailable = 0
    tapConfig, energyConfig, fullenergyConfig = BOOSTS(headers, proxies)
    #Combo
    date_combo = "29/06/2024"
    if str(datetime.now().strftime("%d/%m/%Y")) == date_combo:
      list1 = ["youtube_25_million","compliance_officer","blocking_suspicious_accounts"]
    else:
      list1 = []
    list2 = dailyCombo["upgradeIds"]
    data_5M = list1.copy()
    for item in list2:
        if item in data_5M:
            data_5M.remove(item)
    def UPDATE_COMBO(idUpgrade,upgradesInfo, dailyCombo, balance, earnPerHour, targetLv, proxies):
      for u in upgradesInfo:
        if idUpgrade == u["id"]:
          id_upgrade = u["id"]
          name_upgrade = u["name"]
          profit_upgrade = u["profitPerHourDelta"]
          price_upgrade = u["price"]+1
          DK_upgrade = u["condition"]
          level_upgrade = u["level"]
          isAvailable_upgrade = u["isAvailable"]
          delay = 0
          try:
            delay = i["cooldownSeconds"]
          except: 
            delay = 0
          if delay != 0:
            isAvailable_upgrade = False
            break
          if u["condition"] != None:
            if u["isAvailable"] == False and u["condition"]["_type"] == "ByUpgrade":
              idUpgrade = u["condition"]["upgradeId"]
              targetLv = u["condition"]["level"]
              print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {đỏ}Cần nâng {hồng}{name_upgrade} {trắng}lên level {lam}{targetLv}")
              upgradesInfo, balance, earnPerHour, level_upgrade = UPDATE_COMBO(idUpgrade,upgradesInfo, dailyCombo, balance, earnPerHour, targetLv, proxies)
              now_time = datetime.now().strftime("%H:%M:%S")
              if level_upgrade >= targetLv:
                print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã nâng cấp {hồng}{name_upgrade} {lục}lên level {lam}{targetLv}\n")
              else:
                print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Chưa nâng cấp {hồng}{name_upgrade} {đỏ}lên level {lam}{targetLv} {trắng}({lam}{level_upgrade}{trắng})\n")
            elif u["condition"]["_type"] == "MoreReferralsCount" and u["isAvailable"] == False:
              moreRef = u["condition"]["moreReferralsCount"]
              print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {đỏ}Cần có thêm {vàng}{moreRef} Referral {đỏ}để nâng cấp thẻ {hồng}{u['name']}")
              break
          while u["isAvailable"] == True and level_upgrade < targetLv and balance > price_upgrade:
            timestamp = int(time.time() * 1000)
            newbalance, newupgradesInfo, dailyCombo = BUY_UPGRADE(headers, {"upgradeId":id_upgrade,"timestamp":timestamp}, balance, upgradesInfo, dailyCombo, proxies)
            earnPerHour += profit_upgrade
            if balance > newbalance:
              balance = newbalance
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đen}╔══{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Nâng cấp thẻ {hồng}{name_upgrade} {trắng}({lam}{level_upgrade+1}{trắng})")
              print(f"{đen}╚══⫸ {đỏ}-{price_upgrade:,} {lục}• {vàng}+{profit_upgrade:,}{đỏ}/{vàng}h {lục}»» {vàng}{earnPerHour:,}{đỏ}/{vàng}h {đen}»»» {vàng}{int(balance):,}\n")
            else:
              now_time = datetime.now().strftime("%H:%M:%S")
              print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Nâng cấp {hồng}{name_upgrade} {đỏ}THẤT BẠI\n")
              break
            for i in newupgradesInfo:
              if str(i["id"]) == id_upgrade:
                delay = 0
                try:
                  delay = i["cooldownSeconds"]
                except: 
                  delay = 0
                if delay != 0:
                  isAvailable_upgrade = False
                  break
                profit_upgrade = i["profitPerHourDelta"]
                price_upgrade = i["price"]
                isAvailable_upgrade = i["isAvailable"]
                level_upgrade = i["level"]
                break
            if targetLv == 999:
              break
          if balance < price_upgrade:
            print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {đỏ}Thiếu tiền nâng cấp {hồng}{name_upgrade} {vàng}Price {price_upgrade:,} {đen}» {vàng}{balance:,}")
            break
          break
      return upgradesInfo, balance, earnPerHour, level_upgrade
    for i in data_5M:
      for u in upgradesInfo:
        if u["id"] == i:
          id_upgrade = u["id"]
          name_upgrade = u["name"]
          profit_upgrade = u["profitPerHourDelta"]
          price_upgrade = u["price"]+1
          DK_upgrade = u["condition"]
          targetLv = u["level"]+1
          isAvailable_upgrade = u["isAvailable"]
          upgradesInfo, balance, earnPerHour, level_upgrade = UPDATE_COMBO(i,upgradesInfo, dailyCombo, balance, earnPerHour, targetLv, proxies)
          now_time = datetime.now().strftime("%H:%M:%S")
          if level_upgrade >= targetLv:
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã nâng cấp {lam}COMBO {hồng}{name_upgrade} {lục}lên level {lam}{targetLv}\n")
          else:
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Chưa nâng cấp {lam}COMBO {hồng}{name_upgrade} {đỏ}lên level {lam}{targetLv} {trắng}({lam}{level_upgrade}{trắng}\n)")
          break
    if dailyCombo["isClaimed"] == False:
      balance = CLAIM_5M(headers, balance, proxies)
    else:
      print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}Đã nhận {vàng}5M {trắng}ngày hôm nay\n")
    while True:
      if energy/dame > 10:
        countTap = int(energy/dame)
        timestamp = int(time.time() * 1000)
        amount = dame*countTap
        newbalance, energy = TAP(headers, {"count":countTap,"availableTaps":energy-countTap*dame,"timestamp":timestamp}, proxies)
        collectAmount = newbalance - balance
        balance = newbalance
        now_time = datetime.now().strftime("%H:%M:%S")
        print(f"{đen}╔═{đỏ}[{vàng}{now_time}{đỏ}] {trắng}Đã CLICK {lục}{countTap} {trắng}lần {vàng}+{collectAmount} {đỏ}»", end=" ")
        print(f"{vàng}{newbalance:,}\n{đen}╚⫸{hồng}Tải tool miễn phí tại Channel Telegram{đỏ}: {lục}@AnubisMMO\n")
      else:
        tapConfig, energyConfig, fullenergyConfig = BOOSTS(headers, proxies)
        if fullenergyConfig["level"] <= fullenergyConfig["maxLevel"] and fullenergyConfig["cooldownSeconds"] == 0:
          balance, energy, dame, tapConfig, energyConfig, newfullenergyConfig, energyMax = LEVEL_UP(headers,"BoostFullAvailableTaps", proxies)
          if fullenergyConfig["level"] < newfullenergyConfig["level"]:
            fullenergyConfig = newfullenergyConfig
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã kích hoạt Full Energy", end=" ")
            print(f"{đỏ}[{lam}{energy}{đen}/{lam}{energyMax}{đỏ}]\n")
          else:
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Đã kích hoạt Full Energy THẤT BẠI")
        else:
          break
    list_upgrade = []
    list_upgrade_Combo = []
    for upgrade in upgradesInfo:
      delay = 0
      id_upgrade = upgrade["id"]
      name_upgrade = upgrade["name"]
      profit_upgrade = upgrade["profitPerHourDelta"]
      price_upgrade = upgrade["price"]+1
      DK_upgrade = upgrade["condition"]
      level_upgrade = upgrade["level"]
      isAvailable_upgrade = upgrade["isAvailable"]
      isExpired_upgrade = upgrade["isExpired"]
      try:
        delay = upgrade["cooldownSeconds"]
      except:
        delay = 0
      if delay != 0:
        isAvailable_upgrade = False
        continue
      if isExpired_upgrade == False and isAvailable_upgrade == True and profit_upgrade*24*30 > price_upgrade:
        infoItem = f"{profit_upgrade/price_upgrade}|{profit_upgrade}|{price_upgrade}|{id_upgrade}|{level_upgrade}|{name_upgrade}|{isAvailable_upgrade}|"
        infoItem += (250-len(infoItem))*"x"
        list_upgrade.append(infoItem)
    list_upgrade = sorted(list_upgrade, key=lambda x: float(x.split('|')[0]), reverse=True)
    print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}HIỆN CÓ {lam}{len(list_upgrade)} {trắng}THẺ CÓ THỂ NÂNG CẤP")
    #print(list_upgrade)
    for i in range(0,len(list_upgrade)):
      upgrade = list_upgrade[i]
      if upgrade != list_upgrade[-1]:
        next_TB = list_upgrade[i+1]
        next_TB = float(next_TB.split('|')[0])
      upgradeInfo = upgrade.split('|')
      priceTB = float(upgradeInfo[0])
      profit_upgrade = int(upgradeInfo[1])
      price_upgrade = int(upgradeInfo[2])
      id_upgrade = upgradeInfo[3]
      level_upgrade = int(upgradeInfo[4])
      name_upgrade = upgradeInfo[5]
      isAvailable_upgrade = upgradeInfo[6]
      if balance < price_upgrade:
        #print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {đỏ}THIẾU TIỀN NÂNG {hồng}{name_upgrade} {vàng}{profit_upgrade:,}{đỏ}/{vàng}h {đen}| {đỏ}{price_upgrade} {đen}» {vàng}{balance:,}")
        continue
      while balance > price_upgrade and isAvailable_upgrade == "True":
        timestamp = int(time.time() * 1000)
        if len(list_upgrade) > 1:
          if upgrade != list_upgrade[-2] and id_upgrade not in list_upgrade:
            if profit_upgrade/price_upgrade < next_TB:
              break
        newbalance, newupgradesInfo, dailyCombo = BUY_UPGRADE(headers, {"upgradeId":id_upgrade,"timestamp":timestamp}, balance, upgradesInfo, dailyCombo, proxies)
        earnPerHour += profit_upgrade
        if balance > newbalance:
          balance = newbalance
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đen}╔══{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Nâng cấp thẻ {hồng}{name_upgrade} {trắng}({lam}{level_upgrade+1}{trắng})")
          print(f"{đen}╚══⫸ {đỏ}-{price_upgrade:,} {lục}• {vàng}+{profit_upgrade:,}{đỏ}/{vàng}h {lục}»» {vàng}{earnPerHour:,}{đỏ}/{vàng}h {đen}»»» {vàng}{int(balance):,}\n")
          if len(dailyCombo["upgradeIds"]) == 3 and dailyCombo["isClaimed"] == False:
            balance = CLAIM_5M(headers, balance, proxies)
        else:
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Nâng cấp {hồng}{name_upgrade} {đỏ}THẤT BẠI")
          break
        if upgrade == list_upgrade[-1]:
          break
        for i in newupgradesInfo:
          if str(i["id"]) == id_upgrade:
            delay = 0
            try:
              delay = i["cooldownSeconds"]
            except: 
              delay = 0
            if delay != 0:
              isAvailable_upgrade = False
              break
            profit_upgrade = i["profitPerHourDelta"]
            price_upgrade = i["price"]
            isAvailable_upgrade = str(i["isAvailable"])
            level_upgrade = i["level"]
            break
    print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}KHÔNG ĐỦ TIỀN ĐỂ NÂNG CẤP THẺ LỢI NHUẬN CAO")
    print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}HẾT LƯỢT CLICK, HẾT BOOST {đỏ}» {vàng}ĐỔI TÀI KHOẢN")
BANNER()
"""
print(f"{đỏ}⟩{vàng}⟩{lục}⟩ TÙY CHỌN CHỨC NĂNG TOOL
{đỏ}⟨{vàng}1{đỏ}⟩ {trắng}Chạy tool
{đỏ}⟨{vàng}2{đỏ}⟩ {trắng}Sửa cấu hình tài khoản
")
while True:
  selectFunction = (input(f"{đỏ}⟩{vàng}⟩{lục}⟩ {lam}Nhập chức năng Tool{đỏ}: ")
  if selectFunction == "1":
    
"""
delay = input(f"{lục} NHẬP THỜI GIAN DELAY ĐỂ CHẠY LƯỢT TIẾP THEO{đỏ} : {vàng}")
while True:
 RUN_HAMSTER()
 time.sleep(delay)