import json
import requests, sys, base64, collections
import urllib3
import getpass
import string

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
JIRA_USERNAME=sys.argv[6]
JIRA_PASS=sys.argv[7]

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


            
            
            #----------------------------------------------------------------
jira_url = 'https://criticaldesign.atlassian.net/rest/servicedeskapi/request'
headers = {"Content-Type": "application/json"}
#jirasm_payload = '{"serviceDeskId": "1", "requestTypeId": "16", "requestFieldValues": {"summary": "Developer Setup Load Balanced VIP via REST", "description": "These are the actions taken"}}'
jirasm_payload = '{"serviceDeskId": "1", "requestTypeId": "16", "requestFieldValues": {"summary": "Developer Setup Load Balanced VIP via REST", "description": "STATUS"}}'
MyString = "The following IP was " + SERVER_STATE + " : " + SERVER_IP
jirasm_payload = jirasm_payload.replace('STATUS', MyString)
r = requests.post(jira_url, auth=(JIRA_USERNAME, JIRA_PASS), data=jirasm_payload, headers=headers)

print(r.status_code)
#print(r.text)
jira_text = r.content
jira_data = json.loads(jira_text)
for link in jira_data['_links'] :
    agent_link = jira_data['_links']['agent']
    print("Jira Service Management Ticket #: " + agent_link)
    #print(agent_link)
    exit()
