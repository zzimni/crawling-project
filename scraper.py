import requests
from bs4 import BeautifulSoup as bs
def get_table_data():
  url = "https://crawlingstudy-dd3c9.web.app/01/" 
response = requests.get(url)
soup = bs(response.text, "lxml")
rows = soup.select("tbody tr")
for row in rows:
  tds = row.select("td")
print(f"이름: {tds[0].text}, 나이: {tds[1].text}")
if __name__ == "__main__":
  get_table_data()