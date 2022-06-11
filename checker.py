import httpx, json, random, os, threading, time, requests, subprocess, sys
from colorama import Fore
from cryptography.fernet import Fernet

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
cls()

success = Fore.GREEN + " [" + Fore.RESET + "V" + Fore.GREEN + "] " + Fore.RESET
faild = Fore.RED + " [" + Fore.RESET + "V" + Fore.RED + "] " + Fore.RESET
waiting = Fore.YELLOW + " [" + Fore.RESET + "0" + Fore.YELLOW + "] " + Fore.RESET
onlp =  Fore.LIGHTCYAN_EX + " [" + Fore.RESET + "Z" + Fore.LIGHTCYAN_EX + "] " + Fore.RESET


x1='  __    __   __   __        ___  __        ___  __  '
x2='   / | |__) /  \ /  ` |__| |__  /  ` |__/ |__  |__) '
x3='  /_ | |  \ \__/ \__, |  | |___ \__, |  \ |___ |  \ '
     
os.system("mode con cols=80 lines=20")
os.system("title OnlpChecker")

print("\n"+Fore.LIGHTBLUE_EX+x1)
print(x2)
print(Fore.BLUE+x3, Fore.RESET+"\n\n")

class Data():  
    ids = """"""      
    hits = 0
    locked = 0
    invalid = 0
    ta = 0
    left = 0
    threadingx = 0
    
page_list = ['fortnite','grand theft auto v','just chatting','FIFA 22']


def follow(token,proxy):
    Data.ta = Data.ta + 1
    id = random.choice(Data.ids.splitlines())
    while True:
        try:
            xproxy = random.choice(proxy)
            prox = {
                "https": "http://" + xproxy,
                "http": "http://" + xproxy,
            }
            headers = {'Connection': 'keep-alive','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"','Accept-Language': 'en-US','sec-ch-ua-mobile': '?0','Client-Version': 'bdcf138a-e9ce-4710-836b-82c8974c0a4d','Authorization': 'OAuth '+token,'Content-Type': 'text/plain;charset=UTF-8','User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",'Client-Session-Id': 'fd9996a9be67b78f','Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko','X-Device-Id': 'ZCee2Car4erCGaovCA9xuofRwhHfzocw','sec-ch-ua-platform': '"Windows"','Accept': '*/*','Origin': 'https://www.twitch.tv','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.twitch.tv/',}
            data = [{"operationName": "FollowButton_FollowUser","variables": {"input": {"disableNotifications": False,"targetID": id}},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"}}}]
            response = requests.post('https://gql.twitch.tv/gql', headers=headers, data=json.dumps(data),proxies=prox,timeout=20)
            break
        except:
            None
    try:
        if response.json()[0]['data']['followUser']['error']['code'] == "FORBIDDEN":
            Data.locked = Data.locked + 1
            open("out/locked.txt","a").write(token + "\n")
    except:
        None
    try:
        if response.json()['error'] == "Unauthorized":
            Data.invalid = Data.invalid + 1
    except:
        None
    try:
        if response.json()[0]['data']['followUser']['follow']['user']['id'] == id:
            Data.hits = Data.hits + 1
            open("out/valid.txt","a").write(token + "\n")
    except:
        None
    Data.left = Data.left - 1
    Data.ta = Data.ta - 1
    
    None
def start(): 
    def get_int():
        cls()
        try:
            print("")
            Data.threadingx = int(input(" [!] Threads: "))
        except:
            cls()
            print("\n INT ERROR")
            time.sleep(1)
            cls()
            get_int()
    get_int()
    for x in page_list:
        try:      
            headers = {'Connection': 'keep-alive','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"','Accept-Language': 'en-US','sec-ch-ua-mobile': '?0','Client-Version': 'bdcf138a-e9ce-4710-836b-82c8974c0a4d','Authorization': 'OAuth z3tmlx9j2uu692bdc9xfdjef8v7jw2','Content-Type': 'text/plain;charset=UTF-8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36','Client-Session-Id': 'fd9996a9be67b78f','Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko','X-Device-Id': 'ZCee2Car4erCGaovCA9xuofRwhHfzocw','sec-ch-ua-platform': '"Windows"','Accept': '*/*','Origin': 'https://www.twitch.tv','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.twitch.tv/',}
            data = [{"operationName": "DirectoryPage_Game","variables": {"name": x,"options": {"includeRestricted": ["SUB_ONLY_LIVE"],"sort": "VIEWER_COUNT_ASC","recommendationsContext": {"platform": "web"},"requestID": "JIRA-VXP-2397","tags": []},"sortTypeIsRecency": False,"limit": 100},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "d5c5df7ab9ae65c3ea0f225738c08a36a4a76e4c6c31db7f8c4b8dc064227f9e"}}}]
            response = httpx.post('https://gql.twitch.tv/gql', headers=headers, data=json.dumps(data))
            jsonx =  response.json()
            for i in range(100):
                try:
                    randomid = jsonx[0]['data']['game']['streams']['edges'][i]['node']['broadcaster']['id']
                    Data.ids = Data.ids + randomid + "\n"
                except:
                    None
        except:
            print("\n [x] ID Scrape error\n")
            time.sleep(2)

    proxy = open("proxy.txt", "r").read().splitlines()
    tokens = open("token.txt", "r").read().splitlines()
    
    Data.left = len(tokens)
    if Data.left == 0:
        print("\n [!] 0 Tokens in token.txt")
        time.sleep(3)
    if len(proxy) == 0:
        print("\n [!] 0 Proxy in proxy.txt")
        time.sleep(3)

    def title():
        start_time = time.time()
        while True:
            
            if Data.left == 0:
                cls()
                print("\n FINISHED")
                time.sleep(3)
                break
            timex = " %s  " % (time.time() - start_time)
            sep = "."
            stripped = timex.split(sep, 1)[0]
            def cpm():
                try:
                    if int(Data.hits) + int(Data.invalid)+ int(Data.locked)  == 0:
                        return 0
                    else:
                        cxtime = float(stripped) / 60
                        xxtime = cxtime / 60
                        xxx = str(int(Data.hits) + int(Data.invalid)+ int(Data.locked) / xxtime)
                        strippedx = xxx.split(sep, 1)[0]
                        return strippedx
                except:
                    return 0
                
            timex = " %s  " % (time.time() - start_time)
            sep = "."
            stripped = timex.split(sep, 1)[0]
            os.system(f"title  OnlpChecker v1")
            os.system("mode con cols=30 lines=8") 
            def print_stats():
                print("\n")
                print(success +   f" HITS: {str(Data.hits)}")
                print(waiting +   f" LOCKED: {str(Data.locked)}")
                print(faild +   f" INVALID: {str(Data.invalid)}")
                print()
                print(onlp +    f" TIME: {stripped}")
                print(onlp +    f" LEFT: {str(Data.left)}")
            print_stats()
            time.sleep(1)
            cls()
            
            
    threading.Thread(target=title).start()
    
    for i in tokens:
        while True:
            if Data.ta < Data.threadingx:
                threading.Thread(target=follow,args=(i,proxy)).start()
                break


start()

   
