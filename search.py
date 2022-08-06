#--------Enthernet---Code---®-----------
import requests
from bs4 import BeautifulSoup

search = input ('search: ')
result = requests.get(search)
#print(result.text)
print("The status code is ", result.status_code)
print("\n")
soup_data = BeautifulSoup(result.text, 'html.parser')
print(soup_data.title)
print("\n")
tag = input('enter tag to scrap eg(h1, div, span,etc: ')
r = soup_data.find_all(f'{tag}')
with open('target-source.txt', 'a') as p:
 p.write('\n,'.join(map(str,r)))
 p.close()
