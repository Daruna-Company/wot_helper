from config import info

import requests
from bs4 import BeautifulSoup

def get_user_page(user_id):
    url = info["web"].format(user_id)
    r = requests.get(url)
    return r.text

def get_user_data(user_page):
    soup = BeautifulSoup(user_page) 
    r1 = soup.find_all('div', {'class': 'well well-sm'})
    r2 = soup.find_all('h2')

    g1 = soup.find_all('div', {'class': 'well'})
    g2 = soup.find_all('h3', {'style': 'margin: 0;text-shadow: 1px 1px 1px rgba(0,0,0,0.3);'})

    result = []
    
    result.append(g2[0].text[2:]) #RE
    result.append(g2[1].text[3:]) #WN6
    result.append(g2[2].text[3:]) #WN7
    result.append(g2[3].text[6:]) #MGR

    for i in r2:
        result.append(i.text)

    return result

print(get_user_data(get_user_page(131506209)))
