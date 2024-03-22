from colorama import *
import time
import requests
from datetime import datetime
import os


logo = f'''{Fore.LIGHTMAGENTA_EX}            .-.
           ((`-)
            \\
             \\
      .="""=._))
     /  .,   .'
    /__(,_.-'
   `    /|
       /_|__
         | `))
         |
         
{Fore.LIGHTRED_EX}Made by GoT Flamingo
{Fore.LIGHTYELLOW_EX}Github.com/gotflamingo 
'''

def lookup(id_address):
    url = f"https://dashboard.botghost.com/api/public/tools/user_lookup/{id_address}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        avatar_id = data.get('avatar', "Not available")
        avatar_url = f"https://cdn.discordapp.com/avatars/{id_address}/{avatar_id}.png"
        
        creation_date = datetime.utcfromtimestamp(((int(id_address) >> 22) + 1420070400000) / 1000).strftime('%Y-%m-%d %H:%M:%S')
        
        return {
            "Discord ID": id_address,
            "Username": data.get('username', "Not available"),
            "Avatar": avatar_url,
            "Global Name": data.get('global_name', "Not available"),
            "Discriminator": data.get('discriminator', "Not available"),
            "Public Flags": data.get('public_flags', "Not available"),
            "Nitro: ": "Nej" if data.get('premium_type') == 0 else data.get('premium_type', "Not available"), 
            "Flags": data.get('flags', "Not available"),
            "Banner": "Ingen" if data.get('Banner') == None else data.get('banner', "Not available"),
            "Creation Date": creation_date
        }
    else:
        return {'Error': 'Failed to retrieve data'}
os.system("cls")
print(logo)
ID = input(f"{Fore.LIGHTGREEN_EX}ID:{Fore.LIGHTWHITE_EX} ")
result = lookup(ID)
print(" ")
for key, value in result.items():
    print(f"{Fore.LIGHTRED_EX}{key}{Fore.LIGHTCYAN_EX}: {Fore.WHITE}{value}")  
time.sleep(10)
