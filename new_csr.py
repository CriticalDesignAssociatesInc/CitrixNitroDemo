from OpenSSL import crypto
from pathlib import Path
import os
import sys
import datetime
import paramiko
import select
from scp import SCPClient
import getpass
import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TYPE_RSA = crypto.TYPE_RSA
home = os.getenv("HOME")
# print(home)
now = datetime.datetime.now()
d = now.date()
port = 22
WIN_IP = sys.argv[1]
WIN_USER = sys.argv[2]
try:
    WIN_PWD = sys.argv[3]
except Exception as error:
    print('ERROR', error)
hn = sys.argv[4]
cn = sys.argv[5]
sn = hn + '.' + cn
key = crypto.PKey()
keypath = home + "/" + hn + '-' + str(d) + '.key'
csrpath = home + "/" + hn + '-' + str(d) + '.csr'
cerpath = home + "/" + hn + '-' + str(d) + '.cer'


def generatekey():
    if os.path.exists(keypath):
        print("Certificate file exists, aborting")
        print(keypath)
        sys.exit(1)
    else:
        print("Generating Key Please standby")
        key.generate_key(TYPE_RSA, 4096)
        f = open(keypath, "w")
        res = str(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
        res = res.replace('\\n', '\n').replace("b'", "").replace("'", "")
        f.write(res)
        f.close()


def generatecsr():
    req = crypto.X509Req()
    req.get_subject().CN = sn
    req.get_subject().C = c
    req.get_subject().ST = st
    req.get_subject().L = l
    req.get_subject().O = o
    req.get_subject().OU = ou
    req.set_pubkey(key)
    req.sign(key, "sha256")

    if os.path.exists(csrpath):
        print("Certificate File Exists, aborting")
        print(csrpath)
    else:
        f = open(csrpath, "w")
        resp = str(crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))
        resp = resp.replace('\\n', '\n').replace("b'", "").replace("'", "")
        f.write(resp)
        f.close()
        print('success')


print("Key stored here:" + keypath)
print("CSR stored here:" + csrpath)


def reqcert():
    win_home = "\\Users\\" + WIN_USER + "\\"
    ps_script = '''certreq -submit -config dc01.training.lab\\training-dc01-ca -attrib "CertificateTemplate:WebServer" ''' + win_home + hn + '-' + str(
        d) + '.csr ' + win_home + hn + '-' + str(d) + '.cer'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(WIN_IP, username=WIN_USER, password=WIN_PWD)
    scp = SCPClient(ssh.get_transport())
    scp.put(csrpath, hn + '-' + str(d) + '.csr')

    print("done")
    stdin, stdout, stderr = ssh.exec_command(ps_script)

    while not stdout.channel.exit_status_ready():
        if stdout.channel.recv_ready():
            rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
            if len(rl) > 0:
                print(stdout.channel.recv(1024))
    scp.get(hn + '-' + str(d) + '.cer', cerpath)
    print("Command done, closing SSH connection")
    scp.close()
    ssh.close()


def add_certkey():

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(NITRO_SERVER, username=NITRO_USER, password=NITRO_PWD)
    scp = SCPClient(ssh.get_transport())
    scp.put(cerpath, "/nsconfig/ssl/")
    scp.put(keypath, "/nsconfig/ssl/")

    scp.close()
    ssh.close()

    headers = {
        "X-NITRO-USER": NITRO_USER,
        "X-NITRO-PASS": NITRO_PWD,
        "Content-Type": "application/json"
    }

    payload = {
        "sslcertkey":
            {
                "certkey": hn + '-' + str(d),
                "cert": hn + '-' + str(d) + '.cer',
                "key": hn + '-' + str(d) + ".key"
            }
    }

    cert_resp = requests.post(url="https://%s/nitro/v1/config/sslcertkey" % (NITRO_SERVER), headers=headers,
                              data=json.dumps(payload), verify=False)
    print(cert_resp)
    print(cert_resp.content)

    lbvs_response = requests.get("https://%s/nitro/v1/config/lbvserver" % (NITRO_SERVER), auth=(NITRO_USER, NITRO_PWD),
                                 verify=False)

    lbvs_data = json.loads(lbvs_response.text)

    # for each lbvserver in lbvs_data get the name and current state
    for j in lbvs_data['lbvserver']:
        lbvs_name = j['name']
        lbvs_ip = j['ipv46']
        lbvs_type = j['servicetype']

        if lbvs_ip == vip:
            if lbvs_type == 'SSL':
                payload = {
                    "sslvserver_sslcertkey_binding":
                        {
                            "vservername": lbvs_name,
                            "certkeyname": hn + '-' + str(d)
                        }
                }
                lbvs_response = requests.put(
                    "https://%s/nitro/v1/config/sslvserver_sslcertkey_binding" % (NITRO_SERVER), headers=headers,
                    data=json.dumps(payload), verify=False)


if __name__ == "__main__":
    generatekey()
    c = sys.argv[6]
    st = sys.argv[7]
    l = sys.argv[8]
    o = sys.argv[9]
    ou = sys.argv[10]
    generatecsr()
    reqcert()
    bind_cert = sys.argv[11]
    if bind_cert == "y":
        NITRO_SERVER = sys.argv[12]
        NITRO_USER = sys.argv[13]
        NITRO_PWD = sys.argv[14]
        vip = sys.argv[15]
        add_certkey()
    else:
        exit(-1)
        
        
        
JIRA_USERNAME = sys.argv[16]
JIRA_PASS = sys.argv[17]

jira_url = 'https://criticaldesign.atlassian.net/rest/servicedeskapi/request'
jheaders = {"Content-Type": "application/json"}
#jirasm_payload = '{"serviceDeskId": "1", "requestTypeId": "16", "requestFieldValues": {"summary": "Developer Setup Load Balanced VIP via REST", "description": "These are the actions taken"}}'
jirasm_payload = '{"serviceDeskId": "1", "requestTypeId": "16", "requestFieldValues": {"summary": "Developer Setup Load Balanced VIP via REST", "description": "STATUS"}}'
MyString = hn + "'s certificate was updated" 
jirasm_payload = jirasm_payload.replace('STATUS', MyString)
r = requests.post(jira_url, auth=(JIRA_USERNAME, JIRA_PASS), data=jirasm_payload, headers=jheaders)

print(r.status_code)
#print(r.text)
jira_text = r.content
jira_data = json.loads(jira_text)
for link in jira_data['_links'] :
    agent_link = jira_data['_links']['agent']
    print("Jira Service Management Ticket #: " + agent_link)
    print(agent_link, '\n')
    
