import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context 

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districs/zidz-sdfj/about_data"
encoding = 'utf-8'
#Open web page
print(f"Opening{url}...")
webpage = urllib.request.urlopen(url)

print(type(webpage))

#iterate through each line in the webpage and search for <title>
for line in webpage:
    line = line.decode(encoding)
    if '<title>' in line:
        print(line)
