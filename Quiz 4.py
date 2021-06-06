import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

url_p = {'cstart': 1}
url = 'https://gtorr.net/index.php?'


file = open('games.csv', 'w', newline='\n', encoding='UTF-8_sig')
file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Year'])

while url_p['cstart'] < 6:
    r = requests.get(url, params=url_p)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')
    games_block = soup.find('div', id='dle-content')
    all_games = games_block.find_all('div', class_='main-news')

    for each in all_games:
        title = each.find('div', class_='main-news-title').text
        year = each.find('span', style='font-family: Fira Sans;').text
        print(year)
        file_obj.writerow([title, year])

    url_p['cstart'] +=1
    sleep(randint(15,20))
