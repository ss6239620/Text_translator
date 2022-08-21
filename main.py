import bs4 
import requests

lang=str(input("Please enter the short of language that you want to translate: "))
convert=str(input("Enter the text: "))
url=f"https://translate.google.co.in/m?sl=auto&tl={lang}&hl=en-US&q={convert}"
re=requests.get(url)
soup=bs4.BeautifulSoup(re.text,'lxml')
result=soup.find(class_='result-container')
print(result.get_text())





