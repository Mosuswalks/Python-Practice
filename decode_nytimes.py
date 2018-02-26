import requests
from bs4 import BeautifulSoup

nyTimes = requests.get('https://www.nytimes.com/?WT.z_jog=1&hF=f&vS=undefined')


soup = BeautifulSoup(nyTimes.content,"utf-8")


print(soup.title)