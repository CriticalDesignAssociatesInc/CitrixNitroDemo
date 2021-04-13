import json
import requests
import mycreds

network_id = '192.168.99.'
network_0 = "0"
network_255 = "255"

ns_ip = """{ "errorcode": 0, "message": "Done", "severity": "NONE", "nsip": [ { "ipaddress": "192.168.99.19", "td": "0", "type": "NSIP", "netmask": "255.255.255.0", "flags": "40", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "DISABLED", "telnet": "ENABLED", "ssh": "ENABLED", "gui": "ENABLED", "snmp": "ENABLED", "ftp": "ENABLED", "mgmtaccess": "ENABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "ENABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "0", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "1032096", "riserhimsgcode": 32, "iptype": [ "NSIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.20", "td": "0", "type": "SNIP", "netmask": "255.255.255.0", "flags": "12", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "DISABLED", "telnet": "ENABLED", "ssh": "ENABLED", "gui": "ENABLED", "snmp": "ENABLED", "ftp": "ENABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "0", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "1032051", "riserhimsgcode": 4, "iptype": [ "SNIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.21", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.22", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.23", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.24", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.25", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.26", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "1.1.1.1", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "1", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" }, { "ipaddress": "192.168.99.27", "td": "0", "type": "VIP", "netmask": "255.255.255.255", "flags": "8", "arp": "ENABLED", "icmp": "ENABLED", "vserver": "ENABLED", "telnet": "DISABLED", "ssh": "DISABLED", "gui": "DISABLED", "snmp": "DISABLED", "ftp": "DISABLED", "mgmtaccess": "DISABLED", "restrictaccess": "DISABLED", "decrementttl": "DISABLED", "dynamicrouting": "DISABLED", "hostroute": "DISABLED", "advertiseondefaultpartition": "DISABLED", "networkroute": "DISABLED", "tag": "0", "hostrtgwact": "0.0.0.0", "metric": 0, "ospfareaval": "0", "vserverrhilevel": "ONE_VSERVER", "vserverrhimode": "DYNAMIC_ROUTING", "viprtadv2bsd": false, "vipvsercount": "1", "vipvserdowncount": "0", "vipvsrvrrhiactivecount": "0", "vipvsrvrrhiactiveupcount": "0", "ospflsatype": "TYPE5", "state": "ENABLED", "freeports": "0", "riserhimsgcode": 0, "iptype": [ "VIP" ], "icmpresponse": "NONE", "ownernode": "255", "arpresponse": "NONE", "ownerdownresponse": "YES" } ] }"""
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


all_ips = [n for n in range(2, 254)]
print("This is the list of all IPs in the assigned range: ")
print(all_ips, '\n')

first_available_ip = lambda x, y: list((set(x) - set(y))) + list((set(y) - set(x)))
available_ip = first_available_ip(all_ips, list_used)
available_ip = str(available_ip[0])
print("First available IP: ", network_id+available_ip)

jira_url = 'https://criticaldesign.atlassian.net/rest/servicedeskapi/request'
headers = {"Content-Type": "application/json"}
#jirasm_payload = '{"serviceDeskId": "1", "requestTypeId": "16", "requestFieldValues": {"summary": "Developer Setup Load Balanced VIP via REST", "description": "These are the actions taken"}}'
jirasm_payload = '{"serviceDeskId": "1", "requestTypeId": "16", "requestFieldValues": {"summary": "Developer Setup Load Balanced VIP via REST", "description": "STATUS"}}'
MyString = "The following LB VIP was created: " + network_id+available_ip
jirasm_payload = jirasm_payload.replace('STATUS', MyString)
r = requests.post(jira_url, auth=(mycreds.username, mycreds.password), data=jirasm_payload, headers=headers)

print(r.status_code)
#print(r.text)
jira_text = r.content
jira_data = json.loads(jira_text)
for link in jira_data['_links'] :
    agent_link = jira_data['_links']['agent']
    print("Jira Service Management Ticket #: " + agent_link)
    #print(agent_link)
    exit()
