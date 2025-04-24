from api.api_models import Quote

from bs4 import BeautifulSoup

import requests as req
import random

class QuoteClient:

    def __init__(self):
        pass

    def get_quote(self):
        return random.choice(self.__get_quotes__())


    def __get_quotes__(self):
        soup = BeautifulSoup(req.get('https://www.infoniac.ru/news/100-korotkih-motiviruyushih-citat-i-fraz-na-kazhdyi-den.html').text, 'html.parser')
        
        list_quotes = soup.find('div', class_='entry')
        quotes = list_quotes.find_all('p')
        
        result = []
        
        for p in quotes:
            text = p.get_text().strip()
            
            if '|' in text:
                _quote_text = '«' + text.split('|')[0].strip() + '»'
                _author = text.split('|')[1].strip()
                
                result.append(Quote(quote_text=_quote_text, quote_author=_author))
        
        return result