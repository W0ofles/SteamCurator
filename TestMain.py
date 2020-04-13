"""                                                                                 
table = soup.find(class_="cntBoxContent")                                           
sales = table.find_all(class_="bundle-container-outer bundle-preview giveaway")     
bundles = table.find_all(class_="bundle-container-outer bundle-preview bundle")     
links = table.find_all(class_="lg")
gamelist = soup.find_all('a', class_='lg')
prettylist = []

count = 0
for game in gamelist:
    count += 1
    prettylist.append(game)

#print(gamelist)
#print(prettylist)
"""

"""

MY OLD CODE

import requests
from bs4 import BeautifulSoup
pricepage = "https://isthereanydeal.com/#/"
page = requests.get(pricepage) #Request The Page
soup = BeautifulSoup(page.content, 'html.parser') #Soup The Page
gamelist = [] #Create Empty List

for link in soup.find_all('a', class_='lg'): #Find Links
    gamelist.append(link.get('href')) #Get Hrefs
gamelist = list(dict.fromkeys(gamelist)) #Remove Duplicates

print(gamelist)


#sales = table.find_all(class_="bundle-container-outer bundle-preview giveaway")
#bundles = table.find_all(class_="bundle-container-outer bundle-preview bundle")
    
"""


# RUN pip3 freeze > requirements.txt IN CONSOLE TO UPDATE REQUIREMENTS TEXT