#! python3
"""
Geonames Search Parser
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


#%%
def get_page_data(search_term, country, count):
    url = f"https://www.geonames.org/advanced-search.html?q={search_term}&country={country}&startRow={count}"
    data_raw = requests.get(url)
    data_text = BeautifulSoup((data_raw.text), "html.parser")
    return data_text


#%%
def result_count(search_term, country):
    data = get_page_data(search_term, country, '0')
    count_raw = data.find('small')
    remove_html = str(count_raw).strip('</small>')
    split_text = remove_html.split(' r')
    count_tot = int(split_text[0])
    return count_tot


#%%
def get_header(data):
    header = []
    header_data = data.find_all('th')
    for i in header_data:
        stripped = str(i).strip('</th>')
        header.append(stripped)
    return header


#%%
def get_records(data):
    records = []
    record_data_raw = data.find_all('tr')
    for row in record_data_raw:
        cols = row.find_all('td')
        cols = [element.text.strip() for element in cols]
        records.append([element for element in cols if element])
    return records


#%%
def set_page_table(data):
    header = get_header(data)
    records = get_records(data)
    table_raw = pd.DataFrame(records, columns=header)
    page_table = table_raw.drop([0, 1, 2, 3, 4, 5])
    return page_table


#%%
def get_geoname_query_data(search_term, country):
    data_complete = pd.DataFrame()
    count = result_count(search_term, country)
    pages = range(0, count, 50)
    for i in pages:
        data_raw = get_page_data(search_term, country, str(i))
        table_raw = set_page_table(data_raw)
        data_complete = data_complete.append(table_raw)
    remove_none = data_complete[data_complete.Name != 'None']
    dedupe = remove_none.drop_duplicates()
    data_final = dedupe.set_index('')
    return data_final
