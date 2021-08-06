import requests

url = 'https://www.zomato.com/melbourne/pho-hung-vuong-springvale-springvale'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}


page = requests.get(url, headers=headers)
print(page.text)
