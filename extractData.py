import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime 

def extractData():

    url = "https://services2.hdb.gov.sg/webapp/BP13BTOENQWeb/BP13J011SBFNov20.jsp"

    # HDB website blocks access from non-browsers, trick the website to think we are accessing using FireFox
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    # Create handle to get page and store HTML
    page = requests.get(url, headers = headers).text

    # Parse data
    soup = BeautifulSoup(page, "html.parser")

    # Identify the two tables for extraction
    tables = soup.find_all("table", attrs = {"class": "scrolltable"})

    # Initiate the two tables for collecting data
    data2R = []
    data3RandBigger = []
    def extractData(t, tableTitle):
        row = []
        tables_data = t.tbody.find_all("tr")
        for td in tables_data[-1].find_all("td"):
            row.append(td.text.replace('/n', " ").strip())

        # Append extraction time
        row.append(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        tableTitle.append(row)

    # Execute function to extract data for each table - 2R and 3R or bigger
    extractData(tables[0], data2R)
    extractData(tables[1], data3RandBigger)
  

    return(data2R, data3RandBigger)
