import json
import requests, sys, base64, collections
import urllib3
import getpass

#Disable SSL Warnings if cert is untrusted
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#User input server IP Address
NITRO_SERVER=sys.argv[1]

#User input username
NITRO_USER=sys.argv[2]

#User input password
try:
    NITRO_PWD=sys.argv[3]
except Exception as error:
    print ('ERROR',error)

SERVER_IP=sys.argv[4]

SERVER_STATE=sys.argv[5]

headers={
"X-NITRO-USER":NITRO_USER,
"X-NITRO-PASS":NITRO_PWD,
"Content-Type": "application/json"
}

server_response = requests.get("https://%s/nitro/v1/config/server" % (NITRO_SERVER), auth=(NITRO_USER, NITRO_PWD),
                             verify=False)

server_data = json.loads(server_response.text)

for l in server_data['server']:
    svrname = l["name"]
    svrip = l["ipaddress"]

    #print(svrip + "=" + SERVER_IP + "?")
    if svrip == SERVER_IP:
        if SERVER_STATE == 'disable':
            payload = {
            "server":
            {
            "name": svrname
            }
            }
            change_state = requests.post("https://%s/nitro/v1/config/server?action=disable"%(NITRO_SERVER),headers=headers,data=json.dumps(payload),verify=False)
            print(change_state)
        else:
            payload = {
            "server":
            {
            "name": svrname
            }
            }
            change_state = requests.post("https://%s/nitro/v1/config/server?action=enable"%(NITRO_SERVER),headers=headers,data=json.dumps(payload),verify=False)

