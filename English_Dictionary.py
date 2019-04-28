import requests
from bs4 import BeautifulSoup

word = input("Search : ")
url = "https://www.dictionary.com/browse/"+str(word)+"?s=ts"
code = requests.get(url)
soup = BeautifulSoup(code.content,"html.parser")
meaning = soup.find_all('span',{'class':'luna-pos'})[0].text
defination = soup.find_all("ol")
meanings = defination[0].findChildren("li",recursive =False)
for i,pos in enumerate(meanings):
    print(str(i+1), pos.text)
    
