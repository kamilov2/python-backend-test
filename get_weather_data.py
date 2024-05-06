import requests
from bs4 import BeautifulSoup

url = "https://nbu.uz/uz/"
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=HEADERS)

# print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
ul_money = soup.find_all("ul")[2] 
money_weather = []
links = ul_money.find_all("a")
for link in links:
    try:
        value = link.find("span").text 
    except Exception as e:
        pass
    else:
        money_weather.append(value.strip())
print(money_weather)