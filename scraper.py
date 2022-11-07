from bs4 import BeautifulSoup as bs
import requests
import time
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
time.sleep(10)

page = requests.get(url)
soup = bs(page.text, "html.parser")
star_table = soup.find_all("table")
table_rows = star_table[7].find_all('tr')

brown_dwarf_data=[]
for td_tag in soup.find_all("td", attrs={"class", "Brown dwarf"}):
            td_tags = td_tag.find_all("li")
            temp_list = []
            for index, tr_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            brown_dwarf_data.append(temp_list)
new_brown_dwarfs_data = []
def scrape_more_data(hyperlink):

    try:
        page = requests.get(hyperlink)
      
        soup = bs(page.content, "html.parser")

        temp_list = []

        for tr_tag in soup.find_all("tr", attrs={"class": "Pegasus"}):
            td_tags = tr_tag.find_all("td")
          
            for td_tag in td_tags:
                try: 
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
                    
        new_brown_dwarfs_data.append(temp_list)

    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

#Calling method

headers = ['brown_dwarf', 'constellation', 'right_ascension', 'declination', 'app_mag', 'distance', 'spectral_type', 'mass', 'radius', 'discovery_year']


print(new_brown_dwarfs_data[0:10])

final_brown_dwarf_data = []

for index, data in enumerate(brown_dwarf_data):

    new_brown_dwarfs_data_element = new_brown_dwarfs_data_element[index]
    new_brown_dwarfs_data_element = [elem.replace("\n", "") for elem in new_brown_dwarfs_data]
    new_brown_dwarfs_data_element = new_brown_dwarfs_data_element[:7]
    final_brown_dwarf_data.append(data + new_brown_dwarfs_data_element)

with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(new_brown_dwarfs_data)




