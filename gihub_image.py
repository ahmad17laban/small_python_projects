import requests 
from bs4 import BeautifulSoup as bs 

github_user = input('enter the username of github user: ')
url = 'https://github.com/'+github_user
r= requests.get(url)

soup = bs(r.content, 'html.parser')
# get the image using html tags and attribute
proflie_image= soup.find('img', {'class':'avatar avatar-user width-full border color-bg-primary'}) ['src']
print(proflie_image)
# src="https://avatars.githubusercontent.com/u/60614075?v=4"