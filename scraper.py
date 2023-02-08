import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.cnn.com/2023/02/07/politics/models-biden-state-of-the-union-former-presidents-fault-lines'
res = requests.get(baseurl)

soup = BeautifulSoup(res.text)
print(soup)

body  = soup.find_all(class_="article__content")

article = ''
for p_tag in body:
    p_text = p_tag.get_text()
    article += p_text

text_file = open(r'text.txt', 'w')
text_file.write(article)
text_file.close()