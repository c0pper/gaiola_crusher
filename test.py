from bs4 import BeautifulSoup
from requests import get

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
r = get("https://booking.areamarinaprotettagaiola.it/winter/booking/index.php", headers=headers).content
soup = BeautifulSoup(r, 'html.parser')

print(soup.prettify())