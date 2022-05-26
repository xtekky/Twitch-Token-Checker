import requests


def check(token):
    headers = {
        'User-Agent':useragent,
        'Authorization':f'OAuth {token}'
    }
    response = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers)

    if 'client_id' in response.text:
        print(token, file=open('valid_tokens.txt', 'a'))

tokens = []

with open('tokens.txt', 'r') as file:
    for line in file:
        tokens.append(line.rstrip())

for token in tokens:
    threading.Thread(target=check, args=(id,)).start()
