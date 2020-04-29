import json
import urllib.request as ur
import urllib.request, urllib.parse, urllib.error



url = input('Enter url: ')

data = ur.urlopen(url).read().decode('utf-8')

info = json.loads(data)

sum = 0
for item in info["comments"]:
    sum += int(item["count"])
        
print(sum)    