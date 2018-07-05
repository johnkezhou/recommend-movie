
import requests

url = 'https://www.bitkk.com/globalmarket'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
html = requests.get(url,verify=False, headers=header).content
print html
