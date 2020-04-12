import requests
from bs4 import BeautifulSoup
list = []

page = requests.get("https://isthereanydeal.com/#/")
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(class_="cntBoxContent")
sales = table.find_all(class_="bundle-container-outer bundle-preview giveaway")
bundles = table.find_all(class_="bundle-container-outer bundle-preview bundle")
links = table.find_all(class_="lg")

for i in range(0,len(links)):
    for link in links[i]:
        list.append(link)


print(list) #Prints text without links
print(sales)
print(bundles)
print(links)

#print(links[0-7]) #Prints in order the items on page.

"""
count = 0
for i in links:
    list.append(i)
    count += 1
    if i == '<span class="lg">':
        list.pop(i[count])
list_pretty = []
length = len(list)
for i in range(length):
    if list[i].find('href') != -1:
        list_pretty.append(list[i])
    else:
        continue
        """