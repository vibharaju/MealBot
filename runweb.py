import requests
from bs4 import BeautifulSoup
from datetime import datetime
class RunWeb:
    def __init__(self):
        self.url = "https://housing.ucdavis.edu/dining/menus/dining-commons/"
        
    def search(self, dc, allergy_word):
        dc_url = self.url + dc.lower() + "/"
        page = requests.get(dc_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        page_body = soup.body
        
        allergy_free = []
        date = datetime.now()
        today = date.strftime("%A, %B %d, %Y")
        
        for item in soup.find_all('h6', text = 'Ingredients'):
            if item.find_previous('h3').text != today:
                continue
            dish = item.find_previous('span')
            ingredients = item.find_next_sibling('p')
            
            if ingredients and allergy_word.lower() not in ingredients.text.lower():
                allergy_free.append(dish.text)
            
        return allergy_free
