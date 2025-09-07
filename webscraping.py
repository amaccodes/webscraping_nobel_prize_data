import html
import pandas as pd
from bs4 import BeautifulSoup
import requests

# define the url of the website we are interested in 
all_prizes_url = 'https://www.nobelprize.org/prizes/lists/all-nobel-prizes/all/'

response = requests.get(all_prizes_url)

html_ = response.text

soup = BeautifulSoup(html_)


getTitle = lambda tag: tag.h3.a.text.strip()[:-5]
getYear = lambda tag: int(tag.h3.a.text.strip()[-5:])
getDescription = lambda tag: tag.blockquote.text.strip()
get_laureates = lambda soup: [(t.text.strip(), t.get('href')) for t in soup.select('.card-prize--laureates--links--link')]

parsed_prizes = []

for p in soup.select('.card-prize'):
    desc = getDescription(p)
    if 'No Nobel Prize was awarded' in desc:
        continue
    d = {
        'title': getTitle(p),
        'year': getYear(p),
        'laureates': get_laureates(p),
        'description': desc
    }
    parsed_prizes.append(d)

print(f'There are {len(parsed_prizes)} Nobel Prizes to date.')

print(parsed_prizes[-1]) # the first ever Nobel Prize

# lets create a laureates dictionary

laureates_dict = []

for p in parsed_prizes:
    for l in p['laureates']:
        laureates_dict.append({
            'name': l[0],
            'url': l[1],
            'year': p['year'],
            'prize': p['title'],
            'desc': p['description']
        })


df = pd.DataFrame(laureates_dict)

#df.to_csv('/Users/aaronmcdonald/webscraping_nobel_prize_data/scraped_data.csv', index=False)