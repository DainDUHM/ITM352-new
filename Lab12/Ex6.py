import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
# Fetch page
response = requests.get(url)

#Check if it was successful
if response.status_code == 200:
    #Parse the HTML
    soup = BeautifulSoup(response.content, "html.parser")

    #GET rate table

    rate_table = soup.find("table")

    if rate_table:
        #Extract rows
        rows = rate_table.find_all("tr")

        #print the table headers
        headers = [header.text.strip() for header in rows[0].find_all("th")]
        print(" | ".join(headers))

        #print each rows data
        for row in rows[1:]:
            cells = [cell.text.strip() for cell in row.find_all("td")]
            print(" | ".join(cells))
    else:
        print("Rate table not found")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")



