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

# RUN pip3 freeze > requirements.txt IN CONSOLE TO UPDATE REQUIREMENTS TEXT