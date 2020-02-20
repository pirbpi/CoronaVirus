#! python3
# Used to get a quick update on Coronavirus stats
import requests, os, bs4, openpyxl

def scrapeWeb():
    url = 'https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    tableElem = soup.find_all('table')

    coronaData = {} # Dictionary to hold the Coronavirus stats

    for table in range(len(tableElem)):
        tableRows = tableElem[table].find_all('tr')
        for tr in tableRows[1:]:
            td = tr.find_all('td')
            row = [i.text for i in td]
            country = row[0]
            confirmedCases = row[1].replace(',','')
            confirmedDeaths = row[2].replace(',','')
            notes = row[3]

            # Make sure the key for this country exists:
            coronaData.setdefault(country, {'Cases':'0', 'Deaths':'0', 'Notes':''})
            coronaData[country]['Cases'] = confirmedCases # Add number of cases
            coronaData[country]['Deaths'] = confirmedDeaths # Add number of deaths
            coronaData[country]['Notes'] = notes # Add any notes that exist
    addSpreadsheet(coronaData)

def addSpreadsheet(statsDictionary):
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']
    print(statsDictionary)
    wb.save('coronaTracker.xlsx')

scrapeWeb()
