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
  
def AccountInfo(headers, proxies=None):
  message = totalAmount = userLevel = userId = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://api-backend.yescoin.gold/account/getAccountInfo", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api-backend.yescoin.gold/account/getAccountInfo", headers=headers, timeout=30)
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        balance = data["data"]["currentAmount"]
        userLevel = data["data"]["userLevel"]
        userId = data["data"]["userId"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      
      print(f"Hàm getAccountInfo, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm getAccountInfo, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm getAccountInfo, Key error: {e}")
      break
  return balance, userLevel, userId
def GameInfo(headers, proxies=None):
  message = level_Click = max_energy = energy = reset_energy = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://api-backend.yescoin.gold/game/getGameInfo", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api-backend.yescoin.gold/game/getGameInfo", headers=headers, timeout=30)
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        click_value = data["data"]["singleCoinValue"]
        max_energy = data["data"]["coinPoolTotalCount"]
        energy = data["data"]["coinPoolLeftCount"]
        recovery_energy = data["data"]["coinPoolRecoverySpeed"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      
      #print(f"Hàm getGameInfo, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm getGameInfo, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm getGameInfo, Key error: {e}")
      break
  return click_value, max_energy, energy, recovery_energy
def mySquad(headers, proxies=None):
  message = squadMembers = squadCoin = squadLevel = squadName = squadTgLink = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://api-backend.yescoin.gold/squad/mySquad", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api-backend.yescoin.gold/squad/mySquad", headers=headers, timeout=30)
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        isJoinSquad = data["data"]["isJoinSquad"]
        if isJoinSquad == True:
          squadInfo = data["data"]["squadInfo"]
          squadMembers = squadInfo["squadMembers"]
          squadCoin = squadInfo["squadTotalAmount"]
          squadLevel = squadInfo["squadLevel"]
          squadName = squadInfo["squadTitle"]
          squadLink = squadInfo["squadTgLink"]
        else:
          squadMembers, squadCoin, squadLevel, squadName, squadLink = joinSquad(headers, proxies)
      break
    except requests.exceptions.RequestException:
      error_count += 1
     # print(f"Hàm mySquad, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm mySquad, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm mySquad, Key error: {e}")
      break
  return squadMembers, squadCoin, squadLevel, squadName, squadLink

def joinSquad(headers, proxies=None):
  message = squadTitle = isJoinSquad = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api-backend.yescoin.gold/squad/joinSquad", headers=headers, json={"squadTgLink":"@anubismmo"}, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api-backend.yescoin.gold/squad/joinSquad", headers=headers, json={"squadTgLink":"@anubismmo"})
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        isJoinSquad = data["data"]["isJoinSquad"]
        if isJoinSquad == True:
          squadInfo = data["data"]["squadInfo"]
          squadMembers = squadInfo["squadMembers"]
          squadCoin = squadInfo["squadTotalAmount"]
          squadLevel = squadInfo["squadLevel"]
          squadName = squadInfo["squadTitle"]
          squadLink = squadInfo["squadTgLink"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm joinSquad, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm joinSquad, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm joinSquad, Key error: {e}")
      break
  return squadMembers, squadCoin, squadLevel, squadName, squadLink
def leaveSquad(headers, proxies=None):
  headers["content-type"] = "application/x-www-form-urlencoded"
  message = data = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://api-backend.yescoin.gold/squad/leaveSquad", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api-backend.yescoin.gold/squad/leaveSquad", headers=headers, timeout=30)
      #response.raise_for_status()
      data = response.json()
      print(data)
      message = data["message"]
      if message == "Success":
        data = data["data"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm leaveSquad, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm leaveSquad, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm leaveSquad, Key error: {e}")
      break
  return data
def getListTask(headers, proxies=None):
  message = data = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://api-backend.yescoin.gold/task/getCommonTaskList", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api-backend.yescoin.gold/task/getCommonTaskList", headers=headers, timeout=30)
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        listTask = data["data"]
        for Task in listTask:
          taskStatus = Task["taskStatus"]
          if taskStatus == 0:
            taskName, bonusAmount = finishTask(headers,Task,proxies)
            now_time = datetime.now().strftime("%H:%M:%S")
            print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã hoàn thành nhiệm vụ {lục}{taskName} {vàng}+{bonusAmount}🪙")
      break
    except requests.exceptions.RequestException:
      error_count += 1
      
      #print(f"Hàm getListTask, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm getListTask, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm getListTask, Key error: {e}")
      break
def finishTask(headers,Task, proxies=None):
  taskId = Task["taskId"]
  taskName = Task["taskName"]
  message = bonusAmount = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api-backend.yescoin.gold/task/finishTask", headers=headers, json=taskId, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api-backend.yescoin.gold/task/finishTask", headers=headers, json=taskId)
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        bonusAmount = data["data"]["bonusAmount"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm finishTask, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm finishTask, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm finishTask, Key error: {e}")
      break
  return taskName, bonusAmount
def Collect(headers,countCollect, proxies=None):
  message = collectAmount = collectStatus = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api-backend.yescoin.gold/game/collectCoin", headers=headers, json=countCollect, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api-backend.yescoin.gold/game/collectCoin", headers=headers, json=countCollect)
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        collectAmount = data["data"]["collectAmount"]
        collectStatus = data["data"]["collectStatus"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
     # print(f"Hàm Collect, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm Collect, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm Collect, Key error: {e}")
      break
  return collectAmount, collectStatus
def ChestInfo(headers, proxies=None):
  message = collectAmount = collectStatus = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://api-backend.yescoin.gold/game/getSpecialBoxInfo", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api-backend.yescoin.gold/game/getSpecialBoxInfo", headers=headers, timeout=30)
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        autoBox = data["data"]["autoBox"]
        if autoBox != None:
          boxStatus = autoBox["boxStatus"]
          if boxStatus == True:
            CollectChest(headers, autoBox, proxies)
        recoveryBox = data["data"]["recoveryBox"]
        if recoveryBox != None:
          boxStatus = recoveryBox["boxStatus"]
          if boxStatus == True:
            CollectChest(headers, recoveryBox, proxies)
      break
    except requests.exceptions.RequestException:
      error_count += 1
      
      #print(f"Hàm ChestInfo, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm ChestInfo, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm ChestInfo, Key error: {e}")
      break
def CollectChest(headers, infoBox, proxies=None):
  boxType = infoBox["boxType"]
  ChestTotalCount = infoBox["specialBoxTotalCount"]
  message = collectAmount = collectStatus = ""
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api-backend.yescoin.gold/game/collectSpecialBoxCoin", headers=headers, json={"boxType":boxType,"coinCount":ChestTotalCount}, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api-backend.yescoin.gold/game/collectSpecialBoxCoin", headers=headers, json={"boxType":boxType,"coinCount":ChestTotalCount})
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        collectAmount = data["data"]["collectAmount"]
        collectStatus = data["data"]["collectStatus"]
        now_time = datetime.now().strftime("%H:%M:%S")
        if collectStatus == True:
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã mở Kho Báu {vàng}+{collectAmount}🪙 {đỏ}»", end=" ")
          #exit()
        else:
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Mở kho báu THẤT BẠI {đỏ}»", end=" ")
        balance, userLevel, userId = AccountInfo(headers,proxies)
        print(f"{vàng}🪙{balance:,}\n")
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm CollectChest, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm CollectChest, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm CollectChest, Key error: {e}")
      break
def AccountBuild(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.get("https://api-backend.yescoin.gold/build/getAccountBuildInfo", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.get("https://api-backend.yescoin.gold/build/getAccountBuildInfo", headers=headers, timeout=30)
      #response.raise_for_status()
      data = response.json()
      
      message = data["message"]
      if message == "Success":
        ChestCount = data["data"]["specialBoxLeftRecoveryCount"]
        RecoveryCount = data["data"]["coinPoolLeftRecoveryCount"]
        ClickConfig = [data["data"]["singleCoinValue"],data["data"]["singleCoinLevel"],data["data"]["singleCoinUpgradeCost"]]
        RecoveryConfig = [data["data"]["coinPoolRecoverySpeed"],data["data"]["coinPoolRecoveryLevel"],data["data"]["coinPoolRecoveryUpgradeCost"]]
        EnergyConfig = [data["data"]["coinPoolTotalCount"],data["data"]["coinPoolTotalLevel"],data["data"]["coinPoolTotalUpgradeCost"]]
        BotConfig = [data["data"]["swipeBotSpeedValue"],data["data"]["swipeBotLevel"],data["data"]["swipeBotUpgradeCost"]]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      
     # print(f"Hàm AccountBuild, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm AccountBuild, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm AccountBuild, Key error: {e}")
      break
  return ChestCount, RecoveryCount, ClickConfig, RecoveryConfig, EnergyConfig, BotConfig
def recoverChest(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api-backend.yescoin.gold/game/recoverSpecialBox", headers=headers, json={}, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api-backend.yescoin.gold/game/recoverSpecialBox", headers=headers, json={})
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        data = data["data"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm recoverChest, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm recoverChest, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm recoverChest, Key error: {e}")
      break
  return data
def recoverCoinPool(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api-backend.yescoin.gold/game/recoverCoinPool", headers=headers, json={}, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api-backend.yescoin.gold/game/recoverCoinPool", headers=headers, json={})
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        data = data["data"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm recoverCoinPool, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm recoverCoinPool, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm recoverCoinPool, Key error: {e}")
      break
  return data
def levelUp(headers, dataUpgrade, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api-backend.yescoin.gold/build/levelUp", headers=headers, json=dataUpgrade, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api-backend.yescoin.gold/build/levelUp", headers=headers, json=dataUpgrade)
      #response.raise_for_status()
      data = response.json()
      message = data["message"]
      if message == "Success":
        data = data["data"]
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm levelUp, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm levelUp, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm levelUp, Key error: {e}")
      break
  return data
def ClaimOffline(headers, proxies=None):
  error_count = 0
  max_retries = 10
  while True:
    try:
      if proxies:
        response = requests.post("https://api-backend.yescoin.gold/game/claimOfflineYesPacBonus", headers=headers, proxies=proxies, timeout=30)
      else:
        response = requests.post("https://api-backend.yescoin.gold/game/claimOfflineYesPacBonus", headers=headers)
      #response.raise_for_status()
      data = response.json()
      #print(data)
      message = data["message"]
      if message == "Success":
        collectAmount = data["data"]["collectAmount"]
        status = data["data"]["collectStatus"]
      else:
        collectAmount = None
        status = False
      break
    except requests.exceptions.RequestException:
      error_count += 1
      print(f"Hàm ClaimOffline, đang xảy ra lỗi. Thử lại lần {error_count}/{max_retries}")
      if error_count >= max_retries:
        print("Đã gặp lỗi quá 10 lần, khởi chạy hàm RUN_YESCOIN()")
        RUN_YESCOIN()
    except ValueError:
      print(f"Hàm ClaimOffline, Error decoding JSON response")
      break
    except KeyError as e:
      print(f"Hàm ClaimOffline, Key error: {e}")
      break
  return collectAmount, status

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
  print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TOOL YESCOIN {đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>>>
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱
{lục}[{đỏ}+{lục}] {trắng}Tên Tool{đen}: {vàng}Auto YesCoin     {lục}[{đỏ}+{lục}] {trắng}Telegram{đen}: {vàng}Anubis MMO
{lục}[{đỏ}+{lục}] {trắng}Phiên bản{đen}: {vàng}Premium v5.0.0  {lục}[{đỏ}+{lục}] {trắng}Creator{đen}: {vàng}Nguyễn Quang Sáng
{lục}[{đỏ}+{lục}] {trắng}Link Tool{đen}: {vàng}t.me/AnubisMMO  {lục}[{đỏ}+{lục}] {trắng}Hướng Dẫn {đen}: {vàng}t.me/AnubisMMO
                   {hồng}Copyright by © Anubis MMO
{trắng}▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱""")
BANNER()
def RUN_YESCOIN():
  stt = 0
  with open('../config/yescoin.json', 'r') as file:
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
      'Host':'api.yescoin.gold',
      'sec-ch-ua':'"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
      'sec-ch-ua-mobile':'?1',
      'token':authorization,
      'user-agent':user_agent,
      'sec-ch-ua-platform':'"Android"',
      'accept':'*/*',
      'origin':'https://www.yescoin.gold',
      'x-requested-with':'mark.via.gp',
      'sec-fetch-site':'cross-site',
      'sec-fetch-mode':'cors',
      'sec-fetch-dest':'empty',
      'referer':'https://www.yescoin.gold/',
      'accept-encoding':'gzip, deflate, br, zstd',
      'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
      'priority':'u=1, i'}
    balance, userLevel, userId = AccountInfo(headers,proxies)
    click_value, max_energy, energy, recovery_energy = GameInfo(headers, proxies)
    squadMembers, squadCoin, squadLevel, squadName, squadTgLink = mySquad(headers, proxies)
    ChestCount, RecoveryCount, ClickConfig, RecoveryConfig, EnergyConfig, BotConfig = AccountBuild(headers, proxies)
    print(f"""{đậm}{đen}<<<<<<<<<<<<<<<<{lam}[{vàngBG}{đỏ}THÔNG TIN TÀI KHOẢN YESCOIN{đenBG}{lam}]{đen}>>>>>>>>>>>>>>>>>\n{đen}〘👤〙{trắng}UserID {đỏ}: {lục}{userId}\n{đen}〘🪙〙{trắng}Số Dư {đỏ}: {vàng}{balance:,}\n{đen}〘🔢〙{trắng}Level {đỏ}: {lam}{userLevel} \n{đen}〘📊〙{trắng}Thông số Game{đỏ}: {vàng}+{click_value}{đen}/{vàng}click {đỏ}[{lam}{energy}{đen}/{lam}{max_energy}{đỏ}] {hồng}{BotConfig[1]}🤖\n{đen}〘🛖〙{trắng}Thông tin Squad{đỏ}: {xanh}{squadName} {đen}| {vàng}{squadCoin}🪙 {đen}| {lục}{squadMembers}👥\n{đen}〘🌏〙{trắng}IP {đỏ}: {nâu}{ip} {lục}»»» {trắng}Fake IP {đỏ}: {lam}{fakeip}
  """)
    start_time = datetime.now()
    print(f"{đỏ}\033[1;33;40mBẮT ĐẦU CHẠY TOOL {thường}{đậm}{đỏ}» {đen}[{vàng}{start_time.strftime('%H:%M:%S')}{đen}]\n")
    getListTask(headers,proxies)
    
    #print(BotConfig)
    print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}NÂNG CẤP BOOST")
    def UPGRADE(balance, ClickConfig,RecoveryConfig,EnergyConfig, BotConfig):
      while balance > BotConfig[2]:
        level = BotConfig[1]
        if level >= 5:
          break
        priceLevelUp = BotConfig[2]
        nameLevelUp = "Bot Claim"
        dataUpgrade = 4
        """
        if RecoveryConfig[2] <= ClickConfig[2] and RecoveryConfig[2] <= EnergyConfig[2] and RecoveryConfig[2] <= BotConfig[2] :
          level = RecoveryConfig[1]
          if level >= 12:
            break
          priceLevelUp = RecoveryConfig[2]
          nameLevelUp = "Recovery Coin"
          dataUpgrade = 2
        elif EnergyConfig[2] <= ClickConfig[2] and EnergyConfig[2] <= RecoveryConfig[2] and EnergyConfig[2] <= BotConfig[2] :
          level = EnergyConfig[1]
          if level >= 15:
            break
          priceLevelUp = EnergyConfig[2]
          nameLevelUp = "Max Energy"
          dataUpgrade = 3
        else:
          level = ClickConfig[1]
          if level >= 10:
            break
          priceLevelUp = ClickConfig[2]
          nameLevelUp = "Click Value"
          dataUpgrade = 1
        """
        data = levelUp(headers, dataUpgrade, proxies)
        balance, userLevel, userId = AccountInfo(headers,proxies)
        ChestCount, RecoveryCount, ClickConfig, RecoveryConfig, EnergyConfig, BotConfig = AccountBuild(headers, proxies)
        now_time = datetime.now().strftime("%H:%M:%S")
        if data == True:
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {trắng}Nâng cấp {lục}{nameLevelUp} {trắng}({lam}{level+1}{trắng}) {đỏ}-{priceLevelUp} {đen}» {vàng}{balance:,}")
        else:
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Nâng cấp {lục}{nameLevelUp} {đỏ} THẤT BẠI {đen}» {vàng}{balance:,}")
      return balance, ClickConfig,RecoveryConfig,EnergyConfig, BotConfig
    balance, ClickConfig,RecoveryConfig,EnergyConfig, BotConfig = UPGRADE(balance, ClickConfig,RecoveryConfig,EnergyConfig, BotConfig)
    print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {đỏ}KHÔNG ĐỦ TIỀN NÂNG CẤP")
    if ChestCount > 0:
      for i in range(0,ChestCount):
        data = recoverChest(headers, proxies)
        if data == True:
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã kích hoạt kho báu\n")
          ChestInfo(headers, proxies)
        else:
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Kích hoạt kho báu thất bại\n")
    collectAmount, status = ClaimOffline(headers,proxies)
    if status == True:
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã {lam}Claim Offline {vàng}+{collectAmount:,}\n")
    while True:
      ChestInfo(headers, proxies)
      click_value, max_energy, energy, recovery_energy = GameInfo(headers, proxies)
      # if energy/click_value > 50:
      #   countCollect = 301
      #   while countCollect > 300:
      #     countCollect = random.randint(50,int(energy/click_value))
      # else:
      #   countCollect = int(energy/click_value)
      if energy/click_value > 50:
        countCollect = int(energy/click_value)
        #countCollect = click_value*2000
        collectAmount, collectStatus = Collect(headers, countCollect, proxies)
        now_time = datetime.now().strftime("%H:%M:%S")
        if collectStatus == True:
          print(f"{đen}╔═{đỏ}[{vàng}{now_time}{đỏ}] {trắng}Đã Click {vàng}{countCollect} {trắng}lần {vàng}+{collectAmount}🪙 {đỏ}»", end=" ")
          balance, userLevel, userId = AccountInfo(headers,proxies)
          print(f"🪙{vàng}{balance:,}\n{đen}╚⫸{hồng}Tải tool miễn phí tại Channel Telegram{đỏ}: {lục}@AnubisMMO\n")
        else:
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ} Click nhận coin thất bại\n")
      ChestCount, RecoveryCount, ClickConfig, RecoveryConfig, EnergyConfig, BotConfig = AccountBuild(headers, proxies)
      click_value, max_energy, energy, recovery_energy = GameInfo(headers, proxies)
      if RecoveryCount > 0 and energy/click_value < 50:
        data = recoverCoinPool(headers, proxies)
        if data == True:
          click_value, max_energy, energy, recovery_energy = GameInfo(headers, proxies)
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {lục}Đã khôi phục lại Coin Pool {đỏ}» {vàng}{energy}{đen}/{vàng}{max_energy}\n")
        else:
          now_time = datetime.now().strftime("%H:%M:%S")
          print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ {đỏ}Khôi phục Coin Pool THẤT BẠI\n")
      elif energy/click_value < 50:
        print(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}HẾT LƯỢT CLICK, HẾT BOOTERS {đỏ}» {vàng}ĐỔI TÀI KHOẢN {lục}{ChestCount} {RecoveryCount}\n")
        break
delay = input(f"{lục} NHẬP THỜI GIAN DELAY ĐỂ CHẠY LƯỢT TIẾP THEO{đỏ} : {vàng}")
while True:
 RUN_YESCOIN()
 time.sleep(delay)