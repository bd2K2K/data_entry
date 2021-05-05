TARGET_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.74300612402344%2C%22east%22%3A-122.25548781347656%2C%22south%22%3A37.52711679625716%2C%22north%22%3A37.926289353244634%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
from bs4 import BeautifulSoup
import requests
import lxml
from data_entry import DataEntry


my_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"

}
response = requests.get(url=TARGET_URL, headers = my_header)
print(response)

zillow_web_page = response.content
soup = BeautifulSoup(zillow_web_page,"lxml")
front_link = "https://www.zillow.com"
house_rent_list=[]
house_adress_list =[]
house_link_list =[]
prices = soup.find_all('div', attrs={"class":"list-card-price"})
for price in prices:
    house_rent = price.text.split("/")[0]
    house_rent = house_rent.split("+")[0]
    house_rent = house_rent.split(" ")[0]
    house_rent_list.append(house_rent)


adresses = soup.find_all('div', attrs={"class":"list-card-info"})
for adres1 in adresses:
    house_adr = adres1.text
    house_adr = house_adr.split("CA")[0]
    house_adr = house_adr + "CA"
    house_adress_list.append(house_adr)
    link = adres1.a.get("href")
    if link[0:5] == "https":
        real_link = link
    else:
        real_link = front_link + link
    house_link_list.append(real_link)

house = DataEntry(house_adress_list, house_rent_list, house_link_list)
house.fill_form()
