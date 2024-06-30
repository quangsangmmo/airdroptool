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
BANNER()
print(f"""
{đậm}{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}TÙY CHỌN CHỨC NĂNG TOOL

{đỏ}⟨{lục}1{đỏ}⟩ {vàng}CẬP NHẬT PHIÊN BẢN MỚI NHẤT
{đỏ}⟨{lục}2{đỏ}⟩ {vàng}CHẠY TOOL
""")

select_function = input(f"{đỏ}⟩{vàng}⟩{lục}⟩ {trắng}NHẬP CHỨC NĂNG TOOL{đỏ}: {lam}")

if select_function == "1":
  