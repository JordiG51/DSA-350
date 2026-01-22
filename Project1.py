import re
import urllib.request
from urllib.request import Request, urlopen
import matplotlib.pyplot as plt
req = Request('https://en.wikipedia.org/wiki/Erwin_Schr%C3%B6dinger', headers = {'User-Agent' : 'Mozilla/5.0'})

hand = urlopen(req)

years = []

for line in hand:
    line = line.decode().strip()
    years_result19 = re.findall('19[0-9]{2}', line)
    years_result20 = re.findall('20[0-2]{0-6}', line)
    if years_result19 != []:
        years += years_result19
    if years_result20 != []:
        years += years_result20

int_years = []
for y in years:
    int_years.append(int(y))

plt.hist(int_years, bins = 60, color = 'red', edgecolor = 'black')

plt.xlabel('Years')
plt.ylabel('Published')
plt.title('Project1')
plt.show()
