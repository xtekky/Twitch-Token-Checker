import requests, time, sys, os, threading, random


class Main:
    def __init__(self):

        self.user_list = self.scrape()

        self.tokens  = open("tokens.txt", "r").read().splitlines()
        self.proxies = open("proxies.txt", "r").read().splitlines()

        self.valid = 0
        self.invalid = 0
        self.locked = 0

        threading.Thread(target=self.title).start()
        
        

        self.check()

    def title(self):
        while True:
            os.system(f'title Twitch Checker ^| Valid ~ {self.valid} ^| Invalid ~ {self.valid} ^| Locked ~ {self.valid}')
            time.sleep(1)

    def check(self):
        while True:
            try:
                _token = random.choice(self.tokens)
                _id = random.choice(self.user_list)
                _xproxy = random.choice(self.proxies)
                response = requests.post(
                    'https://gql.twitch.tv/gql',
                    headers={
                            "Authorization": f"OAuth {_token}",
                            "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
                            "Client-Version": "29faedea-0f42-4ebb-a2e2-eaa436496718",
                            "Origin": "https://www.twitch.tv",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
                        },
                    json=[
                        {
                            "operationName": "FollowButton_FollowUser",
                            "variables":
                                {
                                    "input":
                                        {
                                            "disableNotifications": False,
                                            "targetID": _id
                                        }
                                },
                            "extensions":
                                {
                                    "persistedQuery":
                                        {
                                            "version": 1,
                                            "sha256Hash": "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"
                                        }
                                }
                        }
                    ],
                    proxies = {
                        "https": f"http://{_xproxy}",
                        "http": f"http://{_xproxy}"
                    },
                    timeout = 20
                )
                try:
                    if response.json()[0]['data']['followUser']['error']['code'] == "FORBIDDEN":
                        self.locked += 1
                        open("out/locked.txt", "a").write(_token + "\n")
                except:
                    pass
                try:
                    if response.json()['error'] == "Unauthorized":
                        self.invalid += 1
                        open("out/invalid.txt", "a").write(_token + "\n")
                except:
                    pass
                try:
                    if response.json()[0]['data']['followUser']['follow']['user']['id'] == _id:
                        self.valid += 1
                        open("out/valid.txt", "a").write(_token + "\n")
                except:
                    pass
            except:
                pass

    @staticmethod
    def scrape():
        _list = []

        for x in ['fortnite', 'grand theft auto v', 'just chatting', 'FIFA 22']:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                    'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                }

                data = [
                    {
                        "operationName": "DirectoryPage_Game",
                        "variables":
                            {
                                "name": x,
                                "options": {
                                    "includeRestricted":
                                        [
                                            "SUB_ONLY_LIVE"
                                        ],
                                    "sort": "VIEWER_COUNT_ASC",
                                    "recommendationsContext":
                                        {
                                            "platform": "web"
                                        },
                                    "requestID": "JIRA-VXP-2397",
                                    "tags": [
                                    ]
                                },
                                "sortTypeIsRecency": False,
                                "limit": 100
                            },
                        "extensions":
                            {
                                "persistedQuery":
                                    {
                                        "version": 1,
                                        "sha256Hash": "d5c5df7ab9ae65c3ea0f225738c08a36a4a76e4c6c31db7f8c4b8dc064227f9e"
                                    }
                            }
                    }
                ]

                response = requests.post('https://gql.twitch.tv/gql', headers=headers, json=data)
                jsonx = response.json()

                for _ in jsonx[0]['data']['game']['streams']['edges']:
                    _list.append(_['node']['broadcaster']['id'])

            except Exception:
                pass

        if len(_list) < 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            input("Error while scraping id's")
            sys.exit("Error while scraping id's")

        return _list

   Main()
