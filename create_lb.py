import json
import requests, sys, base64, collections
import urllib3
import getpass
import random
import string
import time
#import mycreds


#Disable SSL Warnings if cert is untrusted
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#variables
JIRA_USERNAME=sys.argv[11]
JIRA_PASS=sys.argv[12]
NITRO_SERVER= sys.argv[1]
#NITRO_SERVER="192.168.99.19"
#User input username
NITRO_USER= sys.argv[2]
#NITRO_USER="nsroot"
#User input password
try:
    NITRO_PWD = sys.argv[3]
except Exception as error:
    print('ERROR', error)
#NITRO_PWD="nsroot"
app_name = sys.argv[4]
app_port = sys.argv[5]
lb_serviceType = sys.argv[6]
#Use Autoselect
#lb_IPadd = sys.argv[7]


headers = {
"X-NITRO-USER":NITRO_USER,
"X-NITRO-PASS":NITRO_PWD,
"Content-Type": "application/json"
}

network_id = '192.168.99.'
network_0 = "0"
network_255 = "255"

#ns_ip = """{ "errorcode": 0, "message": "Done", "severity": "NONE", "nsip": [ { "ipaddress": "192.168.99.19", "td": "0", "type": "NSIP", "netmask": "255.255.255.0", "flags": "40", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "DISABLED", "telnet": "ENABLED", "ssh": "ENABLED", "gui": "ENABLED", "snmp": "ENABLED", "ftp": "ENABLED", "mgmtaccess": "ENABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "ENABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "0", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "1032096", "riserhimsgcode": 32, "iptype": [ "NSIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.20", "td": "0", "type": "SNIP", "netmask": "255.255.255.0", "flags": "12", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "DISABLED", "telnet": "ENABLED", "ssh": "ENABLED", "gui": "ENABLED", "snmp": "ENABLED", "ftp": "ENABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "0", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "1032051", "riserhimsgcode": 4, "iptype": [ "SNIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.21", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.22", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.23", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.24", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.25", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.26", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "1.1.1.1", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "1", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.27", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" } ] }"""
ns_ip_r = requests.get("https://%s/nitro/v1/config/nsip"%(NITRO_SERVER),headers=headers,verify=False)
ns_ip = ns_ip_r.text
print(ns_ip, '\n')

data = json.loads(ns_ip)
list_used = []
for i in data['nsip']:
    #print(i["ipaddress"])
    used_ip_address = i["ipaddress"]
    used_ip_address = used_ip_address.split(".")
    #print(used_ip_address[3])
    list_used.append(int(used_ip_address[3]))
print("")
print("The following IPs are in use for subnet: "+network_id)
print(list_used, '\n')


all_ips = [n for n in range(30, 254)]
print("This is the list of all IPs in the assigned range: ")
print(all_ips, '\n')

first_available_ip = lambda x, y: list((set(x) - set(y))) + list((set(y) - set(x)))
available_ip = first_available_ip(all_ips, list_used)
available_ip = str(available_ip[0])
print("First available IP: ", network_id+available_ip)

lb_IPadd = network_id+available_ip
lb_name = "VS-LB-PRI-" + app_name + "-" + app_port
svg_name = "SVG-PRI-" + app_name + "-" + app_port
print(lb_IPadd)
print(lb_name)
print(svg_name)


def create_lb():


    #type(int(app_port))


    payload = {
    "lbvserver": 
    {
    "name":lb_name,
    "servicetype":lb_serviceType,
    "ipv46":lb_IPadd,
    "port":app_port
    } 
    }

    lbvs_response = requests.post(url="https://%s/nitro/v1/config/lbvserver"%(NITRO_SERVER),headers=headers,data=json.dumps(payload),verify=False)
    print(lbvs_response)
    print(lbvs_response.content)

def create_svg():



    payload= {
    "servicegroup": 
    {
    "servicegroupname":svg_name,
    "servicetype":svg_type
    } 
    }
    svg_resp=requests.post(url="https://%s/nitro/v1/config/servicegroup"%(NITRO_SERVER),headers=headers,data=json.dumps(payload),verify=False)
    print(svg_resp)
    print(svg_resp.content)
    
    print(lb_name)
    if lb_name:
        bind_svg= {
        "lbvserver_servicegroup_binding":
        {
        "name":lb_name,
        "servicegroupname":svg_name
        }
        }
        svg_bind_resp=requests.post(url="https://%s/nitro/v1/config/lbvserver_servicegroup_binding"%(NITRO_SERVER),headers=headers,data=json.dumps(bind_svg),verify=False)
        print(svg_bind_resp)
        print(svg_bind_resp.content)
        return(svg_name)

def create_servers():


    payload = {
    "server": 
    {
    "name":server_name,
    "ipaddress":server_ip
    } 
    }
    server_resp=requests.post(url="https://%s/nitro/v1/config/server"%(NITRO_SERVER),headers=headers,data=json.dumps(payload),verify=False)
    print(server_resp)
    print(server_resp.content)
    
    print(svg_name)
    if svg_name:
        bind_server={
        "servicegroup_servicegroupmember_binding":
        {
        "servicegroupname":svg_name,
        "port":server_port,
        "servername":server_name
        }
        }
        
        server_bind_resp=requests.post(url="https://%s/nitro/v1/config/servicegroup_servicegroupmember_binding"%(NITRO_SERVER),headers=headers,data=json.dumps(bind_server),verify=False)
        print(server_bind_resp)
        print(server_bind_resp.content)



if __name__=="__main__":

    create_lb()
    svg_type = sys.argv[7]
    create_svg()
    
#    while True:
#        a = input("Add Backend Server? (y/n) ").lower()
#        if a == "y":
    server_name = sys.argv[8]
    server_ip = sys.argv[9]
    server_port = sys.argv[10]
    create_servers()
#        elif a == "n":
#            break
#        else:
#            print("Enter y/n")




#---------------------------------------------------------------------





jira_url = 'https://criticaldesign.atlassian.net/rest/servicedeskapi/request'
headers = {"Content-Type": "application/json"}
#jirasm_payload = '{"serviceDeskId": "1", "requestTypeId": "16", "requestFieldValues": {"summary": "Developer Setup Load Balanced VIP via REST", "description": "These are the actions taken"}}'
jirasm_payload = '{"serviceDeskId": "1", "requestTypeId": "16", "requestFieldValues": {"summary": "Developer Setup Load Balanced VIP via REST", "description": "STATUS"}}'
MyString = "The following LB VIP was created: " + network_id+available_ip
jirasm_payload = jirasm_payload.replace('STATUS', MyString)
r = requests.post(jira_url, auth=(JIRA_USERNAME, JIRA_PASS), data=jirasm_payload, headers=headers)

print(r.status_code)
print(r.text)


#---------------------------------------------------------------
