#curl -D- -u adidonato@criticaldesign.net:APIKEYHERE -X POST
# -H "X-Atlassian-Token: no-check" -F "file=@monitor_test.txt" https://criticaldesign.atlassian.net/rest/api/3/issue/DIP-62/attachments

import requests
username = 'adidonato@criticaldesign.net'
password = 'APIKEYHERE'
files = {'file': open('monitor_status_test.csv', 'rb')}
headers = {"X-Atlassian-Token": "no-check"}
#headers = {"Content-Type": "application/json"}
jurl = 'https://criticaldesign.atlassian.net/rest/api/3/issue/DIP-62/attachments'

r = requests.post(jurl, auth=(username, password), files=files, headers=headers)
print(r.status_code)
print(r.text)
