#! python3
# Used to get a quick update on Coronavirus stats
import requests, os, bs4

url = 'https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
tableElem = soup.find_all('table')


for table in range(len(tableElem)):
    tableRows = tableElem[table].find_all('tr')
    for tr in tableRows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        print(row)
